"""Package commit-addressed Neolink test releases using only the standard library."""

import argparse
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import tempfile
import zipfile


TARGETS = {
    "x86_64-unknown-linux-gnu": "Linux x64 (Ubuntu 24.04 or compatible, glibc >= 2.39)",
    "aarch64-unknown-linux-gnu": "Linux ARM64 (Ubuntu 24.04 or compatible, glibc >= 2.39)",
    "x86_64-pc-windows-msvc": "Windows x64, with GStreamer runtime included",
    "aarch64-apple-darwin": "macOS 15+ on Apple Silicon, with Homebrew",
}


def git(root, *arguments):
    return subprocess.check_output(["git", "-C", str(root), *arguments])


def identity(root, commit, repository):
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected a full, lowercase Git commit SHA")
    if not re.fullmatch(r"[\w.-]+/[\w.-]+", repository):
        raise ValueError("Expected repository owner/name")
    if git(root, "rev-parse", "HEAD").decode().strip() != commit:
        raise ValueError("The checkout does not match the requested release commit")
    return {
        "kind": "test",
        "commit": commit,
        "short_commit": commit[:12],
        "repository": repository,
        "source_url": f"https://github.com/{repository}/tree/{commit}",
        "commit_timestamp": int(git(root, "show", "-s", "--format=%ct", commit)),
    }


def build_document(info, target=None):
    commit = info["commit"]
    text = (
        f"# Neolink test build {info['short_commit']}\n\n"
        "This is an experimental test prerelease, not a stable version.\n\n"
        f"Source commit: `{commit}`\n\n"
        f"Source: {info['source_url']}\n\n"
        f"Documentation: https://github.com/{info['repository']}/tree/{commit}/docs\n\n"
        "The matching source archive and SHA-256 checksums are attached to the release.\n"
        "The GStreamer feature is enabled; the optional pushnoti feature is not enabled.\n\n"
    )
    if target:
        text += f"Target: `{target}` — {TARGETS[target]}.\n\n"
        if "linux" in target:
            text += (
                "Install runtime dependencies on Ubuntu 24.04:\n\n"
                "```sh\nsudo apt-get update\nsudo apt-get install -y \\\n"
                "  libgstrtspserver-1.0-0 libgstreamer1.0-0 libglib2.0-0t64 libssl3t64 \\\n"
                "  gstreamer1.0-plugins-base gstreamer1.0-plugins-good \\\n"
                "  gstreamer1.0-plugins-bad gstreamer1.0-libav\n"
                "./neolink --version\n./neolink rtsp --config=neolink.toml\n```\n\n"
            )
        elif "windows" in target:
            text += (
                "Keep the complete extracted directory together. DLLs, plugins and their\n"
                "license notices are included alongside the executable. No SDK installation\n"
                "is required to run it. Windows also needs the Microsoft Visual C++\n"
                "2015–2022 x64 runtime: https://aka.ms/vs/17/release/vc_redist.x64.exe\n\n"
                "In PowerShell:\n\n"
                "```powershell\n.\\bin\\neolink.exe --version\n"
                ".\\bin\\neolink.exe rtsp --config=neolink.toml\n```\n\n"
                "GStreamer distribution and corresponding sources: https://gstreamer.freedesktop.org/\n\n"
            )
        else:
            text += (
                "Install the runtime with Homebrew (its gstreamer formula includes RTSP\n"
                "server support and the codec plugins):\n\n"
                "```sh\nbrew install gstreamer openssl@3\n"
                "./neolink --version\n./neolink rtsp --config=neolink.toml\n```\n\n"
                "This test executable is unsigned and is not notarized.\n\n"
            )
        text += "Copy `sample_config.toml` to `neolink.toml` and configure your cameras first.\n\n"
    text += (
        "To build the matching source, install Rust and the native development dependencies\n"
        "described in the repository README, then set the build identity explicitly:\n\n"
        f"```sh\nNEOLINK_BUILD_COMMIT={commit} cargo build --release --locked\n```\n\n"
        "On Windows, set `$env:NEOLINK_BUILD_COMMIT` to the same commit in PowerShell\n"
        "before running `cargo build --release --locked`. Cargo.toml retains the project's\n"
        "development version; the test build identity is the commit above.\n"
    )
    return text


