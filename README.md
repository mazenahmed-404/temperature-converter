# Temperature Converter

A command-line temperature conversion application developed using Python.

The program allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin through an interactive terminal interface.

## Features

- Celsius to Fahrenheit
- Celsius to Kelvin
- Fahrenheit to Celsius
- Fahrenheit to Kelvin
- Kelvin to Celsius
- Kelvin to Fahrenheit
- Same-unit temperature handling
- Basic validation for negative Kelvin values
- Results displayed to three decimal places for conversions

## Technologies

- Python 3

## Concepts Demonstrated

- Variables and data types
- User input and output
- Functions and return values
- Conditional statements
- Mathematical operations
- Floating-point arithmetic
- Input validation
- F-string formatting

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open the project directory in your terminal.
4. Run:

```bash
python main.py
```

## Example

```text
Welcome! Please, Enter the temperature you got: 25

Enter the temperature unit: c
Enter the desired temperature unit: f

The Converted Temperature value is: 77.000 °F
```

## Limitations

- Temperature units must be entered using lowercase letters: c, f, or k.
- Non-numerical temperature input is not yet handled.
- Physical temperature validation below absolute zero is not implemented for Celsius and Fahrenheit.

## Project Status

Completed — Beginner Python Project.

Developed independently as part of my Python programming practice.
