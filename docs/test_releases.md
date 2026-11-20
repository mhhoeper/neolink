# Test releases

The **Release Test Binaries** GitHub Actions workflow publishes an experimental
prerelease from a single commit. It does not increment package versions.

## Start a test release

1. Push the workflow and its supporting files to the repository. The workflow
   must exist on the default branch (`master`) before manual dispatch is available.
2. Open **Actions → Release Test Binaries → Run workflow** on GitHub.
3. Select the branch or tag to test, then click **Run workflow**. The commit at
   dispatch time is fixed for every job, even if that branch advances during the build.
4. Wait for the binaries and Docker image to build. The completed prerelease
   appears under **Releases**, named `Test build <12-character commit>`.

GitHub Actions must be enabled. The workflow uses the repository's automatic
`GITHUB_TOKEN`: read access for builds, package write access for GHCR, and content
write access for the final release job. No personal access token is needed.
Linux ARM64 uses the GitHub-hosted `ubuntu-24.04-arm` runner; the repository's
Actions plan must support that runner.

## Published files and image

For a commit abbreviated as `0123456789ab`, the release tag is
`test-0123456789ab`. The downloads are:

| Download | Contents |
|---|---|
| `neolink-test-0123456789ab-x86_64-unknown-linux-gnu.tar.gz` | Linux x64 binary |
| `neolink-test-0123456789ab-aarch64-unknown-linux-gnu.tar.gz` | Linux ARM64 binary |
| `neolink-test-0123456789ab-x86_64-pc-windows-msvc.zip` | Windows x64 binary and GStreamer runtime |
| `neolink-test-0123456789ab-aarch64-apple-darwin.tar.gz` | macOS Apple Silicon binary |
| `neolink-test-0123456789ab-source.tar.gz` | Complete committed source tree and generated provenance |
| `neolink-test-0123456789ab-docker-image.txt` | Docker tag, digest, platforms and source commit |
| `TEST-RELEASE-0123456789ab.md` | Test-release notes and installation information |
| `SHA256SUMS-test-0123456789ab.txt` | SHA-256 checksums of every other download |

Every binary archive contains the sample configuration, license,
`TEST-RELEASE-0123456789ab.md`, and `BUILD-INFO-0123456789ab.json`. The documents
record the **full 40-character commit**, the target and the source location.
The source archive uses `git archive` of that exact commit: ignored files,
untracked files and build output are excluded. The archive preserves the source
tree and adds the two provenance documents at its root. GitHub also provides its
standard source downloads for the release tag.

The matching image is `ghcr.io/<owner>/<repository>:test-0123456789ab`, supporting
`linux/amd64` and `linux/arm64`. Release notes record the manifest digest so you
can pull the exact image using `ghcr.io/<owner>/<repository>@sha256:...`.
The full commit is also stored in the image's OCI revision label and in
`/usr/share/neolink/BUILD-INFO.txt`.

This workflow only publishes the commit-specific Docker test tag. The existing
Docker push workflows continue to handle `dev`, version tags and `latest`.
The test prerelease is explicitly excluded from GitHub's latest-release selection.

## Runtime requirements

- **Linux:** Ubuntu 24.04 or a compatible distribution with glibc 2.39 or newer,
  GStreamer, RTSP server support, and the base/good/bad/libav plugins. Package-specific
  installation commands are included in each download.
- **Windows:** Keep the entire extracted directory together and run
  `bin/neolink.exe`. GStreamer DLLs, plugins, helpers and license notices are bundled.
  The Microsoft Visual C++ 2015–2022 x64 runtime must be installed; obtain it from
  <https://aka.ms/vs/17/release/vc_redist.x64.exe> if needed.
  The CI smoke test removes the installed SDK from the environment and tests the
  extracted download, including a GStreamer pipeline.
- **macOS:** macOS 15 or newer on Apple Silicon, with Homebrew's `gstreamer` and
  `openssl@3` installed. This test executable is unsigned and is not notarized.

All binaries use the default `gstreamer` feature. The optional `pushnoti` feature
is not enabled. Each build checks its commit identity, CLI help, required
GStreamer elements and a small GStreamer pipeline before uploading its archive.
The Dockerfile also checks `neolink --version` in each target image.

## Retry behavior

There is one published test release per commit. Dispatching another complete run
for an already published commit stops before building. Choose a new commit to
publish another test release.

The release job first creates a draft, uploads all downloads, then publishes it
as a prerelease. If upload or publication fails, rerun the failed jobs: an existing
draft can be completed, provided its tag points to the same commit. Published
release assets are not replaced. The Docker image is pushed before the final
release job; it may already be available if that final job fails.

## Build the source download

Install Rust and the platform's native development dependencies, extract the
source archive, then use the full commit recorded in its provenance documents:

```sh
NEOLINK_BUILD_COMMIT=<full-commit> cargo build --release --locked
```

In PowerShell:

```powershell
$env:NEOLINK_BUILD_COMMIT = '<full-commit>'
cargo build --release --locked
```

The executable reports `test-<short-commit> (commit: <full-commit>)`. The package
version in `Cargo.toml` remains the project's development version. Rust and native
dependency versions can change between builds; this workflow records the source
commit and image digest, but does not promise bit-for-bit reproducible binaries.
