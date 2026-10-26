# How to study, submit, and preserve learning evidence

## The cycle for each lesson

1. **Before:** read prerequisites and predict what a code snippet does *before executing it*.
2. **Understand:** identify names, evaluation order, data types, why the syntax works, and the historical/design reasons when appropriate.
3. **Attempt:** write a solution without copying model solutions.
4. **Validate:** run the file, compare predicted and actual output, create meaningful edge cases.
5. **Explain:** document why the solution works and what assumptions were made.
6. **Review:** receive feedback; revise in a separate commit; preserve prior attempt history.
7. **Verify:** update the lesson status only with evidence and explicit review.

## Git convention

Use small commits with a topical prefix and lesson number:

```text
lesson(01.01): run first print and arithmetic program
exercise(01.01): experiment with expression output
fix(01.01): correct mistaken division prediction
docs(01.01): reflect on interpreter versus terminal
review(01.01): apply feedback and finalize explanations
course: revise source mapping and prerequisites
```

Commit bodies should answer **why** as well as what:

```text
exercise(01.02): compare integer and decimal division

Predicted identical results, then observed that / returns float.
Added a journal entry explaining the difference and a check.

Evidence: uv run python lessons/.../example.py
```

Never fabricate a date, review verdict, test result, or explanation. A correction is legitimate progress.

## Code comments

Explain non-obvious design intent, input constraints, units, edge cases, numerical assumptions, and reason for an implementation decision. Avoid comments that just repeat the source code. As a beginner, personal explanatory comments are welcome, even if obvious to an experienced programmer.

## Journal

Each lesson has a `journal.md`. Record: first prediction, trial, observation, mistakes, corrected explanation, relevant commands and outputs, questions, source notes, final takeaways. Use the templates for later lessons. Don't force polished summaries before experiments.

## Review and proficiency

A passed command alone isn't a demonstrated understanding. Review checks independent reasoning, clarity, correct code, correct edge cases, explanation, and ability to generalize. Reviewer feedback should be in a versioned `review.md` or a GitHub PR discussion and reflected into `docs/PROGRESS.md` after verification.

## Instructor assistance

Ask for hints before complete solutions when practicing. Full solutions can be supplied after an independent attempt or as explicit worked examples, but assessments must have identifiable independent work.
