# Lesson 01.04 — Strings and Output

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lessons 01.01–01.03  
**Environment:** Python, VS Code, uv

## 1. Why this lesson exists

Programs rarely work with numbers alone. They also need to represent words, labels, messages, identifiers, and human-readable results.

Python uses the `str` type to represent text as sequences of Unicode characters.

This lesson introduces string literals, elementary string operations, escape sequences, type conversion for output, and string formatting.

Understanding these concepts is necessary before we develop programs that communicate results clearly to users.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Create strings using single and double quotation marks.
2. Distinguish numerical values from textual representations of numbers.
3. Inspect string types using `type()`.
4. Combine text and values using `print()`.
5. Explain string concatenation and repetition.
6. Use common escape sequences.
7. Recognize and resolve elementary string-related errors.
8. Convert numerical values to text using `str()`.
9. Construct formatted strings using f-strings.
10. Display numbers with a specified number of decimal places.
11. Explain the difference between formatting a value and changing its underlying numerical representation.
12. Independently produce a readable text report.

## 3. Core concepts and worked examples

### A — String fundamentals

A string is an object representing text.

Examples:

- `message = "Hello"`
- `language = 'Python'`
- `number_as_text = "42"`

Single and double quotation marks can both delimit string literals.

The expression `42` produces an integer, whereas `"42"` produces a string.

Use `type()` to inspect these differences.

### B — Printing text and values

The `print()` function can receive multiple arguments, separated by commas.

Example: `print("Distance:", 12)`

By default, `print()` separates arguments with spaces and ends the output with a newline.

Later in this activity, investigate the optional `sep` and `end` arguments:

- `sep` controls the separator between multiple printed arguments.
- `end` controls what is printed after the final argument.

### C — Quotes and escape sequences

Quotation marks delimit strings, but they can also appear as characters inside strings.

Escape sequences allow special characters to be represented within string literals.

Investigate:

- `\n` — newline
- `\t` — horizontal tab
- `\\` — literal backslash
- `\"` — double quotation mark
- `\'` — single quotation mark

The backslash introduces an escape sequence in ordinary Python string literals.

### D — Elementary string operations

The `+` operator concatenates strings.

Example: `"Py" + "thon"` produces `"Python"`.

The `*` operator can repeat a string.

Example: `"Hi" * 3` produces `"HiHiHi"`.

String addition differs from numerical addition.

Attempting to concatenate an ordinary string and integer directly raises `TypeError`.

Use `str()` to obtain the textual representation of a value when needed.

### E — F-strings and formatted output

An f-string is a string literal preceded by `f`.

Expressions inside `{}` are evaluated and included in the resulting string.

Example: `name = "Ada"` followed by `print(f"Hello, {name}!")`.

F-strings can incorporate existing numerical variables and arithmetic expressions.

Formatting instructions can control how a value is displayed.

For example, the format specification `.2f` displays a floating-point number with two digits after the decimal point.

**Important:** Formatting changes the textual representation, not the underlying numerical object.

### F — Independent mini-lab: Receipt generator

Create `receipt_lab.py`.

Implement a small receipt without copying an instructor solution.

Requirements:

1. Store the product name as a string.
2. Store the quantity as an integer.
3. Store the unit price as a floating-point number.
4. Calculate the total price.
5. Print a readable receipt containing the product name, quantity, unit price, and total.
6. Format monetary values with two decimal places.
7. Include a title and at least one line break.
8. Change the quantity and verify that the calculated total changes correctly.
9. Explain the difference between the numerical value and its formatted string representation.

Use only previously taught concepts and the new features introduced in this lesson.

No `input()`, loops, conditionals, user-defined functions, or external libraries are required.

## 4. Programming activities

**Activity A — String values and types**

File: `strings.py`

- Create string variables.
- Print their values and types.
- Compare text containing digits with integer literals.
- Predict outputs before execution.

**Activity B — Constructing output**

File: `strings.py`

- Print text alongside numerical variables.
- Experiment with multiple `print()` arguments.
- Compare default and customized separators and line endings.

**Activity C — Quotation marks and escapes**

File: `strings.py`

- Include quotation marks within strings.
- Produce multiple output lines.
- Experiment with tabs and literal backslashes.

**Activity D — String operations and errors**

File: `output_format.py`

- Concatenate two strings.
- Repeat a string.
- Investigate a string/integer type mismatch.
- Correct the error using an appropriate conversion or output technique.

**Activity E — F-strings and formatting**

File: `output_format.py`

- Insert variables into text.
- Include arithmetic results in an f-string.
- Format a floating-point number to two decimal places.
- Explain the difference between displayed precision and stored numerical precision.

**Activity F — Independent receipt mini-lab**

File: `receipt_lab.py`

- Complete the requirements in Section 3F.
- Test at least two quantities.
- Explain the calculations and formatting choices.

## 5. Independent verification

Before each experiment:

1. Predict the output.
2. Write or examine the program.
3. Execute it.
4. Compare the actual result with the prediction.
5. Explain surprises or errors.

From the repository root, run:

`uv run python lessons/01-python-foundations/01-04-strings-and-output/strings.py`

`uv run python lessons/01-python-foundations/01-04-strings-and-output/output_format.py`

`uv run python lessons/01-python-foundations/01-04-strings-and-output/receipt_lab.py`

Also run:

`uv run python -m unittest discover -s tests -v`

Record actual failures honestly. An existing bootstrap test passing does not necessarily test all the new lesson exercises.

## 6. Required submission

- `README.md`
- `journal.md`
- `strings.py`
- `output_format.py`
- `receipt_lab.py`
- GitHub pull request containing the completed lesson

## 7. Assessment requirements

The learner should independently demonstrate:

- Correct string literal syntax.
- Understanding of strings versus numerical values.
- Correct concatenation and repetition.
- Appropriate use of escape sequences.
- Ability to interpret a basic `TypeError`.
- Correct type conversion when constructing text.
- Accurate f-string and numerical formatting behavior.
- Independent construction of a readable receipt.
- Explanation of formatting versus numerical precision.

The instructor reviews code and demonstrated reasoning before marking the lesson Verified.

## 8. Reflection

Use the short `journal.md` document.

The journal should preserve one meaningful prediction, one observation, and any important correction or discovery. Detailed exercise transcripts are not required.

## 9. Sources and provenance

- Python Software Foundation — Python Tutorial, introductory strings: https://docs.python.org/3/tutorial/introduction.html#text

- Python Software Foundation — Input and Output: https://docs.python.org/3/tutorial/inputoutput.html

- Python Software Foundation — Format String Syntax: https://docs.python.org/3/library/string.html#format-string-syntax

- Python Software Foundation — Built-in `print()` and `str()`: https://docs.python.org/3/library/functions.html

- Allen B. Downey — *Think Python*, 3rd edition: https://allendowney.github.io/ThinkPython/

Lesson exercises and instructional structure are original course materials.

## 10. Review

**Assessment:** Pending  
**Status:** Not yet verified

Instructor feedback, commit references, and final verification are tracked through GitHub.
