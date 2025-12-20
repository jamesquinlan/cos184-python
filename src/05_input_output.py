"""
Example: User Input and Output
Demonstrates getting input from users and formatting output.
"""

print("User Input Example")
print("-" * 40)

# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input with type conversion
age_str = input("Enter your age: ")
age = int(age_str)  # Convert string to integer
print(f"You are {age} years old.")

# Multiple inputs
print("\nLet's calculate the area of a rectangle:")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"The area is: {area:.2f}")

# Formatted output
print("\nFormatted Output Examples:")

# Using f-strings
pi = 3.14159265359
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Pi to 4 decimal places: {pi:.4f}")

# Alignment
print("\nAlignment:")
print(f"{'Left':<10}|{'Center':^10}|{'Right':>10}")
print(f"{'---':<10}|{'---':^10}|{'---':>10}")
print(f"{'Item1':<10}|{'Item2':^10}|{'Item3':>10}")

# Numbers with formatting
number = 1234567.89
print(f"\nNumber formatting: {number:,.2f}")  # Comma separator

# Percentage
accuracy = 0.8534
print(f"Accuracy: {accuracy:.1%}")  # As percentage

# Padding with zeros
order_num = 42
print(f"Order number: {order_num:05d}")  # Pad with zeros

print("\n" + "=" * 40)
print("End of examples")
