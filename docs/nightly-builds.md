# Nightly test builds on GitHub

The [Nightly test builds workflow](../.github/workflows/nightly.yml) builds
Neolink with its default GStreamer/RTSP features on Linux x86_64 and Windows
x86_64. It runs the application and core library unit tests in the default
debug/test profiles, builds the debug executable, and checks that the startup
log reports the expected full commit ID and debug profile. The source ZIP is
generated from that same commit after both binary jobs have passed.

All downloadable archives and GitHub artifact names include the `-debug`
suffix. The source ZIP belongs to the same debug nightly build. The binary
archives contain executables named `neolink` and `neolink.exe`.

"Nightly" describes the daily schedule. Both builds use stable Rust 1.100.0,
not the Rust nightly channel. Dependencies are resolved from `Cargo.lock`
with `--locked`. `build.rs` continues to generate the version without editing
`Cargo.toml`; the workflow checks out the complete history and tags.
`GITHUB_SHA` is already supported by the build script. The commit ID appears
in the startup log; the CLI's `--version` line itself currently reports the
Cargo package version.

The other workspace applications and the optional `pushnoti` feature are not
part of these builds. The unit tests do not require a camera and do not replace
an end-to-end camera/RTSP test.

## Enable and run

1. Commit the workflow, `ci/` scripts, and documentation, and push them to
   `master` on `https://github.com/mhhoeper/neolink`. Scheduled workflows must
   be present on the repository's default branch.
2. Check **Settings > Actions > General** and enable GitHub Actions if needed.
   The workflow uses GitHub-hosted `ubuntu-24.04` and `windows-2022` runners.
   No additional runner or secret is required. The workflow requests only
   read access to repository contents.
3. Open **Actions > Nightly test builds > Run workflow** and select `master` to
   verify the first run. The three jobs must succeed.

The cron expression `17 1 * * *` runs daily at 01:17 UTC, which is 02:17 in
Berlin during winter and 03:17 during summer. GitHub schedules use UTC; the
minute is deliberately away from the start of the hour, when queues can be
busy. The scheduled run uses the latest commit on the default branch, even
when no new commit was pushed that day. Actual start times can be delayed by
GitHub's scheduler and runner availability.

Pushes and pull requests do not trigger this workflow. The existing Docker
workflows continue to handle their usual push and PR events. For public
repositories, GitHub can disable scheduled workflows after 60 days without
repository activity; they can be re-enabled from the Actions page.

## Build environments

Linux runs in the pinned `rust:1.100.0-bookworm` container on a GitHub Ubuntu
runner. The container installs GStreamer development libraries and the base,
good, bad, ugly, and libav plugins. The ugly/libav encoders also allow the
generated MP4 unit test to run.

Windows uses the MSVC x64 Rust toolchain and the runner's Visual Studio C++
Build Tools, Windows SDK, and CMake. The setup script installs the official
GStreamer 1.26.11 MSVC x64 runtime and development MSI packages with all
features if no existing installation is supplied. This version supports the
project's GStreamer >= 1.20 requirement. Newer 1.28 installers use a different
format; changing `GSTREAMER_VERSION` to 1.28 requires updating the installer
script too. An existing installation can be supplied using
`GSTREAMER_1_0_ROOT_MSVC_X86_64`.

The Windows setup and build run in the same PowerShell step, so the Rust and
GStreamer environment settings remain available to compilation and tests.
Rust dependencies and `target/` are cached separately for the two platforms.
The first build takes longer because it has to compile all dependencies.
Each build job has a 120-minute timeout.

Debug builds include debug symbols, debug assertions, and integer overflow
checks. They are intended for functional testing and diagnosing failures;
their performance can differ from an optimized release build. The Windows
ZIP includes `neolink.pdb` alongside `neolink.exe` so debuggers can load its
symbols. Linux debug symbols are included in the executable.

## Download and run

Open a successful run under **Actions > Nightly test builds** and download
the three entries under **Artifacts**. GitHub requires signing in to download
workflow artifacts. They are retained for 30 days, subject to repository
retention policies.

| Platform | Packaged file inside the artifact |
| --- | --- |
| Linux x86_64 | `neolink-nightly-<run>-<attempt>-<sha>-linux-x86_64-debug.tar.gz` |
| Windows x86_64 | `neolink-nightly-<run>-<attempt>-<sha>-windows-x86_64-debug.zip` |
| Source | `neolink-nightly-<run>-<attempt>-<sha>-source-debug.zip` |

Every archive has a SHA-256 checksum file. The binary archives also contain
`sample_config.toml`, `LICENSE`, and `BUILD-INFO.txt` with the full commit,
workflow URL, debug profile, Rust/GStreamer versions, and runtime instructions.

Linux is built against Debian 12/glibc, suitable for Debian 12 and Ubuntu 24.04
or newer on x86_64. It is not a static musl binary. Install the GStreamer
runtime and plugins listed in `BUILD-INFO.txt` on the destination machine.
Windows requires a separate GStreamer MSVC x64 **Full** runtime installation
with its `bin` directory on `PATH`; DLLs and plugins are not bundled in the
ZIP. Copy `sample_config.toml` to `neolink.toml`, configure the camera, and
start `neolink rtsp --config=neolink.toml`.

The source ZIP uses `git archive`, includes all tracked files such as
`Cargo.lock`, `vendor/`, and `LICENSE`, and excludes `.git`, build outputs,
caches, and untracked local files. Rebuilding the extracted ZIP has no Git
metadata, so `build.rs` falls back to the Cargo version and `unknown commit`.
Use a Git checkout of the recorded commit to reproduce the Git version string.

This workflow creates downloadable test artifacts. GitHub Releases with
permanent downloads can be added separately if needed.

## References

- [Repository actions](https://github.com/mhhoeper/neolink/actions)
- [Scheduled workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)
- [Downloading artifacts](https://docs.github.com/en/actions/managing-workflow-runs/downloading-workflow-artifacts)
- [GStreamer downloads](https://gstreamer.freedesktop.org/download/)