def write_documents(directory, info, target=None):
    name = info["short_commit"]
    (directory / f"TEST-RELEASE-{name}.md").write_text(
        build_document(info, target), encoding="utf-8"
    )
    (directory / f"BUILD-INFO-{name}.json").write_text(
        json.dumps(info, indent=2) + "\n", encoding="utf-8"
    )


def copy_windows_runtime(package, runtime):
    runtime = runtime.resolve()
    required = [runtime / "lib/gstreamer-1.0", runtime / "share/licenses"]
    for directory in required:
        if not directory.is_dir():
            raise ValueError(f"GStreamer runtime directory is missing: {directory}")
    shutil.copytree(runtime / "share/licenses", package / "share/licenses")
    plugins = list((runtime / "lib/gstreamer-1.0").glob("*.dll"))
    if not plugins:
        raise ValueError("No GStreamer runtime plugins found")
    plugin_destination = package / "lib/gstreamer-1.0"
    plugin_destination.mkdir(parents=True)
    for plugin in plugins:
        shutil.copy2(plugin, plugin_destination / plugin.name)
    dlls = list((runtime / "bin").glob("*.dll"))
    if not dlls:
        raise ValueError("No GStreamer runtime DLLs found")
    for dll in dlls:
        shutil.copy2(dll, package / "bin" / dll.name)
    for executable in ("gst-inspect-1.0.exe", "gst-launch-1.0.exe"):
        shutil.copy2(runtime / "bin" / executable, package / "bin" / executable)
    scanner_dir = runtime / "libexec/gstreamer-1.0"
    if scanner_dir.is_dir():
        shutil.copytree(scanner_dir, package / "libexec/gstreamer-1.0")
    else:
        # Some GStreamer distributions keep the scanner next to the DLLs.
        shutil.copy2(runtime / "bin/gst-plugin-scanner.exe", package / "bin/gst-plugin-scanner.exe")
    for relative in ("share/gstreamer-1.0", "etc/fonts"):
        if (runtime / relative).is_dir():
            shutil.copytree(runtime / relative, package / relative)


def verify_package(archive, info, target):
    """Test the extracted download; Windows must work without the installed SDK."""
    with tempfile.TemporaryDirectory(prefix="neolink-test-extract-", dir=archive.resolve().parent) as temporary:
        extracted = Path(temporary)
        if archive.suffix == ".zip":
            with zipfile.ZipFile(archive) as bundle:
                bundle.extractall(extracted)
        else:
            with tarfile.open(archive) as bundle:
                bundle.extractall(extracted, filter="data")
        package, = extracted.iterdir()
        environment = os.environ.copy()
        windows = "windows" in target
        executable = package / ("bin/neolink.exe" if windows else "neolink")
        if windows:
            for name in list(environment):
                if name.startswith(("GSTREAMER_", "GST_", "PKG_CONFIG")):
                    environment.pop(name)
            system_root = environment.get("SystemRoot", r"C:\Windows")
            environment["PATH"] = os.pathsep.join(
                [str(package / "bin"), str(Path(system_root) / "System32"), system_root]
            )
            plugins = str(package / "lib/gstreamer-1.0")
            environment["GST_PLUGIN_PATH_1_0"] = plugins
            environment["GST_PLUGIN_SYSTEM_PATH_1_0"] = plugins
            scanner = package / "libexec/gstreamer-1.0/gst-plugin-scanner.exe"
            if not scanner.is_file():
                scanner = package / "bin/gst-plugin-scanner.exe"
            environment["GST_PLUGIN_SCANNER_1_0"] = str(scanner)
        environment["GST_REGISTRY_1_0"] = str(extracted / "gst-registry.bin")

        def run(*arguments):
            return subprocess.check_output(
                [str(argument) for argument in arguments], cwd=package,
                env=environment, stderr=subprocess.STDOUT, timeout=120,
            ).decode(errors="replace")

        version = run(executable, "--version")
        if info["commit"] not in version or f"test-{info['short_commit']}" not in version:
            raise ValueError(f"The packaged binary has the wrong build identity: {version}")
        if "rtsp" not in run(executable, "--help"):
            raise ValueError("The packaged binary does not expose the RTSP command")
        inspect = package / "bin/gst-inspect-1.0.exe" if windows else "gst-inspect-1.0"
        for element in ("appsrc", "appsink", "h264parse", "h265parse", "rtph264pay", "rtph265pay", "decodebin"):
            run(inspect, "--exists", element)
        launch = package / "bin/gst-launch-1.0.exe" if windows else "gst-launch-1.0"
        run(launch, "-q", "videotestsrc", "num-buffers=1", "!", "fakesink")
        print(f"Verified extracted package: {archive.name}")


