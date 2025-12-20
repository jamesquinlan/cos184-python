# Lab 1: Introduction to Python and Basic Operations

**Course:** COS 184 - Introduction to Python Programming  
**Due Date:** Week 2  
**Points:** 100

## Objectives

In this lab, you will:
- Write your first Python programs
- Work with variables and basic data types
- Perform arithmetic operations
- Use input and output functions
- Practice basic string manipulation

## Prerequisites

- Python 3.8 or higher installed
- Text editor or IDE set up
- Completed the "Getting Started" guide

## Instructions

Complete all exercises in this lab. Create a separate Python file for each exercise, named as indicated. Test your code thoroughly before submission.

---

## Exercise 1: Hello, World! (10 points)

Create a file named `hello.py` that prints a greeting message.

**Requirements:**
- Print "Hello, World!" to the console
- Print your name on a new line
- Print "Welcome to COS 184!" on a third line

**Example Output:**
```
Hello, World!
John Doe
Welcome to COS 184!
```

---

## Exercise 2: Basic Arithmetic (15 points)

Create a file named `calculator.py` that performs basic arithmetic operations.

**Requirements:**
- Define two variables: `num1 = 15` and `num2 = 4`
- Calculate and print:
  - Sum
  - Difference
  - Product
  - Quotient (division)
  - Integer division
  - Remainder (modulus)
  - Exponentiation (num1 to the power of num2)

**Example Output:**
```
15 + 4 = 19
15 - 4 = 11
15 * 4 = 60
15 / 4 = 3.75
15 // 4 = 3
15 % 4 = 3
15 ** 4 = 50625
```

---

## Exercise 3: Variables and Data Types (15 points)

Create a file named `datatypes.py` that demonstrates different data types.

**Requirements:**
- Create variables of the following types:
  - Integer (your age)
  - Float (your height in meters)
  - String (your favorite color)
  - Boolean (whether you like Python - True or False)
- Print each variable with a descriptive label
- Print the type of each variable using `type()`

**Example Output:**
```
Age: 20 (Type: <class 'int'>)
Height: 1.75 (Type: <class 'float'>)
Favorite color: blue (Type: <class 'str'>)
Likes Python: True (Type: <class 'bool'>)
```

---

## Exercise 4: User Input (20 points)

Create a file named `greeting.py` that interacts with the user.

**Requirements:**
- Ask the user for their first name
- Ask the user for their last name
- Ask the user for their age
- Print a personalized greeting using all the information
- Calculate and print the year they were born (assume current year is 2025)

**Example Output:**
```
Enter your first name: Jane
Enter your last name: Smith
Enter your age: 22
Hello, Jane Smith!
You are 22 years old.
You were born in approximately 2003.
```

---

## Exercise 5: String Operations (20 points)

Create a file named `strings.py` that demonstrates string manipulation.

**Requirements:**
- Create a variable with your full name
- Print the length of your name
- Print your name in uppercase
- Print your name in lowercase
- Print your name with the first letter of each word capitalized
- Replace spaces with hyphens
- Count how many times a specific letter appears in your name (you choose the letter)

**Example Output (for name "John Doe"):**
```
Full name: John Doe
Length: 8
Uppercase: JOHN DOE
Lowercase: john doe
Title case: John Doe
With hyphens: John-Doe
Number of 'o' letters: 2
```

---

## Exercise 6: Circle Calculations (20 points)

Create a file named `circle.py` that calculates circle properties.

**Requirements:**
- Define a variable `radius` with a value of 5.0
- Define `pi` as 3.14159
- Calculate and print:
  - Circumference (2 × π × radius)
  - Area (π × radius²)
- Format the output to 2 decimal places

**Example Output:**
```
Radius: 5.0
Circumference: 31.42
Area: 78.54
```

**Bonus (+5 points):** Modify the program to ask the user for the radius instead of hardcoding it.

---

## Submission Guidelines

1. Create a folder named `lab1_yourname` (replace "yourname" with your actual name)
2. Place all Python files in this folder:
   - `hello.py`
   - `calculator.py`
   - `datatypes.py`
   - `greeting.py`
   - `strings.py`
   - `circle.py`
3. Test each program to ensure it runs without errors
4. Submit according to your instructor's guidelines

## Grading Rubric

| Criteria | Points |
|----------|--------|
| Exercise 1: Hello World | 10 |
| Exercise 2: Basic Arithmetic | 15 |
| Exercise 3: Data Types | 15 |
| Exercise 4: User Input | 20 |
| Exercise 5: String Operations | 20 |
| Exercise 6: Circle Calculations | 20 |
| **Total** | **100** |
| Bonus (Circle with user input) | +5 |

### Deductions
- Code does not run: -50% per exercise
- Incorrect output: -25% per exercise
- Poor code style/readability: -10%
- Late submission: -10% per day (up to 3 days)

## Tips

- Test your code frequently as you write it
- Use meaningful variable names
- Add comments to explain your code
- Make sure your output is clear and readable
- Use the Python interactive mode (`python` or `python3`) to test small code snippets

## Help and Resources

- Python Documentation: https://docs.python.org/3/
- Course `docs/getting-started.md` for setup help
- Example code in the `src/` directory
- Office hours with your instructor

---

Good luck! 🐍
