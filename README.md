# PYHDL

PYHDL is a Python to VHDL converter that translates Python-like syntax to VHDL hardware description language code.

## Features

- Convert Python-like syntax to VHDL
- Support for entities, processes, functions, loops, and conditionals
- Command-line interface

## Installation

### Build .deb Package

To build a Debian package (.deb file):

1. **On Linux (WSL/Ubuntu/Debian):**
   ```bash
   chmod +x build_deb.sh
   ./build_deb.sh
   ```

2. **Install the package:**
   ```bash
   sudo dpkg -i pyhdl_0.1.0-1_amd64.deb
   ```

3. **Fix any dependencies:**
   ```bash
   sudo apt-get install -f
   ```

### Alternative: Using Makefile

On Linux:
```bash
make deb
sudo make install
```

## Usage

```bash
pyhdl input.py output.vhd [--verbose]
```

### Arguments

- `input` - Input Python-like file
- `output` - Output VHDL file (default: out.vhd)
- `--verbose, -v` - Enable verbose output

### Example

```bash
pyhdl mydesign.py mydesign.vhd
```

## Requirements

- Python 3.7 or higher
- Debian/Ubuntu system (for .deb packaging)

## Development

Install for development:
```bash
python3 setup.py install
```

## License

Apache 2.0 License

## Author

PYHDL Team
