# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a basic Python learning repository ("Hello Python") containing structured exercises organized by programming concepts. The repository contains 11 exercise files covering fundamental Python topics from basic syntax to functions.

## Architecture

The repository follows a simple educational structure:

- **Exercise Files**: Numbered Python files (`00_` to `10_`) each focusing on a specific Python concept
- **Sequential Learning**: Files are designed to be worked through in numerical order
- **Exercise Format**: Each file contains multiple numbered exercises with solutions implemented directly in the code

### File Organization
- `00_hello-python-exercises.py` - Introduction to Python basics and print statements
- `01_variables-exercises.py` - Variables and data types
- `02_operator-exercises.py` - Operators
- `03_string-exercises.py` - String manipulation
- `04_lists-exercises.py` - Lists
- `05_tuples-exercises.py` - Tuples
- `06_sets-exercises.py` - Sets
- `07_dict-exercises.py` - Dictionaries
- `08_conditionals-exercises.py` - Conditional statements
- `09_loops-exercises.py` - Loops
- `10_functions-exercises.py` - Functions
- `Exercises.pdf` - Supporting material

## Common Commands

### Running Individual Exercise Files
```bash
python3 00_hello-python-exercises.py
python3 01_variables-exercises.py
# ... and so on for any specific exercise file
```

### Running All Exercise Files in Sequence
```bash
for file in [0-1][0-9]_*.py; do echo "=== Running $file ==="; python3 "$file"; echo; done
```

### Interactive Python Sessions
```bash
python3 -i 10_functions-exercises.py  # Load a specific file and start interactive session
python3  # Start Python REPL for testing concepts
```

## Code Patterns

### Exercise Structure
Each exercise file follows this pattern:
- Comments indicate exercise numbers (`#01`, `#02`, etc.)
- Solutions are implemented immediately after the exercise comment
- Some exercises have commented-out input statements for interactive testing

### Language Features Used
- **Spanish Comments**: All comments and some variable names are in Spanish
- **Basic Python**: Uses fundamental Python 3 features without external dependencies
- **Print-based Output**: Most exercises use `print()` for demonstration
- **Type Checking**: Exercises explore Python's dynamic typing with `type()` function

### Testing Individual Concepts
To test or modify a specific concept:
1. Open the relevant numbered file
2. Locate the exercise by its comment number (e.g., `#05`)
3. Run the entire file or copy the specific exercise to test interactively

## Development Notes

- **No Dependencies**: Pure Python 3.12+ with no external packages required
- **Educational Focus**: Code prioritizes learning clarity over production best practices
- **Interactive Elements**: Some exercises include commented-out `input()` statements that can be uncommented for interactive learning
- **Spanish Language**: Repository is designed for Spanish-speaking learners

## Rules

User prefers to keep their GitHub repositories private and not visible to anyone else.