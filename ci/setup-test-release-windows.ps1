param([string]$Version = '1.28.8')

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
if ($Version -ne '1.28.8') {
    throw 'Update the pinned installer SHA-256 before changing the GStreamer version.'
}
$gstRoot = Join-Path $env:RUNNER_TEMP 'gstreamer'
$downloadBase = "https://gstreamer.freedesktop.org/data/pkg/windows/$Version/msvc"

$installerName = "gstreamer-1.0-msvc-x86_64-$Version.exe"
$installerPath = Join-Path $env:RUNNER_TEMP $installerName
Invoke-WebRequest -Uri "$downloadBase/$installerName" -OutFile $installerPath
$expectedHash = 'e4c41ee6ee9c6c32a45d198463ec08d79bac3bd5fa58adc93d13fe4a08abc9d9'
if ((Get-FileHash -LiteralPath $installerPath -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expectedHash) {
    throw 'The GStreamer installer SHA-256 does not match the pinned distribution.'
}
$arguments = @('/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-', '/portable=1',
    '/TYPE=devel', "/DIR=`"$gstRoot`"")
$process = Start-Process -FilePath $installerPath -ArgumentList $arguments `
    -Wait -PassThru -WindowStyle Hidden
if ($process.ExitCode -ne 0) {
    throw "GStreamer installer failed with exit code $($process.ExitCode)"
}

$pkgConfig = Join-Path $gstRoot 'bin/pkg-config.exe'
if (-not (Test-Path -LiteralPath $pkgConfig)) {
    throw "GStreamer SDK is missing at $gstRoot"
}
@(
    "GSTREAMER_1_0_ROOT_MSVC_X86_64=$gstRoot"
    "GSTREAMER_1_0_ROOT_X86_64=$gstRoot"
    "PKG_CONFIG=$pkgConfig"
    "PKG_CONFIG_PATH=$(Join-Path $gstRoot 'lib/pkgconfig')"
) | Out-File -FilePath $env:GITHUB_ENV -Encoding utf8 -Append
Join-Path $gstRoot 'bin' | Out-File -FilePath $env:GITHUB_PATH -Encoding utf8 -Append
