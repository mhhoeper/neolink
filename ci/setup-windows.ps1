$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

if (-not $env:GITHUB_WORKSPACE -or -not $env:RUST_VERSION -or -not $env:GSTREAMER_VERSION) {
    throw 'Run this script in GitHub Actions with RUST_VERSION and GSTREAMER_VERSION set.'
}

# GitHub Windows runners have PowerShell and Visual Studio Build Tools.
$toolsDir = Join-Path $env:GITHUB_WORKSPACE '.ci-tools'
New-Item -ItemType Directory -Force -Path $toolsDir | Out-Null
$env:PATH = "$(Join-Path $env:CARGO_HOME 'bin');$env:PATH"
$env:RUSTUP_TOOLCHAIN = "$($env:RUST_VERSION)-x86_64-pc-windows-msvc"

if (-not (Get-Command rustup -ErrorAction SilentlyContinue)) {
    $installer = Join-Path $toolsDir 'rustup-init.exe'
    Invoke-WebRequest -UseBasicParsing -Uri 'https://win.rustup.rs/x86_64' -OutFile $installer
    & $installer -y --profile minimal --default-toolchain $env:RUSTUP_TOOLCHAIN --no-modify-path
    if ($LASTEXITCODE -ne 0) { throw 'Rust installation failed.' }
} else {
    & rustup toolchain install $env:RUSTUP_TOOLCHAIN --profile minimal --no-self-update
    if ($LASTEXITCODE -ne 0) { throw 'Rust toolchain installation failed.' }
}

# A self-managed runner can supply an existing MSVC x64 installation.
$gstRoot = $env:GSTREAMER_1_0_ROOT_MSVC_X86_64
if (-not $gstRoot) { $gstRoot = 'C:\gstreamer\1.0\msvc_x86_64' }
$pkgConfig = Join-Path $gstRoot 'bin\pkg-config.exe'

if (-not (Test-Path -LiteralPath $pkgConfig)) {
    # 1.26 uses MSI installers. Newer 1.28 installers use a different format.
    $baseUrl = "https://gstreamer.freedesktop.org/data/pkg/windows/$env:GSTREAMER_VERSION/msvc"
    foreach ($name in @('gstreamer-1.0-msvc-x86_64', 'gstreamer-1.0-devel-msvc-x86_64')) {
        $msi = Join-Path $toolsDir "$name-$env:GSTREAMER_VERSION.msi"
        $log = Join-Path $toolsDir "$name-install.log"
        Invoke-WebRequest -UseBasicParsing -Uri "$baseUrl/$name-$env:GSTREAMER_VERSION.msi" -OutFile $msi
        $process = Start-Process -FilePath 'msiexec.exe' -ArgumentList @(
            '/i', "`"$msi`"", '/qn', '/norestart', 'ADDLOCAL=ALL', '/l*v', "`"$log`""
        ) -Wait -PassThru -WindowStyle Hidden
        if ($process.ExitCode -notin @(0, 3010)) {
            Get-Content -LiteralPath $log -Tail 50
            throw "GStreamer installation failed with exit code $($process.ExitCode)."
        }
    }
    # The installers use this location by default.
    $gstRoot = 'C:\gstreamer\1.0\msvc_x86_64'
    $pkgConfig = Join-Path $gstRoot 'bin\pkg-config.exe'
}

if (-not (Test-Path -LiteralPath $pkgConfig)) {
    throw "GStreamer pkg-config was not installed at $pkgConfig."
}
$env:GSTREAMER_1_0_ROOT_MSVC_X86_64 = $gstRoot
$env:GSTREAMER_1_0_ROOT_X86_64 = $gstRoot
$env:PKG_CONFIG = $pkgConfig
$env:PKG_CONFIG_PATH = Join-Path $gstRoot 'lib\pkgconfig'
$env:PATH = "$(Join-Path $gstRoot 'bin');$env:PATH"
& $pkgConfig --atleast-version=1.20 gstreamer-1.0 gstreamer-rtsp-server-1.0
if ($LASTEXITCODE -ne 0) { throw 'GStreamer >= 1.20 with RTSP server development libraries is required.' }
