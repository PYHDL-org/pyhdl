---
layout: default
title: Usage
---

# PYHDL Usage Guide

Learn how to use PYHDL to convert Python-like code to VHDL.

## Command Line Interface

### Basic Syntax

```bash
pyhdl <input_file> [output_file] [options]
```

### Arguments

- `input_file` - Input Python file to convert (required)
- `output_file` - Output VHDL file (optional, defaults to `out.vhd`)
- `--verbose, -v` - Enable verbose output

### Examples

```bash
# Basic conversion
pyhdl design.py design.vhd

# Output to default file (out.vhd)
pyhdl design.py

# Verbose mode for debugging
pyhdl design.py design.vhd --verbose

# Short verbose flag
pyhdl design.py design.vhd -v
```

## Input Language Features

### 1. Entity Definitions

Define hardware entities with ports:

```python
entity MyEntity(
    clock: std_logic, 
    reset: std_logic, 
    data: std_logic_vector(7 downto 0)
) -> result: std_logic_vector(7 downto 0):
    # Implementation
```

**Converts to:**
```vhdl
entity MyEntity is
    port(
        clock: in std_logic;
        reset: in std_logic;
        data: in std_logic_vector(7 downto 0);
        result: out std_logic_vector(7 downto 0)
    );
end entity MyEntity;
```

### 2. Process Statements

Sequential logic in processes:

```python
process main(clock, reset):
    if reset = '1':
        counter <= X"0000"
    elif rising_edge(clock):
        if enable = '1':
            counter <= counter + 1
        end if
    end if
```

### 3. Conditional Statements

```python
if signal = '1':
    output <= input_a
elif signal = '0':
    output <= input_b
else:
    output <= (others => '0')
```

### 4. For Loops

```python
for i in range(0, 8):
    parallel_out(i) <= serial_in when shift_enable = '1' else parallel_out(i)
end loop
```

### 5. While Loops

```python
while condition:
    result <= result + 1
end loop
```

### 6. Functions

```python
function add_vectors(
    a: std_logic_vector(7 downto 0), 
    b: std_logic_vector(7 downto 0)
) -> std_logic_vector(7 downto 0):
    return a + b
```

## Complete Examples

### Example 1: Simple Counter

**Input (counter.py):**
```python
entity Counter(
    clock: std_logic, 
    reset: std_logic, 
    enable: std_logic
) -> count: std_logic_vector(7 downto 0):
    
    process counter_proc(clock, reset):
        if reset = '1':
            count <= X"00"
        elif rising_edge(clock):
            if enable = '1':
                count <= count + 1
            end if
        end if
    end process
```

**Command:**
```bash
pyhdl counter.py counter.vhd
```

**Output (counter.vhd):**
```vhdl
entity Counter is
    port(
        clock: in std_logic;
        reset: in std_logic;
        enable: in std_logic;
        count: out std_logic_vector(7 downto 0)
    );
end entity Counter;

architecture CounterArch of Counter is
begin
    process counter_proc(clock, reset) is
    begin
        if reset = '1' then
            count <= X"00";
        elsif rising_edge(clock) then
            if enable = '1' then
                count <= count + 1;
            end if;
        end if;
    end process;
end architecture CounterArch;
```

### Example 2: Multiplexer

**Input (mux.py):**
```python
entity Mux(
    select_signal: std_logic_vector(1 downto 0),
    input_a: std_logic,
    input_b: std_logic,
    input_c: std_logic,
    input_d: std_logic
) -> output: std_logic:
    
    process mux_process(select_signal, input_a, input_b, input_c, input_d):
        if select_signal = "00":
            output <= input_a
        elif select_signal = "01":
            output <= input_b
        elif select_signal = "10":
            output <= input_c
        else:
            output <= input_d
        end if
    end process
```

**Output:** Clean VHDL code with proper entity and architecture.

### Example 3: Shift Register

**Input (shift.py):**
```python
entity ShiftRegister(
    clock: std_logic,
    shift_in: std_logic,
    parallel_load: std_logic_vector(7 downto 0),
    load_enable: std_logic
) -> shift_out: std_logic:
    
    process shift_process(clock):
        if rising_edge(clock):
            if load_enable = '1':
                internal <= parallel_load
            else:
                internal <= internal(6 downto 0) & shift_in
            end if
        end if
    end process
    
    shift_out <= internal(7)
```

## Best Practices

### 1. Use Clear Indentation

Always use 4 spaces for indentation:

```python
# Good
if condition:
    signal <= value
    if nested:
        nested_signal <= other_value

# Bad (mixed spaces)
if condition:
  signal <= value  # Wrong indentation
```

### 2. Name Conventions

Use descriptive names:

```python
# Good
entity DataProcessing(
    input_data: std_logic_vector(7 downto 0)
) -> processed_data: std_logic_vector(7 downto 0):

# Bad
entity MyThing(
    in: std_logic  # 'in' is a reserved word
) -> out: std_logic:  # 'out' is a reserved word
```

### 3. Type Annotations

Always specify port types:

```python
# Good
entity Test(a: std_logic, b: std_logic_vector(3 downto 0)) -> c: std_logic:

# Bad
entity Test(a, b) -> c:  # Missing types
```

### 4. Logical Structure

Organize code logically:

```python
entity ComplexDesign(...) -> ...:
    # Constant declarations
    
    # Process definitions
    
    # Helper functions
```

## Advanced Usage

### Verbose Mode

Use verbose mode to debug conversion issues:

```bash
pyhdl design.py design.vhd --verbose
```

This shows:
- Line processing progress
- Block recognition
- Transformation details
- Error locations

### Large Files

For large designs, consider splitting into modules:

```python
# main.py
entity Top(...) -> ...:
    import submodule
    # Use components
```

## Troubleshooting

### Common Errors

1. **Missing colons**: Every control structure needs a colon
```python
# Wrong
if condition
    code

# Correct
if condition:
    code
```

2. **Incorrect indentation**: Use consistent spacing
```python
# Wrong
if condition:
signal <= value  # Not indented properly

# Correct
if condition:
    signal <= value
```

3. **Reserved words**: Avoid VHDL reserved words
```python
# Wrong
entity Test(in: std_logic) -> out: std_logic:

# Correct
entity Test(input_signal: std_logic) -> output_signal: std_logic:
```

### Getting Help

Run with `--help` for command usage:

```bash
pyhdl --help
```

For more examples, see the examples directory in the repository.

