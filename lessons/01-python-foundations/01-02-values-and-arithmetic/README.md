# Lesson 01.02 — Values and Arithmetic

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lesson 01.01 — Running Python  
**Primary environment:** Python, VS Code, uv

## 1. Why this lesson exists

Before constructing larger programs, we must understand how Python represents numerical values and evaluates mathematical expressions.

Mathematical numbers and their computational representations are not always identical. Python distinguishes integer values from floating-point values, and the choice of numerical representation can influence calculations.

This lesson establishes the foundations required for later work involving variables, mathematical functions, algorithms, and scientific computing.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Explain the distinction between `int` and `float`.
2. Use `type()` to inspect numerical values.
3. Independently construct arithmetic expressions.
4. Explain `/`, `//`, `%`, and `**`.
5. Apply operator precedence and associativity correctly.
6. Distinguish unary negation from subtraction.
7. Verify the integer division identity.
8. Explain why some decimal fractions cannot be represented exactly in binary floating-point.
9. Recognize the effects of rounding and evaluation order.
10. Distinguish mathematical correctness, program correctness, and numerical accuracy.

## 3. Core concepts

### 3.1 Numerical values and types

- Integers: `int`
- Floating-point values: `float`
- Numerical literals
- Type inspection with `type()`
- Nested function calls

### 3.2 Arithmetic operators

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Regular division: `/`
- Floor division: `//`
- Modulo: `%`
- Exponentiation: `**`

### 3.3 Expression evaluation

- Operator precedence
- Parentheses and grouping
- Associativity
- Unary negation
- Evaluation order

### 3.4 Computational representation

- Finite numerical representations
- Exact integer arithmetic
- Binary floating-point
- Floating-point rounding
- Numerical error and accuracy
- Effects of different evaluation orders

## 4. Exercises

### Activity A — Values and types

Create `values.py`.

Investigate integer and floating-point literals using `print()` and `type()`.

Compare the numerical values and types of `7` and `7.0`.

### Activity B — Arithmetic operators

**B1 — Positive arithmetic**

Investigate regular division, floor division, modulo, and exponentiation. Inspect the types produced by division operations.

**B2 — Negative arithmetic**

Investigate negative dividends using `/`, `//`, and `%`.

Explain the mathematical relationship between quotient and remainder.

### Activity C — Operator precedence

**C1 — Evaluation order**

Experiment with expressions containing multiple arithmetic operators and parentheses.

**C2 — Exponentiation and negation**

Compare unary negation, exponentiation, and different forms of parenthesized expressions.

Explain precedence and associativity.

### Activity D — Floating-point representation

**D1 — Decimal precision**

Investigate `0.1 + 0.2` and related expressions.

**D2 — Binary representation**

Compare decimal fractions that have exact binary representations with those that do not.

**D3 — Evaluation order**

Investigate whether changing the grouping of floating-point additions changes the computed result.

### Activity E — Independent arithmetic mini-lab

Create `arithmetic_check.py`.

Given 29 measurements and groups of size 6:

1. Determine the number of complete groups.
2. Calculate the remainder.
3. Reconstruct the original total.
4. Inspect the type produced by regular division.
5. Repeat the quotient and remainder calculations for -29.
6. Verify the negative division identity.

Use only concepts taught through Lesson 01.02.

### Final conceptual checkpoint

Predict the values and types produced by:

- `12 / 6`
- `12 // 6`
- `12.0 // 6`
- `12.0 % 6`

Verify the predictions experimentally and explain the results.

## 5. Independent verification

From the repository root, execute:

```bash
uv run python lessons/01-python-foundations/01-02-values-and-arithmetic/values.py

uv run python lessons/01-python-foundations/01-02-values-and-arithmetic/arithmetic_check.py

uv run python -m unittest discover -s tests -v
```

Record actual output and errors in `journal.md`.

Automated checks supplement independent reasoning; they do not establish proficiency by themselves.

## 6. Required submission

- `README.md` — Lesson instructions
- `values.py` — Numerical experiments
- `arithmetic_check.py` — Independent arithmetic lab
- `journal.md` — Predictions, observations, corrections, and explanations
- Meaningful Git commit(s)
- GitHub pull request for review

## 7. Review requirements

The learner must demonstrate:

- Correct arithmetic and numerical types.
- Independent use of taught Python syntax.
- Correct explanation of floor division and modulo.
- Understanding of precedence and associativity.
- Awareness of floating-point limitations.
- Ability to explain and validate observed results.
- Accurate documentation of experiments and mistakes.

Lesson verification requires instructor review and sufficient evidence. Completion of code alone does not establish verification.

## 8. Sources and provenance

- Python Software Foundation — *Python Tutorial: An Informal Introduction to Python*, particularly numbers and calculations.  
  https://docs.python.org/3/tutorial/introduction.html

- Python Software Foundation — *Floating-Point Arithmetic: Issues and Limitations*.  
  https://docs.python.org/3/tutorial/floatingpoint.html

- Python Software Foundation — *Expressions*, language reference.  
  https://docs.python.org/3/reference/expressions.html

- Allen B. Downey — *Think Python*, 3rd edition, introductory material on values, expressions, and types.  
  https://allendowney.github.io/ThinkPython/

- Hans Fangohr — *Introduction to Python for Computational Science and Engineering*.  
  https://fangohr.github.io/introduction-to-python-for-computational-science-and-engineering/

The exercises and lesson organization are original course materials. References provide additional explanations and authoritative descriptions of language behavior.

## 9. Review record

**Reviewer:** Pending  
**Review date:** Pending  
**Commit SHA:** Pending  
**Findings:** Pending  
**Final status:** Not yet verified
