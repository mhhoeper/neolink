$ErrorActionPreference = 'Stop'

if (-not $env:GITHUB_SHA -or -not $env:GITHUB_RUN_ID -or -not $env:GITHUB_RUN_ATTEMPT -or -not $env:GITHUB_REPOSITORY) {
    throw 'Run this script in GitHub Actions.'
}
$headCommit = & git rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $headCommit.Trim() -ne $env:GITHUB_SHA) {
    throw 'The checkout does not match GITHUB_SHA.'
}
& rustc --version
if ($LASTEXITCODE -ne 0) { throw 'Rust is not available.' }
& cargo --version
if ($LASTEXITCODE -ne 0) { throw 'Cargo is not available.' }
& cargo test --locked -p neolink -p neolink_core --lib --bins
if ($LASTEXITCODE -ne 0) { throw 'Unit tests failed.' }
& cargo build --locked -p neolink --bin neolink
if ($LASTEXITCODE -ne 0) { throw 'Debug build failed.' }

$package = "neolink-nightly-$env:GITHUB_RUN_ID-$env:GITHUB_RUN_ATTEMPT-$($env:GITHUB_SHA.Substring(0, 8))-windows-x86_64-debug"
$packageDir = Join-Path 'target\nightly' $package
New-Item -ItemType Directory -Force -Path $packageDir, 'dist' | Out-Null
Copy-Item -LiteralPath 'target\debug\neolink.exe', 'target\debug\neolink.pdb', 'sample_config.toml', 'LICENSE' -Destination $packageDir

# PowerShell 5 treats redirected native stderr as errors. Capture it through
# Start-Process so the informational version log does not fail the job.
$stdoutPath = Join-Path $packageDir 'version-stdout.txt'
$stderrPath = Join-Path $packageDir 'version-stderr.txt'
$env:RUST_LOG = 'info'
$process = Start-Process -FilePath (Join-Path (Resolve-Path $packageDir).Path 'neolink.exe') `
    -ArgumentList '--version' -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath `
    -Wait -PassThru -WindowStyle Hidden
if ($process.ExitCode -ne 0) { throw 'The packaged binary failed its version smoke test.' }
$versionOutput = (Get-Content -LiteralPath $stderrPath, $stdoutPath -Raw) -join "`n"
Write-Host $versionOutput
if (-not $versionOutput.Contains("commit: $env:GITHUB_SHA")) {
    throw 'The binary does not report the expected commit.'
}
if (-not $versionOutput.Contains(') debug')) {
    throw 'The binary does not report the debug profile.'
}
Remove-Item -LiteralPath $stdoutPath, $stderrPath

$rustVersion = & rustc --version
if ($LASTEXITCODE -ne 0) { throw 'Cannot determine the Rust version.' }
$gstVersion = & $env:PKG_CONFIG --modversion gstreamer-1.0
if ($LASTEXITCODE -ne 0) { throw 'Cannot determine the GStreamer version.' }
$server = $env:GITHUB_SERVER_URL
if (-not $server) { $server = 'https://github.com' }
$workflowUrl = "$server/$env:GITHUB_REPOSITORY/actions/runs/$env:GITHUB_RUN_ID"
$buildInfo = @"
Commit: $env:GITHUB_SHA
Workflow: $workflowUrl
Run attempt: $env:GITHUB_RUN_ATTEMPT
Target: x86_64-pc-windows-msvc
Profile: debug
Rust: $rustVersion
GStreamer: $gstVersion

$versionOutput

Runtime dependencies:
Install the GStreamer MSVC x86_64 runtime (Full installation, >= 1.20).
https://gstreamer.freedesktop.org/download/
Add its bin directory to PATH before starting Neolink, for example:
`$env:PATH = 'C:\gstreamer\1.0\msvc_x86_64\bin;' + `$env:PATH

Copy sample_config.toml to neolink.toml and configure your camera, then run:
.\neolink.exe rtsp --config=neolink.toml
"@
$utf8 = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText((Join-Path (Resolve-Path $packageDir).Path 'BUILD-INFO.txt'), $buildInfo, $utf8)

$archive = Join-Path 'dist' "$package.zip"
Compress-Archive -Path "$packageDir\*" -DestinationPath $archive -Force
$hash = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
$checksum = "$hash  $package.zip`n"
[System.IO.File]::WriteAllText("$((Resolve-Path $archive).Path).sha256", $checksum, $utf8)
