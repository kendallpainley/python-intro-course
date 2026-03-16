# Python Mastery: From Fundamentals to Advanced 

A hands-on Python course with **20 modules** taking you from absolute zero to advanced Python developer.

---

## Course Structure

Each module contains:
- **`lesson_XX_topic.ipynb`** — Jupyter notebook with theory, explanations, and live code demos
- **`exercises/ex_XX_topic.py`** — Hands-on exercises with **solutions hidden at the bottom**

---

## Curriculum

| Module | Topic | Key Concepts |
|--------|-------|--------------|
| 01 | Getting Started | `print()`, comments, running Python |
| 02 | Variables & Data Types | `int`, `float`, `str`, `bool`, `None`, `type()` |
| 03 | Operators | Arithmetic, comparison, logical, assignment |
| 04 | Strings In Depth | Indexing, slicing, methods, f-strings |
| 05 | User Input & Type Conversion | `input()`, `int()`, `float()`, truthy/falsy |
| 06 | Control Flow | `if` / `elif` / `else`, ternary, `match` |
| 07 | While Loops | `while`, `break`, `continue`, `else` |
| 08 | For Loops | `for`, `range()`, `enumerate()`, `zip()` |
| 09 | Functions | `def`, `return`, `*args`, `**kwargs`, lambda, recursion |
| 10 | Lists | Indexing, mutation, methods, sorting, nested lists |
| 11 | Tuples, Sets & Dicts | All three data structures, when to use each |
| 12 | File I/O | Reading/writing files, `pathlib`, CSV |
| 13 | Error Handling | `try`/`except`/`else`/`finally`, custom exceptions |
| 14 | OOP Fundamentals | Classes, `__init__`, methods, properties |
| 15 | Advanced OOP | Inheritance, polymorphism, dunder methods, ABC |
| 16 | Modules & Packages | `import`, standard library, `pip`, `venv` |
| 17 | Comprehensions | List, dict, set comprehensions, generators |
| 18 | Iterators & Generators | `iter`/`next`, `yield`, `yield from` |
| 19 | Decorators & Closures | Closures, `@decorator`, `functools` |
| 20 | Advanced Topics | Type hints, dataclasses, `collections`, `itertools`, regex, concurrency |

---

## Quick Start

### Prerequisites
- Python 3.10 or later
- IDE

### Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/python-intro-course.git
cd python-intro-course
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate it**
```bash
# macOS / Linux:
source venv/bin/activate

# Windows (Command Prompt):
venv\Scripts\activate.bat

# Windows (PowerShell):
venv\Scripts\Activate.ps1
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Open in IDE**
- File → Open → select the `python-intro-course` folder
- IDE will detect `venv` automatically
- If not: Settings → Project → Python Interpreter → select `venv/bin/python`

---

## How to Use This Course

### Reading Lessons (Jupyter Notebooks)
1. Double-click any `.ipynb` file in IDE
2. Run cells with **Shift+Enter**
3. **Experiment!** Change the code and re-run — this is how you learn

### Exercises (`.py` files)
1. Open the exercise file for the module you're on
2. Read each `# TODO:` comment and write your code below it
3. Run the file: right-click → **Run**, or press the green ▶ button
4. Check your output against the expected results
5. **Only scroll to the SOLUTIONS section after you've genuinely tried**


---

## Running Notebooks Outside IDE

If you prefer JupyterLab:
```bash
jupyter lab
```
Then navigate to any module folder and open the `.ipynb` file.

---

## Project Structure

```
python-intro-course/
├── README.md
├── requirements.txt
├── .gitignore
├── module_01_getting_started/
│   ├── lesson_01_getting_started.ipynb
│   └── exercises/
│       └── ex_01_getting_started.py
├── module_02_variables_and_data_types/
│   ├── lesson_02_variables_and_data_types.ipynb
│   └── exercises/
│       └── ex_02_variables_and_data_types.py
... (continued)
```

---

## Contributing / Issues

Found a bug in an exercise or notebook? Open an issue or submit a PR!

---

*Happy coding!*