def package_binary(root, output, info, target, binary, runtime=None, verify=False):
    windows = "windows" in target
    name = f"neolink-test-{info['short_commit']}-{target}"
    with tempfile.TemporaryDirectory(prefix="neolink-test-package-", dir=output.resolve()) as temporary:
        package = Path(temporary) / name
        destination = package / ("bin/neolink.exe" if windows else "neolink")
        destination.parent.mkdir(parents=True)
        shutil.copy2(binary, destination)
        destination.chmod(0o755)
        for filename in ("LICENSE", "sample_config.toml"):
            shutil.copy2(root / filename, package / filename)
        metadata = dict(info, target=target, features=["gstreamer"])
        if windows:
            if not runtime:
                raise ValueError("The Windows package requires a GStreamer runtime")
            copy_windows_runtime(package, runtime)
        write_documents(package, metadata, target)
        archive = output / (name + (".zip" if windows else ".tar.gz"))
        if windows:
            with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
                for path in sorted(package.rglob("*")):
                    if path.is_file():
                        bundle.write(path, path.relative_to(package.parent))
        else:
            with tarfile.open(archive, "w:gz") as bundle:
                def permissions(member):
                    # Windows filesystems do not expose POSIX executable bits.
                    if member.name == f"{name}/neolink":
                        member.mode = 0o755
                    elif member.isdir():
                        member.mode = 0o755
                    return member

                bundle.add(package, arcname=name, filter=permissions)
    if verify:
        verify_package(archive, info, target)
    return archive


def package_source(root, output, info):
    name = f"neolink-test-{info['short_commit']}-source"
    archive = output / f"{name}.tar.gz"
    # git archive excludes build output, ignored files and local untracked files.
    process = subprocess.Popen(
        ["git", "-C", str(root), "archive", "--format=tar", f"--prefix={name}/", info["commit"]],
        stdout=subprocess.PIPE,
    )
    try:
        with tarfile.open(fileobj=process.stdout, mode="r|") as source:
            with tarfile.open(archive, "w:gz") as bundle:
                for member in source:
                    content = source.extractfile(member) if member.isfile() else None
                    bundle.addfile(member, content)
                extras = {
                    f"TEST-RELEASE-{info['short_commit']}.md": build_document(info),
                    f"BUILD-INFO-{info['short_commit']}.json": json.dumps(info, indent=2) + "\n",
                }
                for filename, text in extras.items():
                    data = text.encode("utf-8")
                    member = tarfile.TarInfo(f"{name}/{filename}")
                    member.size = len(data)
                    member.mode = 0o644
                    member.mtime = info["commit_timestamp"]
                    bundle.addfile(member, io.BytesIO(data))
    finally:
        process.stdout.close()
        status = process.wait()
    if status:
        raise RuntimeError(f"git archive failed with exit code {status}")
    return archive


