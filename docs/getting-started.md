---
layout: default
title: Getting Started
---

# Getting Started with PYHDL

Welcome to PYHDL! This guide will help you get up and running with PYHDL in no time.

## Installation

### Requirements

- Python 3.7 or higher
- Linux/Ubuntu/WSL or macOS/Windows with package manager
- dpkg (for Debian package installation)

### Installing from .deb Package

The easiest way to install PYHDL is using the Debian package:

```bash
# Build the package
chmod +x build_deb.sh
./build_deb.sh

# Install
sudo dpkg -i pyhdl_0.1.0-1_amd64.deb

# Fix dependencies (if needed)
sudo apt-get install -f
```

### Installing from Source

```bash
# Clone the repository
git clone https://github.com/pyhdl/pyhdl.git
cd pyhdl

# Install dependencies
python3 -m pip install -r requirements.txt

# Install the package
python3 setup.py install
```

### Verify Installation

Check if PYHDL is installed correctly:

```bash
pyhdl --help
```

You should see the help output with available commands.

## Syntax Basics

PYHDL uses Python-like syntax that gets automatically converted to VHDL. Here are the basics:

### Entity Declaration

Entities define the interface of your hardware:

```python
entity MyComponent(input_a: std_logic, input_b: std_logic) -> output: std_logic:
    # Your logic here
```

### Ports

- **Input ports**: Define with type in the parameter list
- **Output ports**: Define after `->` in the return annotation

### Processes

Processes describe sequential behavior:

```python
process my_process(clock, reset):
    if reset = '1' then:
        counter <= "00000000"
    elif rising_edge(clock):
        counter <= counter + 1
```

### Conditions

Python-like if statements:

```python
if condition:
    result <= '1'
elif condition2:
    result <= '0'
```

### Loops

For loops in VHDL:

```python
for i in range(0, 8):
    temp[i] <= input[i] and mask[i]
```

### Functions

Define reusable functions:

```python
def func add(a: std_logic_vector, b: std_logic_vector) -> std_logic_vector:
    return a + b
```

## Your First Conversion

Let's create a simple example:

1. **Create a file** `example.py`:

```python
entity SimpleCounter(clk: std_logic, reset: std_logic) -> count: std_logic_vector(7 downto 0):
    if reset = '1':
        count <= "00000000"
    elif rising_edge(clk):
        count <= count + 1
```

2. **Convert to VHDL**:

```bash
pyhdl example.py counter.vhd
```

3. **Check the output** in `counter.vhd`

## Common Syntax Elements

### Signal Assignment

Use `<=` for signal assignments (converted from `=` in Python):

```python
signal <= value
```

### Logical Operations

```python
result <= a and b
result <= a or b
result <= not a
```

### Comparisons

```python
if signal = '1':
if signal /= '0':  # not equal
if a < b:
```

### Comments

Python comments are preserved:

```python
# This is a comment
# Comments are kept in VHDL output
```

## Next Steps

- Read the [Usage Guide](usage.html) for detailed conversion examples
- Check the [API Reference](api-reference.html) for all supported features
- Join our community on GitHub

## Troubleshooting

### Installation Issues

If you encounter installation errors:

```bash
# Check Python version
python3 --version

# Should be 3.7+

# Install build tools
sudo apt-get update
sudo apt-get install build-essential dpkg-dev

# Try installing again
python3 setup.py install --force
```

### Conversion Errors

Common errors and solutions:

1. **"Invalid definition level"** - Check indentation (use 4 spaces)
2. **"Expected definition block"** - Ensure colons after control structures
3. **"File not found"** - Check file path and permissions

### Getting Help

- Check the [Usage Guide](usage.html) for examples
- File an issue on [GitHub](https://github.com/pyhdl/pyhdl/issues)
- Read the FAQ section

## Examples

See the [examples directory](https://github.com/pyhdl/pyhdl/tree/main/examples) for more code samples.

