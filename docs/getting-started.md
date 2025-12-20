# Getting Started with Python Programming

Welcome to COS 184! This guide will help you set up your Python programming environment and get ready for the course.

## Step 1: Install Python

### Windows

1. Visit [python.org](https://www.python.org/downloads/)
2. Download the latest Python 3.x installer
3. Run the installer
4. **Important:** Check the box "Add Python to PATH" before clicking "Install Now"
5. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

### macOS

1. Python 3 can be installed via Homebrew (recommended):
   ```bash
   brew install python3
   ```
   Or download from [python.org](https://www.python.org/downloads/)

2. Verify installation:
   ```bash
   python3 --version
   ```

### Linux

Most Linux distributions come with Python pre-installed. If not:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

Verify installation:
```bash
python3 --version
```

## Step 2: Choose an Editor/IDE

You'll need a text editor or IDE to write Python code. Here are some popular options:

### Recommended for Beginners

#### VS Code (Visual Studio Code)
- **Free and powerful**
- Download from: https://code.visualstudio.com/
- Install the Python extension from the Extensions marketplace
- Great for all skill levels

#### PyCharm Community Edition
- **Full-featured Python IDE**
- Download from: https://www.jetbrains.com/pycharm/download/
- Free community edition available
- Excellent for learning Python

### Alternative Options

- **IDLE**: Comes with Python installation, simple and lightweight
- **Jupyter Notebook**: Great for learning and experimentation
- **Sublime Text**: Fast and customizable
- **Atom**: Open-source and extensible

## Step 3: Set Up Your Workspace

1. Create a folder for your course work:
   ```bash
   mkdir cos184-python
   cd cos184-python
   ```

2. Clone the course repository:
   ```bash
   git clone https://github.com/jamesquinlan/cos184-python.git
   cd cos184-python
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - **Windows:**
     ```
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

5. When the virtual environment is active, you'll see `(venv)` in your terminal prompt.

## Step 4: Test Your Setup

Create a simple test file to ensure everything works:

1. Create a file named `hello.py`:
   ```python
   print("Hello, Python!")
   print(f"Python is working correctly!")
   
   # Test basic math
   result = 2 + 2
   print(f"2 + 2 = {result}")
   
   # Get Python version
   import sys
   print(f"Python version: {sys.version}")
   ```

2. Run the file:
   ```bash
   python hello.py
   ```
   or
   ```bash
   python3 hello.py
   ```

3. You should see output similar to:
   ```
   Hello, Python!
   Python is working correctly!
   2 + 2 = 4
   Python version: 3.x.x ...
   ```

## Step 5: Learn the Basics

### Running Python Interactively

You can run Python in interactive mode (REPL):
```bash
python
```
or
```bash
python3
```

Try some commands:
```python
>>> print("Hello!")
>>> 5 + 3
>>> name = "Student"
>>> print(f"Welcome, {name}!")
>>> exit()
```

### Python File Basics

- Python files end with `.py`
- Run Python files with: `python filename.py`
- Comments start with `#`
- Python uses indentation (spaces or tabs) for code blocks

## Common Issues and Solutions

### Issue: "python: command not found"
- **Solution:** Use `python3` instead of `python`
- Or add Python to your PATH (Windows)

### Issue: "Permission denied" (Linux/macOS)
- **Solution:** Use `python3` or check file permissions

### Issue: "pip: command not found"
- **Solution:** Use `python -m pip` or `python3 -m pip`
- Or install pip: `python3 -m ensurepip`

### Issue: Import errors
- **Solution:** Make sure you're in the correct directory and have activated your virtual environment (if using one)

## Additional Resources

### Official Documentation
- Python Documentation: https://docs.python.org/3/
- Python Tutorial: https://docs.python.org/3/tutorial/

### Learning Resources
- Real Python: https://realpython.com/
- Python for Everybody: https://www.py4e.com/
- W3Schools Python: https://www.w3schools.com/python/
- Python Tutor (visualize code execution): https://pythontutor.com/

### Practice Sites
- HackerRank: https://www.hackerrank.com/domains/python
- LeetCode: https://leetcode.com/
- Codewars: https://www.codewars.com/
- Exercism: https://exercism.org/tracks/python

## Getting Help

If you encounter issues:

1. Check the error message carefully
2. Search for the error online (Stack Overflow is helpful)
3. Review the course documentation
4. Ask your instructor during office hours
5. Collaborate with classmates (but submit individual work!)

## Next Steps

Now that you're set up:

1. Read through the course syllabus in `docs/syllabus.md`
2. Explore the example code in the `src/` directory
3. Start with Lab 1 in the `labs/` directory
4. Review lecture slides as they become available

---

**Congratulations!** You're ready to start your Python programming journey! 🎉🐍
