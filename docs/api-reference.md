---
layout: default
title: API Reference
---

# API Reference

Complete reference for PYHDL language features and supported constructs.

## Language Elements

### Entity Declaration

Define hardware components with ports.

**Syntax:**
```python
entity EntityName([input_ports]) -> [output_ports]:
    # Implementation
```

**Parameters:**
- `EntityName`: Name of the entity
- `input_ports`: List of `name: type` input port declarations
- `output_ports`: List of `name: type` output port declarations

**Example:**
```python
entity Adder(
    a: std_logic_vector(7 downto 0),
    b: std_logic_vector(7 downto 0)
) -> sum: std_logic_vector(8 downto 0):
    sum <= ('0' & a) + ('0' & b)
```

### Port Types

Supported VHDL types:

- `std_logic` - Single bit
- `std_logic_vector(n downto m)` - Vector of bits
- `integer` - Integer type
- `boolean` - Boolean type

### Process Statements

Define sequential logic processes.

**Syntax:**
```python
process ProcessName([sensitivity_list]):
    # Sequential statements
```

**Example:**
```python
process counter(clock, reset):
    if reset = '1' then:
        value <= X"00"
    elif rising_edge(clock):
        value <= value + 1
    end if
```

### If Statements

Conditional logic support.

**Syntax:**
```python
if condition:
    statements
elif condition:
    statements
else:
    statements
```

**Example:**
```python
if enable = '1':
    result <= input_a
elif select_signal = '0':
    result <= input_b
else:
    result <= (others => 'Z')
```

### For Loops

Iterative statements.

**Syntax:**
```python
for variable in range(start, end):
    statements
```

**Example:**
```python
for i in range(0, 8):
    temp(i) <= data(i) when selector(i) = '1' else temp(i-1)
```

### While Loops

Conditional iteration.

**Syntax:**
```python
while condition:
    statements
```

**Example:**
```python
while count < max_value:
    output <= input
    count <= count + 1
```

### Functions

Reusable function definitions.

**Syntax:**
```python
function FunctionName([parameters]) -> return_type:
    # Function body
    return expression
```

**Example:**
```python
function Multiply(
    a: std_logic_vector(7 downto 0),
    b: std_logic_vector(7 downto 0)
) -> std_logic_vector(15 downto 0):
    return a * b
```

## Operators

### Arithmetic Operators

- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division (limited support)

### Logical Operators

- `and` - Logical AND
- `or` - Logical OR
- `not` - Logical NOT
- `xor` - Exclusive OR

### Comparison Operators

- `=` - Equality
- `/=` - Inequality
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal
- `>=` - Greater than or equal

### Concatenation

- `&` - Concatenation operator

**Example:**
```python
result <= a & b  # Concatenate a and b
```

## Signal Assignments

### Direct Assignment

```python
signal <= value
```

### Conditional Assignment

```python
signal <= value when condition else default_value
```

### Selected Assignment

```python
signal <= value_a when selector = "00" else
          value_b when selector = "01" else
          value_c
```

## Type Conversions

### Literals

```python
# Bit literal
signal <= '0'
signal <= '1'

# Vector literal
signal <= "10101010"  # std_logic_vector
signal <= X"FF"       # Hexadecimal
signal <= O"123"      # Octal
signal <= B"1010"     # Binary

# Integer literal
count <= 42
```

## Reserved Words

Avoid using these Python reserved words:
- `if`, `elif`, `else`
- `for`, `while`, `in`, `range`
- `def`, `return`
- `and`, `or`, `not`, `in`, `is`

Avoid these VHDL reserved words:
- `entity`, `architecture`, `process`
- `signal`, `variable`, `constant`
- `in`, `out`, `inout`, `buffer`
- `std_logic`, `std_logic_vector`

## Conversion Rules

### Basic Transformations

| Python Syntax | VHDL Output |
|--------------|------------|
| `=` (assignment) | `<=` |
| `if condition:` | `if condition then` |
| `elif condition:` | `elsif condition then` |
| `for i in range(x, y):` | `for i in x to y loop` |
| `and/or/not` | `and/or/not` |
| `# comment` | `-- comment` |

### Process Conversion

Python-like process:
```python
process example(clock):
    if condition:
        signal <= value
```

Converts to:
```vhdl
process example(clock) is
begin
    if condition then
        signal <= value;
    end if;
end process;
```

### Entity Conversion

Python syntax:
```python
entity Example(a: std_logic) -> b: std_logic:
    # implementation
```

VHDL output:
```vhdl
entity Example is
    port(
        a: in std_logic;
        b: out std_logic
    );
end entity Example;

architecture ExampleArch of Example is
begin
    -- implementation
end architecture ExampleArch;
```

## Error Handling

### Common Errors

1. **Invalid Indentation**
   - Error: "invalid definition level at line X"
   - Fix: Use consistent 4-space indentation

2. **Missing Colon**
   - Error: "expected definition block after line X"
   - Fix: Add colon after control structures

3. **Reserved Word**
   - Error: Syntax error
   - Fix: Use alternative names

4. **Type Mismatch**
   - Error: Invalid type
   - Fix: Use proper VHDL types

## Debugging Tips

1. Use `--verbose` flag for detailed output
2. Check indentation carefully
3. Verify type annotations
4. Test with simple examples first
5. Compare with generated VHDL

## Examples

See the [Usage Guide](usage.html) for complete working examples.

For more examples, check the repository's examples directory.

