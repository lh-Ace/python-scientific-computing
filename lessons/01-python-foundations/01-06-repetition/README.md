# Lesson 01.06 — Repetition

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lessons 01.01–01.05  
**Environment:** Python, VS Code, uv

## 1. Why this lesson exists

Until now, repeated calculations have required manually repeating Python statements.

Loops allow programs to execute instructions repeatedly, using conditions or a predetermined sequence of values.

This capability forms a foundation for algorithms, scientific simulations, numerical iteration, data processing, and computational mathematics.

The objective is not merely to memorize loop syntax, but to understand how execution progresses, how state changes, and how repetition terminates.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Explain what iteration means.
2. Write `while` loops using Boolean conditions.
3. Explain how loop conditions are reevaluated.
4. Update variables within loops.
5. Identify and prevent accidental infinite loops.
6. Write `for` loops using `range()`.
7. Understand `range(start, stop, step)` and exclusive stopping bounds.
8. Predict iteration counts and identify off-by-one errors.
9. Use counters and accumulators.
10. Explain loop invariants and termination conditions at an introductory level.
11. Use `break` and `continue` appropriately.
12. Debug simple loop-related errors.
13. Construct an independent program performing repeated numerical updates.

## 3. Core concepts

### A — Introduction to while loops

A `while` statement repeats a block while its condition evaluates to true.

Example:

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

The condition is checked before each iteration.

The variable update ensures that the condition eventually becomes false.

Python uses indentation rather than C++-style braces to define the loop body.

### B — Progress and termination

A loop must have a clearly understood stopping behavior.

Investigate:

- Loop conditions
- State changes
- Termination conditions
- Infinite loops
- Boundary values
- Off-by-one errors

A useful question is: What changes during each iteration that allows the loop to terminate?

### C — for loops and range()

A `for` loop can iterate over values produced by `range()`.

Example:

```python
for step in range(3):
    print(step)
```

Study:

- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`
- Positive and negative steps
- Exclusive stopping boundaries
- Loop variables

Python's `for` iterates over values from an iterable. Unlike a traditional C++ `for` statement, its syntax does not contain separate initialization, condition, and update expressions.

### D — Counters and accumulators

A counter tracks how many times an event occurs.

An accumulator stores a running result, such as a sum or product.

Study:

- Initialization
- Updating within a loop
- Maintaining useful state
- Mathematical verification of a final result
- Avoiding accidental resets inside loops

### E — Loop control and debugging

Introduce:

- `break` — terminate a loop early
- `continue` — skip to the next iteration
- Incorrect indentation
- Missing updates
- Incorrect stopping conditions
- Off-by-one errors

Practice tracing loops by hand before execution.

### F — Independent mini-lab: Discrete cooling simulation

Create `iteration_lab.py`.

Model a simplified object cooling toward its surrounding temperature.

Use these initial values:

- Object temperature: 80°C
- Ambient temperature: 20°C
- Cooling fraction per step: 0.2
- Number of update steps: 6

At each step, update the temperature according to:

\[
T_{\text{new}}=T_{\text{old}}+0.2(T_{\text{ambient}}-T_{\text{old}})
\]

Requirements:

1. Store the initial temperature, ambient temperature, cooling fraction, and step count in variables.
2. Display the initial temperature.
3. Use a loop to perform exactly six updates.
4. Display the step number and updated temperature.
5. Format temperatures to two decimal places.
6. Verify that temperature moves toward ambient temperature.
7. Explain why the process terminates.
8. Test a different initial temperature.
9. Avoid manually copying the update statement six times.

This exercise is a discrete numerical model. Later modules will introduce differential equations, numerical integration, physical modeling assumptions, and error analysis.

## 4. Programming activities

**Activity A — Basic while loop**

File: `while_loops.py`

- Predict loop output.
- Write simple increasing and decreasing loops.
- Explain when conditions are evaluated.

**Activity B — Termination and boundaries**

File: `while_loops.py`

- Investigate stopping conditions.
- Identify off-by-one errors.
- Trace loop state.
- Explain the risk of infinite loops.

**Activity C — for and range()**

File: `for_loops.py`

- Write loops using different forms of `range()`.
- Investigate stopping boundaries and steps.
- Compare `while` and `for` for known iteration counts.

**Activity D — Counters and accumulators**

File: `for_loops.py`

- Count iterations.
- Calculate repeated sums and products.
- Verify results mathematically.

**Activity E — Debugging and loop control**

Files: `while_loops.py` and `for_loops.py`

- Correct a faulty loop.
- Experiment with `break` and `continue`.
- Explain their effects on execution.

**Activity F — Independent mini-lab**

File: `iteration_lab.py`

- Implement the cooling simulation independently.
- Compare predicted and observed outputs.
- Test a modified initial condition.
- Explain the mathematical update rule and loop termination.

## 5. Independent verification

For every programming activity:

1. Predict the output before running.
2. Write the code independently.
3. Execute the program.
4. Compare predictions with observations.
5. Explain errors, boundaries, and termination.

Run completed files from the repository root:

```bash
uv run python lessons/01-python-foundations/01-06-repetition/while_loops.py

uv run python lessons/01-python-foundations/01-06-repetition/for_loops.py

uv run python lessons/01-python-foundations/01-06-repetition/iteration_lab.py

uv run python -m unittest discover -s tests -v
```

Do not intentionally execute an infinite loop without understanding how to interrupt it.

## 6. Submission requirements

- `README.md`
- `journal.md`
- `while_loops.py`
- `for_loops.py`
- `iteration_lab.py`
- GitHub pull request containing independent work

## 7. Assessment

The learner must demonstrate:

- Correct use of `while` and `for`.
- Understanding of loop conditions and termination.
- Correct use of `range()`.
- Ability to predict iteration counts.
- Correct counter and accumulator patterns.
- Understanding of `break` and `continue`.
- Ability to identify off-by-one errors.
- Correct completion of the numerical iteration mini-lab.
- Clear reasoning and independent debugging.

Verification requires reviewed code and evidence of understanding.

## 8. Reflection

Use the lightweight `journal.md` template.

Record one meaningful prediction, observation, mistake, or discovery. Detailed exercise transcripts are not required.

## 9. Sources and provenance

- Python Tutorial — More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html
- Python Language Reference — Compound Statements: https://docs.python.org/3/reference/compound_stmts.html
- Python Documentation — Built-in range(): https://docs.python.org/3/library/stdtypes.html#ranges
- Allen B. Downey — Think Python, 3rd edition: https://allendowney.github.io/ThinkPython/

Lesson structure and exercises are original course materials.

## 10. Review

**Assessment:** Pending  
**Status:** Not yet verified

Instructor feedback and final verification will be tracked through GitHub.
