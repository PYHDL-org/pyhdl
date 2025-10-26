---
layout: default
title: Home
---

# PYHDL

**Python to VHDL Converter**

Translate Python-like syntax to VHDL hardware description language code.

## Quick Start

```bash
# Build the .deb package
chmod +x build_deb.sh
./build_deb.sh

# Install
sudo dpkg -i pyhdl_0.1.0-1_amd64.deb

# Use
pyhdl input.py output.vhd
```

## What is PYHDL?

PYHDL is a powerful tool that converts Python-inspired syntax to VHDL hardware description language code. This allows developers to write hardware designs using familiar Python syntax and convert them to industry-standard VHDL.

### Features

- 🐍 **Python-like Syntax** - Write hardware designs using familiar Python syntax
- 🔄 **Automatic Conversion** - Seamlessly converts Python code to VHDL
- 📦 **Easy Installation** - Available as a Debian package (.deb)
- 🔧 **Command-Line Interface** - Simple and intuitive CLI
- 📝 **Full VHDL Support** - Generates complete, valid VHDL code

## Why PYHDL?

Traditionally, hardware design using VHDL requires learning a specialized language with unique syntax. PYHDL bridges this gap by allowing developers to use Python-like syntax that is automatically converted to VHDL.

### Use Cases

- **Educational** - Learn hardware design concepts using familiar Python syntax
- **Rapid Prototyping** - Quickly prototype hardware designs
- **Code Translation** - Convert Python designs to VHDL for production use
- **Hardware Development** - Accelerate hardware development workflows

## Getting Started

Get started with PYHDL in minutes:

1. [Install PYHDL](getting-started.html#installation)
2. [Learn the syntax](getting-started.html#syntax-basics)
3. [Read the documentation](api-reference.html)

## Example

**Input (Python-like syntax):**
```python
entity MyCounter(clock: std_logic, reset: std_logic) -> value: std_logic_vector(7 downto 0):
    if reset = '1':
        value <= "00000000"
    elif rising_edge(clock):
        value <= value + 1
```

**Output (VHDL):**
```vhdl
entity MyCounter is
    port(
        clock: in std_logic;
        reset: in std_logic;
        value: out std_logic_vector(7 downto 0)
    );
end entity MyCounter;

architecture MyCounterArch of MyCounter is
begin
    if reset = '1' then
        value <= "00000000";
    elsif rising_edge(clock) then
        value <= value + 1;
    end if;
end architecture MyCounterArch;
```

## Community

- 📖 [Documentation](getting-started.html) - Complete documentation
- 💬 [Issues](https://github.com/pyhdl/pyhdl/issues) - Report bugs or request features
- 🤝 [Contributing](https://github.com/pyhdl/pyhdl) - Contribute to PYHDL

## License

MIT License - Free and open source

