#!/bin/bash
# Build script for creating .deb package

set -e

PACKAGE_NAME="pyhdl"
VERSION="0.1.0"
DEB_VERSION="1"
PYTHON_VERSION="3"

echo "=== Building PYHDL Debian Package ==="

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.egg-info deb_package

# Create package structure
echo "Creating package structure..."
mkdir -p deb_package/${PACKAGE_NAME}_${VERSION}_amd64
mkdir -p deb_package/${PACKAGE_NAME}_${VERSION}_amd64/usr/bin
mkdir -p deb_package/${PACKAGE_NAME}_${VERSION}_amd64/usr/lib/python${PYTHON_VERSION}/dist-packages
mkdir -p deb_package/${PACKAGE_NAME}_${VERSION}_amd64/DEBIAN

# Copy source files
echo "Copying source files..."
cp -r src/* deb_package/${PACKAGE_NAME}_${VERSION}_amd64/usr/lib/python${PYTHON_VERSION}/dist-packages/

# Copy DEBIAN files
echo "Copying DEBIAN control files..."
cp debian/control deb_package/${PACKAGE_NAME}_${VERSION}_amd64/DEBIAN/
cp debian/copyright deb_package/${PACKAGE_NAME}_${VERSION}_amd64/DEBIAN/
cp debian/postinst deb_package/${PACKAGE_NAME}_${VERSION}_amd64/DEBIAN/
chmod +x deb_package/${PACKAGE_NAME}_${VERSION}_amd64/DEBIAN/postinst

# Set correct permissions for Python files
echo "Setting permissions..."
find deb_package/${PACKAGE_NAME}_${VERSION}_amd64 -type f -name '*.py' -exec chmod 644 {} \;

# Create executable symlink (for Linux)
echo "Creating executable symlink..."
ln -sf /usr/lib/python${PYTHON_VERSION}/dist-packages/tokenizer.py \
       deb_package/${PACKAGE_NAME}_${VERSION}_amd64/usr/bin/pyhdl

# Build .deb package
echo "Building .deb package..."
dpkg-deb --build deb_package/${PACKAGE_NAME}_${VERSION}_amd64 \
           ${PACKAGE_NAME}_${VERSION}-${DEB_VERSION}_amd64.deb

echo ""
echo "=== Build Complete ==="
echo "Package created: ${PACKAGE_NAME}_${VERSION}-${DEB_VERSION}_amd64.deb"
echo ""
echo "To install: sudo dpkg -i ${PACKAGE_NAME}_${VERSION}-${DEB_VERSION}_amd64.deb"
echo "To fix dependencies: sudo apt-get install -f"

