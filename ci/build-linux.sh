#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_SHA:?Run this script in GitHub Actions}"
: "${GITHUB_RUN_ID:?}"
: "${GITHUB_RUN_ATTEMPT:?}"
: "${GITHUB_REPOSITORY:?}"

[[ "$(git rev-parse HEAD)" == "$GITHUB_SHA" ]]
rustc --version
cargo --version
pkg-config --atleast-version=1.20 gstreamer-1.0 gstreamer-rtsp-server-1.0

# Test the application and its core library, including GStreamer support.
cargo test --locked -p neolink -p neolink_core --lib --bins
cargo build --locked -p neolink --bin neolink

package="neolink-nightly-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}-${GITHUB_SHA:0:8}-linux-x86_64-debug"
package_dir="target/nightly/${package}"
mkdir -p "$package_dir" dist
cp target/debug/neolink sample_config.toml LICENSE "$package_dir/"

# Run the packaged binary and retain the startup log containing NEOLINK_VERSION.
version_output="$(RUST_LOG=info "$package_dir/neolink" --version 2>&1)"
printf '%s\n' "$version_output"
if [[ "$version_output" != *"commit: ${GITHUB_SHA}"* ]]; then
    echo "The binary does not report the expected commit" >&2
    exit 1
fi
if [[ "$version_output" != *") debug"* ]]; then
    echo "The binary does not report the debug profile" >&2
    exit 1
fi

cat > "$package_dir/BUILD-INFO.txt" <<EOF
Commit: ${GITHUB_SHA}
Workflow: ${GITHUB_SERVER_URL:-https://github.com}/${GITHUB_REPOSITORY}/actions/runs/${GITHUB_RUN_ID}
Run attempt: ${GITHUB_RUN_ATTEMPT}
Target: x86_64-unknown-linux-gnu
Profile: debug
Build system: Debian 12 (bookworm)
Rust: $(rustc --version)
GStreamer: $(pkg-config --modversion gstreamer-1.0)

${version_output}

Runtime dependencies (Debian 12 / Ubuntu 24.04 or newer):
sudo apt install libgstrtspserver-1.0-0 libgstreamer1.0-0 \\
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good \\
  gstreamer1.0-plugins-bad gstreamer1.0-libav ca-certificates

Copy sample_config.toml to neolink.toml and configure your camera, then run:
./neolink rtsp --config=neolink.toml
EOF

archive="${package}.tar.gz"
tar -czf "dist/$archive" -C "$package_dir" .
(cd dist && sha256sum "$archive" > "$archive.sha256")
