# Makefile for building .deb package

PACKAGE_NAME := pyhdl
VERSION := 0.1.0
DEB_VERSION := 1
PYTHON_VERSION := 3

.PHONY: clean deb build

build:
	@echo "Building Python package..."
	python3 setup.py sdist bdist_wheel
	@echo "Python package built successfully"

deb: clean build
	@echo "Creating Debian package structure..."
	mkdir -p dist/$(PACKAGE_NAME)_$(VERSION)_amd64
	mkdir -p dist/$(PACKAGE_NAME)_$(VERSION)_amd64/usr/bin
	mkdir -p dist/$(PACKAGE_NAME)_$(VERSION)_amd64/usr/lib/python$(PYTHON_VERSION)/dist-packages
	mkdir -p dist/$(PACKAGE_NAME)_$(VERSION)_amd64/DEBIAN
	@echo "Copying files..."
	cp -r src/* dist/$(PACKAGE_NAME)_$(VERSION)_amd64/usr/lib/python$(PYTHON_VERSION)/dist-packages/
	cp debian/control dist/$(PACKAGE_NAME)_$(VERSION)_amd64/DEBIAN/
	cp debian/copyright dist/$(PACKAGE_NAME)_$(VERSION)_amd64/DEBIAN/
	cp debian/postinst dist/$(PACKAGE_NAME)_$(VERSION)_amd64/DEBIAN/
	chmod +x dist/$(PACKAGE_NAME)_$(VERSION)_amd64/DEBIAN/postinst
	@echo "Creating bin symlink..."
	ln -sf /usr/lib/python$(PYTHON_VERSION)/dist-packages/tokenizer.py dist/$(PACKAGE_NAME)_$(VERSION)_amd64/usr/bin/pyhdl
	@echo "Setting permissions..."
	find dist/$(PACKAGE_NAME)_$(VERSION)_amd64 -type f -name '*.py' -exec chmod 644 {} \;
	@echo "Building .deb package..."
	dpkg-deb --build dist/$(PACKAGE_NAME)_$(VERSION)_amd64 dist/$(PACKAGE_NAME)_$(VERSION)-$(DEB_VERSION)_amd64.deb
	@echo "Debian package created: dist/$(PACKAGE_NAME)_$(VERSION)-$(DEB_VERSION)_amd64.deb"

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build dist *.egg-info
	rm -rf dist/$(PACKAGE_NAME)_*
	@echo "Clean complete"

install:
	@echo "Installing $(PACKAGE_NAME)..."
	sudo dpkg -i dist/$(PACKAGE_NAME)_$(VERSION)-$(DEB_VERSION)_amd64.deb

