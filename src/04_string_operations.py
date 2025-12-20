"""
Example: String Operations
Demonstrates string manipulation in Python.
"""

# Creating strings
name = "Python Programming"
course = 'COS 184'  # Single or double quotes work

print("String Basics")
print("-" * 40)

# String length
print(f"String: '{name}'")
print(f"Length: {len(name)}")

# String concatenation
greeting = "Hello, " + "World!"
print(f"Concatenation: {greeting}")

# String repetition
print(f"Repetition: {'Python' * 3}")

# String methods
print("\nString Methods:")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Title Case: {name.title()}")
print(f"Replace: {name.replace('Python', 'Java')}")

# String indexing (0-based)
print("\nString Indexing:")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Third character: {name[2]}")

# String slicing
print("\nString Slicing:")
print(f"First 6 characters: {name[0:6]}")
print(f"From index 7 onward: {name[7:]}")
print(f"Last 11 characters: {name[-11:]}")

# String formatting
age = 20
height = 5.9

# f-strings (Python 3.6+)
print("\nString Formatting:")
message = f"I am {age} years old and {height} feet tall."
print(message)

# format() method
message = "I am {} years old and {} feet tall.".format(age, height)
print(message)

# String checking
text = "Hello123"
print("\nString Checking:")
print(f"Is alphanumeric? {text.isalnum()}")
print(f"Is alphabetic? {text.isalpha()}")
print(f"Is digit? {text.isdigit()}")
print(f"Starts with 'Hello'? {text.startswith('Hello')}")
print(f"Ends with '123'? {text.endswith('123')}")

# Counting and finding
sentence = "Python is awesome! I love Python."
print("\nCounting and Finding:")
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Find 'awesome': {sentence.find('awesome')}")
print(f"Index of 'love': {sentence.index('love')}")
