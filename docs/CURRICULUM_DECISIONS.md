# Architecture decisions and their rationale

## ADR-0001 — Curriculum-led progression
- **Decision:** Begin Python from zero and add applications only once prerequisite concepts are mastered.
- **Why:** A useful application is not sufficient justification to skip language or math foundations.
- **Consequence:** The PDE and machine-learning milestones stay in the plan but are not early assignments.

## ADR-0002 — Curated references rather than upstream git merges
- **Decision:** Link and map outside educational sources; keep course explanations, exercises, and code independently authored.
- **Why:** Attribution, differing licenses, outdated dependency locks, unnecessary histories, and overgrown repositories complicate genuine learning.
- **Consequence:** No third-party code in the starter scaffold. Introduce package-level implementation comparisons deliberately.

## ADR-0003 — Scripts before notebooks
- **Decision:** Start with `.py` files and a terminal. Introduce Jupyter only when the learner understands Python execution and imports.
- **Why:** Notebook execution order can hide state; scripts make input/output and execution order visible first.
- **Consequence:** Visualization and notebook work are not omitted—only correctly sequenced.

## ADR-0004 — Standard library before numerical libraries
- **Decision:** No NumPy/SciPy/PyTorch dependencies during Module 01.
- **Why:** Functions, objects, loops, containers, and errors are the conceptual prerequisites for understanding library APIs.
- **Consequence:** Initial environment is intentionally tiny.

## ADR-0005 — Lesson journals plus Git history
- **Decision:** Progress is evidenced through commits, lesson journals, reviewer notes, and explicit verification.
- **Why:** Code diffs show changes; journals capture how understanding changed.
- **Consequence:** Past attempts and mistakes are retained in history, not silently rewritten as if first-time correct.

## ADR-0006 — Machine-independent local setup
- **Decision:** `uv` with pinned CPython 3.13 and a course-owned `pyproject.toml`.
- **Why:** Stable learning runtime on macOS and Ubuntu with no changes to global Python.
- **Consequence:** Future updates to Python versions and library pins are explicit course decisions.

## ADR-0007 — Cross-language backdoors are advanced comparisons
- **Decision:** Preserve eventual C++/Python, Numba, Julia, Rust, and C# investigation, but add each only after Python and relevant computational background.
- **Why:** Backdoors teach alternative execution models and engineering tradeoffs, not shortcuts around fundamental learning.
