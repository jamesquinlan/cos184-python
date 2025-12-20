"""
Example: Variables and Data Types
Demonstrates different data types in Python.
"""

# Integer
age = 20
print(f"Age: {age}, Type: {type(age)}")

# Float
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String
name = "Alice"
print(f"Name: {name}, Type: {type(name)}")

# Boolean
is_student = True
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# Multiple assignment
x, y, z = 1, 2.5, "three"
print(f"x={x}, y={y}, z={z}")

# Constants (convention: use uppercase)
PI = 3.14159
MAX_STUDENTS = 30
print(f"PI: {PI}")
print(f"Max Students: {MAX_STUDENTS}")

# Type conversion
num_str = "100"
num_int = int(num_str)
print(f"String '{num_str}' converted to integer: {num_int}")

float_num = float("3.14")
print(f"String '3.14' converted to float: {float_num}")
