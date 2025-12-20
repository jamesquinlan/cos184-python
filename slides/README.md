# Lecture Slides

This directory contains lecture slides and presentation materials for COS 184 - Introduction to Python Programming.

## Available Slides

- **[Week 1: Introduction to Python Programming](week1-introduction.md)**
  - What is Python?
  - Setting up your environment
  - First program
  - Variables and data types
  - Basic operators

## Slide Format

Slides are provided in Markdown format with section separators (`---`). They can be:
- Viewed directly in any text editor
- Converted to presentations using tools like:
  - [Marp](https://marp.app/)
  - [reveal.js](https://revealjs.com/)
  - [Slidev](https://sli.dev/)

## Converting Slides to Presentations

### Using Marp (Recommended)

1. Install Marp CLI:
   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. Convert to HTML:
   ```bash
   marp week1-introduction.md -o week1.html
   ```

3. Convert to PDF:
   ```bash
   marp week1-introduction.md -o week1.pdf
   ```

### Using Pandoc

```bash
pandoc week1-introduction.md -o week1.html -s -t revealjs
```

## Viewing Slides

You can view the slides:
- As plain Markdown in GitHub or any text editor
- As rendered presentations after conversion
- In VS Code with the Marp extension

## Course Schedule

Slides will be added weekly according to the course schedule:
- Week 1: Introduction
- Week 2: Control Structures
- Week 3: Functions
- Week 4: Data Structures
- (More to be added)

## Contributing

Students are welcome to suggest improvements or corrections to the slides. Contact your instructor with any feedback.

---

*Last Updated: December 2025*
