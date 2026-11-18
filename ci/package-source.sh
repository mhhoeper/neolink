#!/usr/bin/env bash
set -euo pipefail

: "${GITHUB_SHA:?Run this script in GitHub Actions}"
: "${GITHUB_RUN_ID:?}"
: "${GITHUB_RUN_ATTEMPT:?}"

[[ "$(git rev-parse HEAD)" == "$GITHUB_SHA" ]]
mkdir -p dist
archive="neolink-nightly-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}-${GITHUB_SHA:0:8}-source-debug.zip"
# Archive only tracked files at the exact commit used by both binary jobs.
# This includes Cargo.lock, the vendored compatibility patch, and LICENSE.
git archive --format=zip --prefix="neolink-${GITHUB_SHA:0:8}/" \
    --output="dist/$archive" "$GITHUB_SHA"
(cd dist && sha256sum "$archive" > "$archive.sha256")
