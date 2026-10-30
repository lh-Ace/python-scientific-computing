# Lesson 01.07 — Functions

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lessons 01.01–01.06  
**Environment:** Python, VS Code, uv

## 1. Why this lesson exists

Previous programs performed calculations using sequential instructions, conditional statements, and loops.

Functions allow us to organize instructions into reusable computational operations.

This is the foundation of mathematical software: rather than writing the same calculation repeatedly, we define a computation and use it with different inputs.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Define and call functions using `def`.
2. Distinguish defining a function from executing its body.
3. Distinguish parameters from arguments.
4. Pass different values into the same function.
5. Explain the difference between `print()` and `return`.
6. Understand that a function without an explicit return value returns `None`.
7. Use returned values in expressions and assignments.
8. Understand local names and introductory variable scope.
9. Distinguish rebinding a parameter from changing a caller's variable.
10. Use positional, keyword, and basic default arguments.
11. Explain how `return` affects control flow.
12. Design small functions with clear input/output contracts.
13. Recognize and debug common function-related mistakes.
14. Refactor a previously written numerical simulation into reusable functions.

## 3. Core concepts

### A — Defining and calling functions

A function is created using `def`.

Example:

```python
def double(number):
    return number * 2

result = double(5)
print(result)
```

The function body executes when the function is called.

Study the distinction between a function definition, a function call, and the result of that call.

### B — Parameters and arguments

Parameters are names in a function definition.

Arguments are values or objects supplied when calling the function.

Study:

- Multiple parameters
- Positional arguments
- Keyword arguments
- Default parameter values
- Argument order and common call errors

### C — Returning results

A function can return a computed result using `return`.

A returned value can be stored, used in arithmetic, passed into another function, or displayed.

Compare:

- Printing a value
- Returning a value
- Returning early
- Implicitly returning `None`

### D — Local scope and object references

Investigate:

- Names created inside functions
- Local names versus caller names
- Parameter rebinding
- Read-only access to suitable outer-scope names
- Name resolution and `NameError`

Python passes object references into function calls. The consequences for mutation, aliasing, and identity are expanded in Module 02.

### E — Function design and debugging

Design functions around explicit computational responsibilities.

Consider:

- What inputs does the function expect?
- What result does it produce?
- Which assumptions must hold?
- Does it calculate a result or merely display information?
- Can it be tested independently?
- What behavior occurs at boundary inputs?

Introduce simple docstrings and common function errors.

### F — Independent mini-lab: Reusable cooling simulation

File: `cooling_functions.py`

Refactor the cooling simulation from Lesson 01.06 using reusable functions.

Requirements:

1. Define a function that calculates one temperature update.
2. Accept the current temperature, ambient temperature, and cooling fraction as inputs.
3. Return the updated temperature.
4. Define a second function that performs a specified number of update steps.
5. Use the single-step calculation inside the repeated simulation.
6. Return the final temperature.
7. Demonstrate the simulation using initial temperatures of 80°C and 10°C.
8. Verify the numerical results against Lesson 01.06.
9. Test zero steps and zero cooling fraction.
10. Explain the function inputs, outputs, assumptions, and termination behavior.

The implementation must be written independently, without copying a supplied complete solution.

## 4. Activities

**Activity A — Function definitions and calls**

File: `functions_basics.py`

Predict execution, define functions, call them, and inspect results.

**Activity B — Parameters and arguments**

File: `functions_basics.py`

Experiment with positional, keyword, and default arguments.

**Activity C — Return values**

File: `functions_basics.py`

Distinguish printing from returning, including `None` and early returns.

**Activity D — Scope and bindings**

File: `scope_experiments.py`

Trace local names, parameter assignments, and variable lookup.

**Activity E — Debugging and contracts**

Files: `functions_basics.py` and `scope_experiments.py`

Identify faulty calls, missing returns, and incorrect assumptions.

**Activity F — Independent cooling-function mini-lab**

File: `cooling_functions.py`

Refactor, validate, and explain the reusable numerical model.

## 5. Verification

For each activity:

1. Predict behavior before running.
2. Write the implementation independently.
3. Execute and inspect actual output.
4. Explain the result.
5. Test meaningful boundary cases.

Run completed scripts from the repository root:

```bash
uv run python lessons/01-python-foundations/01-07-functions/functions_basics.py
uv run python lessons/01-python-foundations/01-07-functions/scope_experiments.py
uv run python lessons/01-python-foundations/01-07-functions/cooling_functions.py
uv run python -m unittest discover -s tests -v
```

## 6. Assessment

The learner must independently demonstrate correct function definition and calling, parameter passing, result return, basic scope understanding, and reusable numerical computation.

Verification emphasizes understanding, implementation, debugging, and transfer to a new problem, consistent with the HQ Mastery Standard.

A successful GitHub merge alone does not establish module-level mastery.

## 7. Submission

- `README.md`
- `journal.md`
- `functions_basics.py`
- `scope_experiments.py`
- `cooling_functions.py`
- GitHub pull request

## 8. Sources and provenance

- Python Tutorial — Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Python Language Reference — Function Definitions: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
- Python Documentation — Naming and Binding: https://docs.python.org/3/reference/executionmodel.html
- *Think Python*, 3rd edition: https://allendowney.github.io/ThinkPython/
- Repository: `docs/MASTERY_STANDARD.md`
- Repository: `docs/SCIENTIFIC_VALIDATION_STANDARD.md`

## 9. Review

**Assessment:** Pending  
**Status:** Not yet verified
