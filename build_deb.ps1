# PowerShell script to build .deb package (requires WSL or Linux environment)

Write-Host "=== Building PYHDL Debian Package ===" -ForegroundColor Green

$PACKAGE_NAME = "pyhdl"
$VERSION = "0.1.0"
$DEB_VERSION = "1"

# Clean previous builds
Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue build, dist, *.egg-info, deb_package

# Check if WSL is available
$wslAvailable = Get-Command wsl -ErrorAction SilentlyContinue

if ($wslAvailable) {
    Write-Host "Using WSL to build .deb package..." -ForegroundColor Cyan
    
    # Run the bash script in WSL
    wsl bash -c "cd /mnt/c/Users/Public/PYHDL/pyhdl && chmod +x build_deb.sh && ./build_deb.sh"
    
    Write-Host ""
    Write-Host "=== Build Complete ===" -ForegroundColor Green
    Write-Host "Package location: $(pwd)\pyhdl_$VERSION-$DEB_VERSION_amd64.deb"
} else {
    Write-Host ""
    Write-Host "ERROR: WSL (Windows Subsystem for Linux) not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "To build .deb packages on Windows, you need:" -ForegroundColor Yellow
    Write-Host "1. Install WSL: https://docs.microsoft.com/en-us/windows/wsl/install" -ForegroundColor Yellow
    Write-Host "2. Or use a virtual machine with Linux" -ForegroundColor Yellow
    Write-Host "3. Or use a CI/CD service (GitHub Actions, etc.)" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Alternatively, you can package the Python application directly:" -ForegroundColor Cyan
    Write-Host "  python setup.py bdist_wheel" -ForegroundColor White
    Write-Host ""
}

