# Lesson 01.02 — Learning Journal

**Status:** In progress  
**Date of first attempt:** 2026-10-26  
**Relevant commit(s):** Not yet recorded  
**Python version:** [Record version used]

## 1. Initial understanding

Before beginning this lesson, what did I already know about Python expressions and arithmetic?

Similar to C++ in order

What did I expect the distinction between integers and floating-point values to be?

Integers is assumed and becomes floats if one is involved

## 2. Predictions and experiments

Preserve original predictions where available. Record actual results independently. Do not replace an incorrect prediction with the correct answer.

| Activity | Original prediction | Actual observation | Explanation / correction |
|---|---|---|---|
| A — Values and types | [Fill] | [Fill] | [Fill] |
| B1 — Arithmetic operators | [Fill] | [Fill] | [Fill] |
| B2 — Negative division | [Fill] | [Fill] | [Fill] |
| C1 — Operator precedence | [Fill] | [Fill] | [Fill] |
| C2 — Exponentiation | [Fill] | [Fill] | [Fill] |
| D1 — Floating-point precision | [Fill] | [Fill] | [Fill] |
| D2 — Binary representation | [Fill] | [Fill] | [Fill] |
| D3 — Evaluation order | [Fill] | [Fill] | [Fill] |
| E — Independent mini-lab | [Fill] | [Fill] | [Fill] |
| Final checkpoint | [Fill] | [Fill] | [Fill] |

## 3. Concepts I can explain independently

Explaining these in my own words, using examples when helpful.

**Integer (`int`):**

Whole numbers

**Floating-point number (`float`):**

Numbers including a decimal point

**The `type()` function:**

Returns the type assigned to the variable or expression

**Regular division versus floor division:**

Division includes the decimal/fraction value, floor division returns the closest whole number lower than the true value. The floor division floors the quotient

**Modulo and the division identity:**

Returns the remainder of the division

**Exponentiation:**

Takes the power of the right value of the left value

**Operator precedence:**

Parantheses, exponentiation, multiplication/division, addition/subtraction (PEMDAS)

**Associativity:**

[My explanation]

**Binary floating-point representation:**

[My explanation]

**Floating-point rounding error:**

The floating point will never be exact for most, so a small bit remains. Only for some (those that are squares of 2 such as 1/2, 1/4, and 1/8) are exact.

## 4. Mathematical and computational reasoning

### 4.1 Exact versus approximate values

Why can some fractions be represented exactly in binary while others cannot?

Because the fractions must consist of powers of 2.

### 4.2 Evaluation order

Why might two mathematically equivalent arithmetic expressions produce slightly different floating-point results?

Because of how the floating-point errors work or operate.

### 4.3 Types and arithmetic

Why can floor division return either an `int` or a `float`?

Because float takes priority. As long as an int option exists, a float option is automatically assumed. It allows int because it 'truncates' the decmial values to reach the lower number.

### 4.4 Correctness versus accuracy

Explain the difference between:

- Mathematical correctness
- Program correctness
- Numerical accuracy

You could be mathematically correct, but the compilation will make the program vary in correctness to a certain degree, and that is its numerical accuracy.

## 5. Mistakes and corrections

### Mistake 1

**What I originally believed:**

[Fill]

**Evidence that challenged my understanding:**

[Fill]

**What I understand now:**

[Fill]

### Mistake 2

**What I originally believed:**

[Fill]

**Evidence that challenged my understanding:**

[Fill]

**What I understand now:**

[Fill]

Add more entries if useful.

## 6. Independent mini-lab reflection

**Problem:** Divide 29 measurements into groups containing 6 measurements, then repeat the quotient and remainder calculations for -29.

**Approach I chose:**

First used floor, modulus, and used their properties to construct 29 (and -29) again.

**How I verified the results mathematically:**

Wrote them down.

**Did my program behave as expected?**

Yes.

**What would I improve?**

Nothing.

## 7. Remaining questions

Record concepts that remain confusing or deserve further investigation.

None currently

## 8. Final explanation in my own words

Without copying the README or instructor explanations, summarize what I learned about Python numerical values, arithmetic, types, and floating-point precision.

How they work, why they work, and all the operations

## 9. Execution evidence

**Program 1 command:**

```bash
uv run python lessons/01-python-foundations/01-02-values-and-arithmetic/values.py
```

**Actual result:**

[Record output, summary, or relevant terminal transcript]

**Program 2 command:**

```bash
uv run python lessons/01-python-foundations/01-02-values-and-arithmetic/arithmetic_check.py
```

**Actual result:**

[Record output]

**Automated test command:**

```bash
uv run python -m unittest discover -s tests -v
```

**Actual test result:**

1 test run, 1 passed — bootstrap test

## 10. Git and review evidence

**Branch:** lesson/01.02-values-and-arithmetic

**Relevant commits:**

[Add commit SHA(s)]

**Pull request:**

[Add URL after creating PR]

**Reviewer feedback:**

[Pending review]

**Corrections following review:**

[Pending]

**Final lesson status:** Not yet verified