def release_notes(output, info, image, digest):
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise ValueError("Expected a Docker image manifest digest")
    expected = f"ghcr.io/{info['repository'].lower()}:test-{info['short_commit']}"
    if image != expected:
        raise ValueError("The Docker image tag does not match the release commit")
    prefix = f"neolink-test-{info['short_commit']}"
    required = [f"{prefix}-source.tar.gz"]
    required.extend(
        f"{prefix}-{target}{'.zip' if 'windows' in target else '.tar.gz'}"
        for target in TARGETS
    )
    missing = [filename for filename in required if not (output / filename).is_file()]
    if missing:
        raise ValueError(f"Required release downloads are missing: {', '.join(missing)}")
    immutable = f"{image.rsplit(':', 1)[0]}@{digest}"
    receipt = output / f"neolink-test-{info['short_commit']}-docker-image.txt"
    receipt.write_text(
        f"Neolink test image\nSource commit: {info['commit']}\n"
        f"Tag: {image}\nDigest: {digest}\nPlatforms: linux/amd64, linux/arm64\n"
        f"Pull: docker pull {immutable}\n", encoding="utf-8",
    )
    assets = sorted(path.name for path in output.iterdir() if path.is_file())
    text = build_document(info) + "\n## Downloads\n\n"
    text += "\n".join(f"- `{filename}`" for filename in assets)
    text += (
        "\n\nEach binary archive includes runtime instructions, a sample configuration,\n"
        "the license and commit provenance. The source archive contains the complete\n"
        "committed tree plus generated test-release provenance documents.\n\n"
        "## Docker\n\n"
        f"Tag: `{image}`\n\nManifest digest: `{digest}`\n\n"
        "Platforms: `linux/amd64`, `linux/arm64`. Pull the exact published image:\n\n"
        f"```sh\ndocker pull {immutable}\n"
        "docker run --rm --network host \\\n"
        "  -v \"$PWD/neolink.toml:/etc/neolink.toml:ro\" \\\n"
        f"  {immutable}\n```\n\n"
        "The image records its source commit in the OCI revision label and\n"
        "`/usr/share/neolink/BUILD-INFO.txt`. This workflow publishes only a\n"
        "commit-specific test image tag.\n"
    )
    (output / f"TEST-RELEASE-{info['short_commit']}.md").write_text(text, encoding="utf-8")
    checksums = []
    checksum_name = f"SHA256SUMS-test-{info['short_commit']}.txt"
    for path in sorted(output.iterdir()):
        if path.is_file() and path.name != checksum_name:
            with path.open("rb") as stream:
                digest_value = hashlib.file_digest(stream, "sha256").hexdigest()
            checksums.append(f"{digest_value}  {path.name}\n")
    (output / checksum_name).write_text("".join(checksums), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("package", "source", "notes"))
    parser.add_argument("--commit", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("dist"))
    parser.add_argument("--target", choices=TARGETS)
    parser.add_argument("--binary", type=Path)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--image")
    parser.add_argument("--digest")
    args = parser.parse_args()
    info = identity(args.root, args.commit, args.repository)
    args.output.mkdir(parents=True, exist_ok=True)
    if args.command == "package":
        if not args.target:
            parser.error("package requires --target")
        windows = "windows" in args.target
        binary = args.binary or args.root / f"target/{args.target}/release/neolink{'.exe' if windows else ''}"
        runtime = args.runtime
        if windows and not runtime:
            runtime = Path(os.environ["GSTREAMER_1_0_ROOT_MSVC_X86_64"])
        print(package_binary(args.root, args.output, info, args.target, binary, runtime, args.verify))
    elif args.command == "source":
        print(package_source(args.root, args.output, info))
    else:
        if not args.image or not args.digest:
            parser.error("notes requires --image and --digest")
        release_notes(args.output, info, args.image, args.digest)


if __name__ == "__main__":
    main()
