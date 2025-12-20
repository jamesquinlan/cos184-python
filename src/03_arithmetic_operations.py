"""
Example: Basic Arithmetic Operations
Demonstrates arithmetic operators in Python.
"""

# Define numbers
a = 10
b = 3

print("Basic Arithmetic Operations")
print("-" * 30)

# Addition
result = a + b
print(f"{a} + {b} = {result}")

# Subtraction
result = a - b
print(f"{a} - {b} = {result}")

# Multiplication
result = a * b
print(f"{a} * {b} = {result}")

# Division (float result)
result = a / b
print(f"{a} / {b} = {result:.2f}")

# Floor Division (integer result)
result = a // b
print(f"{a} // {b} = {result}")

# Modulus (remainder)
result = a % b
print(f"{a} % {b} = {result}")

# Exponentiation
result = a ** b
print(f"{a} ** {b} = {result}")

# Order of operations (PEMDAS)
print("\nOrder of Operations:")
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")

result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")

# Compound assignment operators
x = 5
print(f"\nCompound Assignments (starting with x = {x}):")

x += 3  # x = x + 3
print(f"x += 3 => x = {x}")

x -= 2  # x = x - 2
print(f"x -= 2 => x = {x}")

x *= 2  # x = x * 2
print(f"x *= 2 => x = {x}")

x /= 3  # x = x / 3
print(f"x /= 3 => x = {x:.2f}")
