# Week 1: Introduction to Python Programming

**Course:** COS 184 - Introduction to Python Programming  
**Instructor:** James Quinlan

---

## Lecture Overview

- What is Python?
- Why Python?
- Course overview
- Setting up Python
- Your first Python program
- Basic syntax and concepts

---

## What is Python?

- **High-level** programming language
- **Interpreted** (no compilation needed)
- **General-purpose** (web, data science, automation, AI, etc.)
- Created by Guido van Rossum in 1991
- Named after Monty Python's Flying Circus

---

## Why Python?

### Advantages

- ✅ Easy to learn and read
- ✅ Powerful and versatile
- ✅ Large community and ecosystem
- ✅ Extensive libraries (100,000+)
- ✅ Cross-platform
- ✅ Great for beginners AND professionals

### Popular Uses

- Web development (Django, Flask)
- Data Science (Pandas, NumPy)
- Machine Learning (TensorFlow, PyTorch)
- Automation and scripting
- Scientific computing

---

## Python Versions

- **Python 2.x** - Legacy (end of life: 2020)
- **Python 3.x** - Current (we'll use this)
  - Python 3.8+ recommended
  - Latest: Python 3.12+

---

## Course Overview

### Topics We'll Cover

1. Python basics (variables, types, operators)
2. Control structures (if, loops)
3. Functions and modules
4. Data structures (lists, dicts, sets)
5. File I/O
6. Object-oriented programming
7. Error handling
8. Popular libraries

---

## Setting Up Python

### Installation

**Windows/Mac/Linux:**
- Download from [python.org](https://python.org)
- Or use package manager (brew, apt, etc.)

### Verify Installation

```bash
python --version
# or
python3 --version
```

---

## Python Interactive Mode

Also called REPL (Read-Eval-Print Loop)

```bash
$ python
>>> print("Hello!")
Hello!
>>> 2 + 2
4
>>> exit()
```

Great for:
- Testing code snippets
- Learning Python
- Quick calculations

---

## Your First Python Program

Create a file `hello.py`:

```python
print("Hello, World!")
```

Run it:

```bash
python hello.py
```

Output:
```
Hello, World!
```

---

## Python Syntax Basics

### Comments

```python
# This is a single-line comment

"""
This is a
multi-line comment
(or docstring)
"""
```

### Print Statement

```python
print("Hello")
print("Hello", "World")  # Multiple values
print("Number:", 42)      # Mixed types
```

---

## Variables

Variables store data:

```python
name = "Alice"
age = 20
height = 5.6
is_student = True
```

**Rules:**
- Start with letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive (`age` ≠ `Age`)
- Cannot use reserved keywords

---

## Data Types

### Basic Types

```python
# Integer
age = 25

# Float
price = 19.99

# String
name = "Python"

# Boolean
is_valid = True
```

### Check Type

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hello")   # <class 'str'>
type(True)      # <class 'bool'>
```

---

## Basic Operators

### Arithmetic

```python
5 + 3      # Addition: 8
5 - 3      # Subtraction: 2
5 * 3      # Multiplication: 15
5 / 3      # Division: 1.666...
5 // 3     # Floor Division: 1
5 % 3      # Modulus: 2
5 ** 3     # Exponentiation: 125
```

---

## String Basics

```python
# Creating strings
name = "Python"
course = 'COS 184'  # Single or double quotes

# Concatenation
greeting = "Hello " + "World"

# String methods
name.upper()     # "PYTHON"
name.lower()     # "python"
len(name)        # 6
```

---

## Getting User Input

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")

# With type conversion
age = int(input("Enter age: "))
print("You are", age, "years old")
```

---

## String Formatting

### f-strings (Recommended)

```python
name = "Alice"
age = 20
print(f"My name is {name} and I am {age}")
```

### format() method

```python
print("My name is {} and I am {}".format(name, age))
```

### Old style (%)

```python
print("My name is %s and I am %d" % (name, age))
```

---

## Python Indentation

Python uses **indentation** for code blocks (not braces):

```python
# This will be important for:
# - if statements
# - loops  
# - functions
# - classes

# Always use consistent indentation (4 spaces recommended)
```

---

## Common Errors

### SyntaxError

```python
print "Hello"  # Missing parentheses
```

### NameError

```python
print(x)  # x is not defined
```

### TypeError

```python
"5" + 5  # Can't add string and int
```

---

## Best Practices

1. **Use descriptive variable names**
   - ✅ `student_name` 
   - ❌ `sn` or `x`

2. **Follow PEP 8** (Python style guide)
   - 4 spaces for indentation
   - Lowercase with underscores for variables

3. **Add comments**
   - Explain WHY, not WHAT

4. **Test your code**
   - Run frequently
   - Check edge cases

---

## Resources

### Official

- Python.org: https://python.org
- Python Documentation: https://docs.python.org/3/
- Python Tutorial: https://docs.python.org/3/tutorial/

### Learning

- Real Python: https://realpython.com
- Python for Everybody: https://py4e.com
- W3Schools: https://w3schools.com/python/

---

## This Week's Tasks

1. ✅ Install Python
2. ✅ Set up your development environment
3. ✅ Complete Lab 1
4. ✅ Read the getting started guide
5. ✅ Practice examples from today

---

## Next Week

- Control structures (if/else)
- Boolean logic
- Comparison operators
- Logical operators

---

## Questions?

Office hours: [TBD]

---

**Thank you!**

Start practicing and see you next week! 🐍
