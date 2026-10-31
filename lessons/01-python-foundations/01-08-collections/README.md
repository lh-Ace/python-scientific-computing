# Lesson 01.08 — Collections

**Status:** In progress  
**Module:** 01 — Python Foundations  
**Prerequisites:** Lessons 01.01–01.07

## 1. Purpose

Learn how Python represents and processes groups of values using lists, tuples, dictionaries, and sets.

Collections enable programs to organize measurements, retain simulation trajectories, represent structured records, and process data without manually assigning separate names to every observation.

## 2. Learning objectives

By the end of this lesson, the learner should be able to:

1. Create and access lists.
2. Understand zero-based and negative indexing.
3. Use `len()`, indexing, slicing, assignment, and common list methods.
4. Distinguish mutable and immutable collections.
5. Create and use tuples.
6. Create dictionaries and retrieve values by key.
7. Add, update, and remove basic dictionary entries.
8. Create sets and explain uniqueness and membership.
9. Use `in` and `not in` appropriately.
10. Iterate over collections using `for`.
11. Build simple collection-based counters and accumulators.
12. Identify indexing, key-lookup, and mutation errors.
13. Explain introductory aliasing behavior without requiring advanced object-model knowledge.
14. Independently implement a program that records and analyzes a numerical trajectory.

## 3. Core concepts

### A — Lists

File: `collections_basics.py`

- List literals and elements
- Zero-based indexing
- Negative indexing
- `len()`
- Appending and replacing values
- Basic slicing
- Index errors
- Iteration

### B — Mutability and tuples

File: `collections_basics.py`

- Mutable lists
- Immutable tuples
- Tuple creation and indexing
- Choosing an appropriate representation
- Introductory object-sharing and reassignment examples

Detailed reference semantics and identity belong to Module 02.

### C — Dictionaries

File: `collection_operations.py`

- Key-value associations
- Creating and updating records
- Accessing values by key
- Membership checks
- Iterating through dictionary data
- Missing keys and basic error prevention

### D — Sets

File: `collection_operations.py`

- Unique elements
- Membership testing
- Adding and removing values
- Elementary union, intersection, and difference
- Unordered collections
- Suitable use cases and limitations

### E — Processing collections

Files: `collections_basics.py` and `collection_operations.py`

- Looping over values
- Counters and accumulators
- Finding simple summaries
- Empty collections
- Basic search and filtering
- Debugging indexing and mutation mistakes

### F — Independent numerical trajectory mini-lab

File: `trajectory_lab.py`

Extend the cooling simulation developed in Lessons 01.06 and 01.07.

Requirements:

1. Use reusable functions.
2. Store the initial temperature and every successive temperature.
3. Return the trajectory as a list.
4. Include the initial value at index zero.
5. Calculate simple numerical summaries from the recorded values.
6. Test both cooling and warming trajectories.
7. Verify the expected number of stored observations.
8. Handle zero steps correctly.
9. Compare selected values with earlier lesson results.
10. Explain the resulting data structure and basic assumptions.

## 4. Independent verification

For each activity:

1. Predict behavior before execution.
2. Implement independently.
3. Run the program.
4. Compare actual and expected results.
5. Test appropriate boundaries.
6. Explain errors and corrections.

Run completed scripts from the repository root:

```bash
uv run python lessons/01-python-foundations/01-08-collections/collections_basics.py
uv run python lessons/01-python-foundations/01-08-collections/collection_operations.py
uv run python lessons/01-python-foundations/01-08-collections/trajectory_lab.py
uv run python -m unittest discover -s tests -v
```

## 5. Assessment

Verification requires demonstrated understanding of collection access, mutation, iteration, appropriate data-structure selection, basic debugging, and independent implementation of the numerical trajectory mini-lab.

## 6. Submission

- `README.md`
- `journal.md`
- `collections_basics.py`
- `collection_operations.py`
- `trajectory_lab.py`
- GitHub pull request

## 7. References

- Python Tutorial — Data Structures: https://docs.python.org/3/tutorial/datastructures.html
- Python Documentation — Built-in Types: https://docs.python.org/3/library/stdtypes.html
- Think Python, 3rd edition: https://allendowney.github.io/ThinkPython/
- Repository: `docs/MASTERY_STANDARD.md`

## 8. Review

**Assessment:** Pending  
**Status:** Not yet verified
