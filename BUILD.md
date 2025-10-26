# Building PYHDL .deb Package

This guide explains how to build a Debian package (.deb file) for PYHDL.

## Prerequisites

- Python 3.7 or higher
- dpkg-deb tool (comes with Debian/Ubuntu systems)
- Make (optional, for using Makefile)

## Quick Start

### On Linux/Ubuntu/WSL:

```bash
# Using the build script
chmod +x build_deb.sh
./build_deb.sh

# Or using Makefile
make deb
```

### On Windows:

#### Using WSL (Recommended)

1. Install WSL if not already installed
2. Run the PowerShell script:
   ```powershell
   .\build_deb.ps1
   ```

#### Using Docker (Alternative)

```bash
docker run -it --rm -v "$(pwd):/workspace" -w /workspace debian:stable bash
apt-get update && apt-get install -y dpkg-dev
chmod +x build_deb.sh
./build_deb.sh
```

## Manual Build Process

If you want to understand the build process:

1. **Clean build directories**
   ```bash
   rm -rf build dist *.egg-info deb_package
   ```

2. **Create package structure**
   ```bash
   mkdir -p deb_package/pyhdl_0.1.0_amd64/usr/lib/python3/dist-packages
   mkdir -p deb_package/pyhdl_0.1.0_amd64/usr/bin
   mkdir -p deb_package/pyhdl_0.1.0_amd64/DEBIAN
   ```

3. **Copy source files**
   ```bash
   cp -r src/* deb_package/pyhdl_0.1.0_amd64/usr/lib/python3/dist-packages/
   ```

4. **Copy DEBIAN control files**
   ```bash
   cp debian/control deb_package/pyhdl_0.1.0_amd64/DEBIAN/
   cp debian/copyright deb_package/pyhdl_0.1.0_amd64/DEBIAN/
   cp debian/postinst deb_package/pyhdl_0.1.0_amd64/DEBIAN/
   chmod +x deb_package/pyhdl_0.1.0_amd64/DEBIAN/postinst
   ```

5. **Create executable link**
   ```bash
   ln -sf /usr/lib/python3/dist-packages/tokenizer.py \
          deb_package/pyhdl_0.1.0_amd64/usr/bin/pyhdl
   ```

6. **Set permissions**
   ```bash
   find deb_package/pyhdl_0.1.0_amd64 -type f -name '*.py' -exec chmod 644 {} \;
   ```

7. **Build the package**
   ```bash
   dpkg-deb --build deb_package/pyhdl_0.1.0_amd64 pyhdl_0.1.0-1_amd64.deb
   ```

## Installing the Package

After building:

```bash
sudo dpkg -i pyhdl_0.1.0-1_amd64.deb
sudo apt-get install -f  # Fix any missing dependencies
```

## Verifying Installation

```bash
pyhdl --help
```

## Troubleshooting

### Permission errors

Make sure to run with appropriate permissions:
```bash
chmod +x build_deb.sh debian/postinst
```

### dpkg-deb not found

Install build tools:
```bash
sudo apt-get update
sudo apt-get install dpkg-dev build-essential
```

### Missing dependencies

When installing the package:
```bash
sudo dpkg -i pyhdl_0.1.0-1_amd64.deb
sudo apt-get install -f
```

## Package Structure

```
deb_package/
└── pyhdl_0.1.0_amd64/
    ├── DEBIAN/
    │   ├── control      # Package metadata
    │   ├── copyright    # License info
    │   └── postinst     # Post-install script
    ├── usr/
    │   ├── bin/
    │   │   └── pyhdl    # Symlink to tokenizer.py
    │   └── lib/
    │       └── python3/
    │           └── dist-packages/
    │               ├── __init__.py
    │               ├── tokenizer.py
    │               └── trans.py
```

