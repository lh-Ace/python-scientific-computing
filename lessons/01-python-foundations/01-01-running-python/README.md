# Lesson 01.01 — What is a Python program, and how do I run one?

**Status:** Not started  
**Prerequisites:** None  
**New vocabulary:** program, source code, Python interpreter, expression, string, `print`, terminal, file, output.

## Why this lesson exists

Before discussing variables, solvers, or libraries, we must distinguish **instructions in a file** from **the program that executes those instructions**. In Python, a `.py` file contains source code. CPython reads it, compiles it internally to bytecode, and executes that bytecode in a Python runtime. The details of bytecode and compilation belong to Module 02; right now, understand that source code is not itself a machine-executable application.

`uv` is not Python and it is not a numerical library. Here it selects and manages the Python environment and launches the actual interpreter. We use the terminal to make program execution visible instead of hiding it behind a notebook.

## By the end you should be able to

1. Point to the file containing source code.
2. Explain in simple words what the terminal, `uv`, and Python interpreter each do.
3. Predict what a `print(...)` statement produces.
4. Run a Python file, change it, and rerun it.
5. Distinguish a numerical expression like `2 + 3` from the output action `print(2 + 3)`.
6. Record actual observations and mistakes in a lesson journal.

## First: inspect without running

Open `hello.py`. Before running it, write in `journal.md` what you expect to see on each output line. Answer:

- What text will be printed exactly?
- Will `2 + 3` appear literally or as a number? Why?
- Does a quoted phrase behave like an unquoted arithmetic expression?

## Run it

From the **repository root**:

```bash
uv run python --version
uv run python lessons/01-python-foundations/01-01-running-python/hello.py
```

The words `uv run python` request that uv launch Python inside the project environment. The path after that is the source file. Python executes the instructions in the file in order. Observe and compare the output with your prediction.

## Original exercises (do them in order)

**A — Experiment with expressions.** Add a line that prints `9 + 6`. Before running, predict the printed result. Then try `9 * 6`. Record both observations. The `*` operator means multiplication.

**B — Separate text and numbers.** Add a line that prints the text `9 + 6` literally, using quotes. Explain why it differs from `print(9 + 6)`.

**C — Change the order.** Rearrange the print statements. Does output order change? Explain why in your own words.

**D — Reason independently.** Without running code first, write what `print(10 - 4)` should produce. Test and record the result.

**E — Debug gently.** In a temporary experiment, remove a closing parenthesis from a `print(...)` call. Read the error message, restore it, and explain what the error is telling you. Never commit intentionally broken final code unless its purpose is clearly labeled.

Do **not** use variables, functions of your own, NumPy, Jupyter, or other modules in this lesson—we have not taught them yet.

## What to submit for review

- Your updated `hello.py`.
- A completed `journal.md`, with your *initial* predictions preserved and corrections described.
- At least one meaningful exercise commit, such as `exercise(01.01): investigate print and arithmetic`.
- Explain: source file vs interpreter vs terminal vs uv; expression vs output; one mistake and the reason for its correction.

Run this small repository check as an introduction to automatic verification (you do **not** need to understand test code yet):

```bash
uv run python -m unittest discover -s tests -v
```

The check ensures the starting program can run; it does not grade the quality of your reasoning or all of the exercises.

## Sources and provenance

- Allen B. Downey, *Think Python* (3rd edition), early chapters on programming and expressions: https://allendowney.github.io/ThinkPython/
- Hans Fangohr, *Introduction to Python for Computational Science and Engineering*, introductory chapters: https://fangohr.github.io/introduction-to-python-for-computational-science-and-engineering/
- Official Python Tutorial, section on using the interpreter: https://docs.python.org/3/tutorial/interpreter.html

This lesson's wording and exercises are original; links supply further reading and independent perspectives.
