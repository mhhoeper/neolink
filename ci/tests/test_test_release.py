"""Exercise committed source contents, download layouts and release provenance."""

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest
from unittest.mock import patch
import zipfile


spec = importlib.util.spec_from_file_location("test_release", Path(__file__).parents[1] / "test_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleasePackagingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="neolink-release-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.output = self.root / "dist"
        self.output.mkdir()
        self.git("init", "--quiet")
        self.git("config", "user.name", "Release Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "core.autocrlf", "false")
        for filename, contents in {
            "LICENSE": "test license\n",
            "sample_config.toml": "bind = '0.0.0.0'\n",
            "tracked.sh": "#!/bin/sh\necho committed\n",
            ".gitignore": "dist/\nsecret.txt\n",
        }.items():
            (self.root / filename).write_bytes(contents.encode("utf-8"))
        self.git("add", ".")
        self.git("update-index", "--chmod=+x", "tracked.sh")
        self.git("-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Source fixture")
        self.commit = self.git("rev-parse", "HEAD").strip()
        self.info = release.identity(self.root, self.commit, "example/neolink")
        self.binary = self.root / "binary"
        self.binary.write_bytes(b"fake executable")

    def git(self, *arguments):
        return subprocess.check_output(["git", "-C", str(self.root), *arguments]).decode()

    def test_source_contains_committed_tree_and_provenance(self):
        (self.root / "tracked.sh").write_text("dirty working tree", encoding="utf-8")
        (self.root / "secret.txt").write_text("ignored secret", encoding="utf-8")
        (self.root / "untracked.txt").write_text("untracked secret", encoding="utf-8")
        archive = release.package_source(self.root, self.output, self.info)
        self.assertIn(self.commit[:12], archive.name)
        with tarfile.open(archive) as bundle:
            prefix = f"neolink-test-{self.commit[:12]}-source/"
            names = bundle.getnames()
            self.assertNotIn(prefix + "secret.txt", names)
            self.assertNotIn(prefix + "untracked.txt", names)
            self.assertFalse(any("/dist/" in name or "/.git/" in name for name in names))
            self.assertEqual(bundle.extractfile(prefix + "tracked.sh").read(), b"#!/bin/sh\necho committed\n")
            self.assertEqual(bundle.getmember(prefix + "tracked.sh").mode & 0o111, 0o111)
            metadata = json.load(bundle.extractfile(prefix + f"BUILD-INFO-{self.commit[:12]}.json"))
            self.assertEqual(metadata["commit"], self.commit)
            documentation = bundle.extractfile(prefix + f"TEST-RELEASE-{self.commit[:12]}.md").read().decode()
            self.assertIn(self.commit, documentation)

    def test_wrong_commit_and_invalid_repository_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "checkout"):
            release.identity(self.root, "a" * 40, "example/neolink")
        with self.assertRaisesRegex(ValueError, "full"):
            release.identity(self.root, self.commit[:12], "example/neolink")
        with self.assertRaisesRegex(ValueError, "repository"):
            release.identity(self.root, self.commit, "../../outside")

    def test_linux_download_has_executable_and_commit_documents(self):
        archive = release.package_binary(
            self.root, self.output, self.info, "aarch64-unknown-linux-gnu", self.binary
        )
        with tarfile.open(archive) as bundle:
            prefix = archive.name.removesuffix(".tar.gz") + "/"
            self.assertEqual(bundle.getmember(prefix + "neolink").mode & 0o111, 0o111)
            self.assertIn(prefix + "sample_config.toml", bundle.getnames())
            document = bundle.extractfile(prefix + f"TEST-RELEASE-{self.commit[:12]}.md").read().decode()
            self.assertIn(self.commit, document)
            self.assertIn("glibc >= 2.39", document)

    def make_runtime(self):
        runtime = self.root / "sdk"
        for filename in (
            "bin/gstreamer-1.0-0.dll", "bin/gst-inspect-1.0.exe", "bin/gst-launch-1.0.exe",
            "lib/gstreamer-1.0/gstcoreelements.dll", "lib/gstreamer-1.0/libgstcoreelements.a",
            "libexec/gstreamer-1.0/gst-plugin-scanner.exe",
            "share/licenses/gstreamer-1.0/COPYING",
        ):
            path = runtime / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"runtime fixture")
        return runtime

    def test_windows_download_contains_runtime_and_licenses(self):
        archive = release.package_binary(
            self.root, self.output, self.info, "x86_64-pc-windows-msvc", self.binary, self.make_runtime()
        )
        with zipfile.ZipFile(archive) as bundle:
            prefix = archive.stem + "/"
            self.assertIn(prefix + "bin/neolink.exe", bundle.namelist())
            self.assertIn(prefix + "bin/gstreamer-1.0-0.dll", bundle.namelist())
            self.assertIn(prefix + "lib/gstreamer-1.0/gstcoreelements.dll", bundle.namelist())
            self.assertNotIn(prefix + "lib/gstreamer-1.0/libgstcoreelements.a", bundle.namelist())
            self.assertIn(prefix + "share/licenses/gstreamer-1.0/COPYING", bundle.namelist())

    def test_windows_smoke_test_isolated_from_installed_sdk(self):
        archive = release.package_binary(
            self.root, self.output, self.info, "x86_64-pc-windows-msvc", self.binary, self.make_runtime()
        )

        def run(arguments, **kwargs):
            environment = kwargs["env"]
            self.assertNotIn("GSTREAMER_1_0_ROOT_MSVC_X86_64", environment)
            self.assertNotIn("installed-sdk", environment["PATH"])
            self.assertIn("neolink-test-extract-", environment["GST_PLUGIN_SYSTEM_PATH_1_0"])
            if "--version" in arguments:
                return f"test-{self.commit[:12]} (commit: {self.commit})".encode()
            if "--help" in arguments:
                return b"commands: rtsp"
            return b""

        with patch.dict(os.environ, {"GSTREAMER_1_0_ROOT_MSVC_X86_64": "installed-sdk"}):
            with patch.object(release.subprocess, "check_output", side_effect=run) as calls:
                release.verify_package(archive, self.info, "x86_64-pc-windows-msvc")
                self.assertEqual(calls.call_count, 10)

    def test_smoke_test_rejects_wrong_binary_identity(self):
        archive = release.package_binary(
            self.root, self.output, self.info, "x86_64-unknown-linux-gnu", self.binary
        )
        with patch.object(release.subprocess, "check_output", return_value=b"old version"):
            with self.assertRaisesRegex(ValueError, "wrong build identity"):
                release.verify_package(archive, self.info, "x86_64-unknown-linux-gnu")

    def test_release_receipt_and_checksums_cover_all_downloads(self):
        prefix = f"neolink-test-{self.commit[:12]}"
        (self.output / f"{prefix}-source.tar.gz").write_bytes(b"source asset")
        for target in release.TARGETS:
            suffix = ".zip" if "windows" in target else ".tar.gz"
            (self.output / f"{prefix}-{target}{suffix}").write_bytes(b"binary asset")
        image = f"ghcr.io/example/neolink:test-{self.commit[:12]}"
        digest = "sha256:" + "a" * 64
        release.release_notes(self.output, self.info, image, digest)
        notes = (self.output / f"TEST-RELEASE-{self.commit[:12]}.md").read_text(encoding="utf-8")
        self.assertIn(self.commit, notes)
        self.assertIn(digest, notes)
        checksum_file = self.output / f"SHA256SUMS-test-{self.commit[:12]}.txt"
        entries = checksum_file.read_text().splitlines()
        self.assertEqual(len(entries), 7)
        for entry in entries:
            expected, filename = entry.split("  ")
            self.assertEqual(expected, hashlib.sha256((self.output / filename).read_bytes()).hexdigest())
        with self.assertRaisesRegex(ValueError, "tag"):
            release.release_notes(self.output, self.info, "ghcr.io/example/neolink:latest", digest)
        with self.assertRaisesRegex(ValueError, "digest"):
            release.release_notes(self.output, self.info, image, "invalid")

    def test_incomplete_download_set_is_not_published(self):
        image = f"ghcr.io/example/neolink:test-{self.commit[:12]}"
        with self.assertRaisesRegex(ValueError, "downloads are missing"):
            release.release_notes(self.output, self.info, image, "sha256:" + "a" * 64)
        self.assertEqual(list(self.output.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
