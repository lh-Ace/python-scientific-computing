# Lesson 01.09 — Program Structure

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lessons 01.01–01.08  
**Environment:** Python, VS Code, uv

## 1. Purpose

Learn how to organize Python programs into multiple files, reuse functions through imports, and separate computational logic from program execution.

This lesson introduces the foundations of modular program design without requiring advanced packaging or object-oriented programming.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Explain what a Python module is.
2. Distinguish a source file, a module, and a running program.
3. Import functions defined in another Python file.
4. Access names through a module's namespace.
5. Use `import`, `from ... import`, and basic aliases.
6. Explain why imported modules execute top-level statements.
7. Understand normal import caching within one Python process.
8. Explain `__name__` and the `if __name__ == "__main__":` pattern.
9. Separate computation from output and execution control.
10. Identify common import mistakes and name collisions.
11. Organize a simple multi-file program.
12. Independently refactor a numerical simulation into reusable modules.

## 3. Activities

### A — Introduction to modules

Files: `measurement_tools.py`, `import_experiments.py`

- Create a reusable Python module.
- Import the module from another file.
- Observe top-level execution during import.
- Predict and verify execution order.

### B — Imports and namespaces

File: `import_experiments.py`

- Use qualified module names.
- Compare `import module` with `from module import name`.
- Introduce import aliases.
- Recognize name collisions.
- Explain why wildcard imports are generally discouraged.

### C — Script execution versus import

Files: `measurement_tools.py`, `import_experiments.py`

- Introduce the module attribute `__name__`.
- Compare running a file directly with importing it.
- Introduce `if __name__ == "__main__":`.
- Avoid unwanted execution when modules are imported.

### D — Program decomposition

- Separate reusable calculations from presentation.
- Assign responsibilities to individual files.
- Organize imports and execution entry points.
- Recognize unnecessary duplication.

### E — Debugging imports

- Investigate missing modules and unavailable names.
- Recognize incorrect module and function references.
- Examine common naming collisions.
- Understand the introductory role of module search paths.

### F — Independent mini-lab: Multi-file cooling experiment

Files: `cooling_model.py`, `run_cooling.py`

Refactor the numerical trajectory simulation from Lesson 01.08.

Requirements:

1. Define reusable numerical functions in `cooling_model.py`.
2. Import those functions into `run_cooling.py`.
3. Keep printing and experiment configuration separate from the reusable calculations.
4. Simulate cooling and warming using different initial temperatures.
5. Store and display the trajectories.
6. Verify results against previous lessons.
7. Test zero steps and zero cooling fraction.
8. Use an appropriate execution entry point.
9. Demonstrate that importing the computational module does not automatically run the experiment.
10. Explain the responsibility of each module.

## 4. Verification

Predict before executing, implement independently, inspect outputs, and explain unexpected behavior.

Run from the repository root:

```bash
uv run python lessons/01-python-foundations/01-09-program-structure/import_experiments.py

uv run python lessons/01-python-foundations/01-09-program-structure/run_cooling.py

uv run python -m unittest discover -s tests -v
```

## 5. Assessment

Verification requires:

- Correct module creation and imports.
- Understanding of module execution and namespaces.
- Correct use of an execution guard.
- Independent decomposition of a small program.
- Correct numerical results across imported functions.
- Meaningful debugging and testing.

Module-level proficiency and mastery follow the HQ standards.

## 6. Submission

- `README.md`
- `journal.md`
- `measurement_tools.py`
- `import_experiments.py`
- `cooling_model.py`
- `run_cooling.py`
- GitHub pull request

## 7. References

- Python Tutorial — Modules: https://docs.python.org/3/tutorial/modules.html
- Python Language Reference — Import System: https://docs.python.org/3/reference/import.html
- Python Documentation — `__main__`: https://docs.python.org/3/library/__main__.html
- Think Python, 3rd edition: https://allendowney.github.io/ThinkPython/
- Repository: `docs/MASTERY_STANDARD.md`

## 8. Review

**Assessment:** Pending  
**Status:** Not yet verified
