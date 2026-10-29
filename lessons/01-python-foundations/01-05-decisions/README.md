# Lesson 01.05 — Decisions

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lessons 01.01–01.04  
**Environment:** Python, VS Code, uv

## 1. Why this lesson exists

Until now, our programs have executed instructions sequentially.

Real programs must also evaluate conditions and choose which instructions to execute. This is called conditional execution, an essential form of control flow.

This lesson introduces Boolean values, comparisons, logical operators, and conditional statements.

These concepts form the foundation for later algorithms, loops, numerical tests, and scientific simulations.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Explain the Boolean type `bool`.
2. Distinguish `True` and `False` from strings containing those words.
3. Write comparison expressions using `==`, `!=`, `<`, `>`, `<=`, and `>=`.
4. Distinguish assignment (`=`) from equality comparison (`==`).
5. Combine conditions using `and`, `or`, and `not`.
6. Explain logical precedence in Boolean expressions.
7. Write `if`, `elif`, and `else` statements.
8. Use indentation correctly to define conditional blocks.
9. Trace which branches execute for given values.
10. Identify simple logical and syntactic errors.
11. Test boundary conditions.
12. Independently implement a small classification program.

## 3. Core concepts

### A — Boolean values and comparisons

Python's `bool` type represents logical truth values.

The two Boolean literals are:

- `True`
- `False`

The comparison operators are:

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

Comparison expressions produce Boolean results.

Example:

```python
distance = 12
print(distance > 10)
```

This displays `True`.

Unlike the assignment operator `=`, the operator `==` tests equality without assigning a value.

### B — Logical operators

Python provides three principal logical operators:

- `and` — Both conditions must be true.
- `or` — At least one condition must be true.
- `not` — Negates the truth value.

Their precedence, from highest to lowest, is:

1. `not`
2. `and`
3. `or`

Parentheses can make logical grouping explicit.

The behavior of these operators with non-Boolean objects and short-circuit evaluation will be introduced at an appropriate point.

### C — Conditional execution

The `if` statement executes a block when its condition is true.

Example:

```python
temperature = 30

if temperature > 25:
    print("Above threshold")
```

Important syntax:

- The condition follows `if`.
- A colon `:` finishes the statement header.
- The body is indented, conventionally using four spaces.
- Python uses indentation to define code blocks.

### D — Alternative branches

Use `else` when an alternative action is required.

Use `elif` when multiple conditions must be considered.

In an `if`/`elif`/`else` chain, Python evaluates conditions in order and executes only the first matching branch.

An `else` branch runs when none of the preceding conditions matches.

Multiple independent `if` statements are not necessarily equivalent to an `if`/`elif`/`else` chain.

### E — Debugging and boundary cases

Common problems include:

- Using `=` instead of `==` in a condition.
- Omitting the colon.
- Incorrect indentation.
- Comparing against the wrong threshold.
- Choosing `>` when `>=` was intended.
- Placing conditions in an incorrect order.

Boundary testing investigates values directly below, at, and above a threshold.

A successful execution does not prove that all branches behave correctly.

## 4. Programming activities

### Activity A — Boolean expressions

File: `comparisons.py`

- Compare integer and floating-point values.
- Inspect Boolean results using `type()`.
- Distinguish equality from assignment.
- Predict comparison outputs before executing.

### Activity B — Logical operators

File: `comparisons.py`

- Combine conditions using `and`, `or`, and `not`.
- Predict outcomes of compound expressions.
- Investigate logical grouping with parentheses.

### Activity C — First conditional program

File: `conditionals.py`

- Write an `if` statement.
- Add an `else` branch.
- Identify which instructions execute.
- Experiment with different variable values.

### Activity D — Multiple decisions

File: `conditionals.py`

- Introduce `elif`.
- Construct a three-way classification.
- Compare an `if`/`elif`/`else` chain with independent `if` statements.
- Test cases satisfying different branches.

### Activity E — Debugging

File: `conditionals.py`

- Identify and correct a syntax or indentation error.
- Investigate an incorrect boundary condition.
- Explain the correction.

### Activity F — Independent mini-lab

File: `sensor_lab.py`

Create a simple laboratory temperature monitor.

The acceptable temperature interval is 18°C through 26°C, inclusive.

Requirements:

1. Store a temperature measurement in a variable.
2. Store the minimum and maximum thresholds.
3. Use comparisons and logical operators to determine whether the measurement is within the acceptable range.
4. Use `if`/`elif`/`else` to classify the measurement as below range, within range, or above range.
5. Display a clear report using f-strings.
6. Test at least four measurements, including both boundary values.
7. Explain why the selected conditions cover all possible numerical measurements.

Do not use loops, user input, or user-defined functions. Those belong to later lessons.

## 5. Independent verification

For every activity:

1. Predict the behavior before execution.
2. Write the code independently.
3. Execute it.
4. Compare results with predictions.
5. Investigate errors.
6. Explain why the program works.

Run each completed script from the repository root:

```bash
uv run python lessons/01-python-foundations/01-05-decisions/comparisons.py

uv run python lessons/01-python-foundations/01-05-decisions/conditionals.py

uv run python lessons/01-python-foundations/01-05-decisions/sensor_lab.py

uv run python -m unittest discover -s tests -v
```

Test output and code review provide complementary evidence. A passing bootstrap test alone does not verify the lesson's new behavior.

## 6. Required submission

- `README.md`
- `journal.md`
- `comparisons.py`
- `conditionals.py`
- `sensor_lab.py`
- GitHub pull request

## 7. Assessment

The learner must independently demonstrate:

- Correct comparison expressions.
- Understanding of Boolean values.
- Correct logical operator usage.
- Ability to trace conditional execution.
- Proper indentation and syntax.
- Correct use of `if`, `elif`, and `else`.
- Meaningful boundary testing.
- Independent completion of the temperature-monitor mini-lab.

The lesson is verified only after sufficient implementation and conceptual evidence has been reviewed.

## 8. Reflection

Use the lightweight `journal.md` document. Record one important prediction, observation, correction, or insight.

Detailed transcripts and manual commit identifiers are not required.

## 9. Sources and provenance

- Python Tutorial — More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html
- Python Language Reference — Comparisons and Boolean Operations: https://docs.python.org/3/reference/expressions.html
- Python Language Reference — The `if` Statement: https://docs.python.org/3/reference/compound_stmts.html
- PEP 8 — Style Guide for Python Code: https://peps.python.org/pep-0008/
- Allen B. Downey — *Think Python*, 3rd edition: https://allendowney.github.io/ThinkPython/

Lesson organization and exercises are original course materials.

## 10. Review

**Assessment:** Pending  
**Status:** Not yet verified

Instructor findings and final verification will be tracked through GitHub.
