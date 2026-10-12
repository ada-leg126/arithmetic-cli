# Arithmetic CLI

A simple Python command-line script that performs basic arithmetic operations using the `argparse` module.

## Requirements

- Python 3 or later

## Usage

Run the script from the project directory:

```bash
python arithmetic.py -o <operation> -n1 <first_number> -n2 <second_number>
```

### Arguments

- `-o`, `--operation`: The operation to perform. Supported values are:
  - `add`
  - `sub`
  - `mul`
  - `div`
- `-n1`, `--num1`: The first number.
- `-n2`, `--num2`: The second number.

## Examples

### Addition

```bash
python arithmetic.py -o add -n1 10 -n2 5
```

Output:

```text
15.0
```

### Subtraction

```bash
python arithmetic.py -o sub -n1 10 -n2 5
```

Output:

```text
5.0
```

### Multiplication

```bash
python arithmetic.py -o mul -n1 10 -n2 5
```

Output:

```text
50.0
```

### Division

```bash
python arithmetic.py -o div -n1 10 -n2 5
```

Output:

```text
2.0
```

## Error Handling

The script displays an error when:

- An unsupported operation is provided.
- A required argument is missing.
- The user attempts to divide by zero.
