# HQ Amendment — Mastery & Research Engineering

**Date:** 2026-10-29  
**Scope:** `python-scientific-computing`  
**Status:** Prepared for review; not yet merged into GitHub  
**Authority:** Supplemental specification; existing syllabus and completed coursework retain their identities.

## Non-negotiable preservation rules

- Preserve Modules **01–13**, all existing lesson numbers, code, exercises, project deliverables, journals, PRs, and reviews.
- Preserve curriculum-first teaching, first-principles explanations, independent code writing, prerequisite ordering, and finite completion standards.
- Do not backfill, regrade, or overwrite progress merely because this amendment exists. No changes to learner work or `docs/PROGRESS.md` without a real verification event.
- External repositories and books remain **references**, not source-code merges.
- Additional depth should be introduced when prerequisites are established, never as a surprise in Module 01.

## Audit of original syllabus

| Capability | Existing status | Decision |
| --- | --- | --- |
| Beginner Python, control flow, functions, collections, files | Explicit in Module 01 | Keep 01.01–01.12 intact |
| Python imports, packages, CPython and basic object semantics | Explicit in Module 02 but broad | Expand and assess |
| Decorators, descriptors, metaclasses, advanced typing | Not explicitly allocated | Depth progression in 02 and 12 |
| General-purpose Python, automation, CLI, everyday tools | Not a dedicated pathway | Standard-library tasks in 02, integrative independent project in 12; elective after 02 |
| Numerics, arrays and performance | Explicit in 03, 05–07, 11 | Add a consistent scientific validation protocol |
| LA–ODE–PDE connections | Present sequentially | Treat 05–07 as one mathematical spine without renumbering |
| Statistics, optimization and ML | Explicit in 08–10 | Tighten experimental-design gates; deep ML optional separate course |
| C++ interop | Explicit in 11 | Add ABI/API/data movement/ownership/FFI and numerical equivalence |
| Rust, Julia, MATLAB | Rust/Julia optional, MATLAB absent | Comparative introductions and optional interop; full language courses separate |
| Software engineering, unfamiliar code review | Partially in 02 and 12 | Escalating independence and maintenance tasks |
| Capstone | Explicit in 13 | Add separate comprehensive unfamiliar-problem examination |
| Mastery, retention and certification | Existing 100-point rubric | Preserve scores; add mastery gate and deferred evidence |

## Revised module-level specification (no renumbering)

| Module | Existing scope retained | Clarified advanced content / exit evidence |
| --- | --- | --- |
| **01 — Python foundations** | All 12 existing lessons and beginner mini-lab/exam | No new topics required. Pass independently with control flow, functions, collections, error reading and small programs. |
| **02 — Internals & engineering** | Modules, scope, objects, iteration, imports, packages, testing, CPython and basic complexity | **Core:** reference and identity semantics, mutation/aliasing, closures, first-class functions, recursion, iterators/generators, class basics, exceptions/context managers, core special methods, standard-library filesystem/CLI tasks, environments and tests. **Depth later:** descriptors/metaclasses, advanced typing and introspection reserved for 12. Exit: small package, tests, unfamiliar-bug diagnosis. |
| **03 — NumPy & numerical representation** | NumPy and array programming | dtypes, shape/strides, vectorization vs Python loops, views/copies, floating point, baseline error budgets, reproducible benchmark; exit: reason about array memory and justify accuracy/performance, not only API usage. |
| **04 — Scientific visualization** | Matplotlib and scientific figures | correct units/axes, sampling, uncertainty, readable annotations, provenance, reproducible source; exit: curated scientific figure portfolio defended against misleading presentation. |
| **05 — Numerical linear algebra** | linear systems, decompositions, sparse, eigen/iterative methods | residual vs forward error, backward error, conditioning, stability; exit: validated linear algebra solver and comparative diagnostic study. |
| **06 — Numerical calculus & ODEs** | differentiation, integration, roots, Euler/RK, adaptive, stiff systems | compare exact/reference/symbolic solutions when available; verify convergence order, tolerances, sensitivity and solver failure; exit: independent ODE solver with error study. |
| **07 — PDEs & scientific simulation** | finite difference, heat/wave/Laplace, boundary conditions, FEM introduction | matrix operators from 05, time integration from 06, stability/convergence studies, manufactured or independently checked solutions; exit: PDE simulation with grid-convergence and physical/mathematical validity arguments. |
| **08 — Statistics & probability** | distributions, simulation, estimation, inference, regression, Bayesian reasoning | uncertainty quantification, experiment design, reproducible random streams, sensitivity, valid interpretation; exit: defensible independent statistical study. |
| **09 — Optimization & autodiff** | gradient methods, constraints, computational graphs | numerical versus automatic/symbolic differentiation, finite-difference checks, conditioning, objective validation, stopping rules; exit: independent optimizer with gradient verification. |
| **10 — Machine learning** | classical ML, model evaluation, introductory neural networks | leakage prevention, baselines, generalization/uncertainty, controlled comparisons, model cards; exit: independent study including an implemented algorithm and defended results. Advanced DL is a separate future specialization. |
| **11 — Performance & interoperability** | profiling, Numba, C++ bindings, native builds, concurrency, GPU introduction | CPU/GPU tradeoffs, GIL/free-threading version distinctions, thread/process/async roles, FFI, ownership, array exchange, build/link, cross-language numerical consistency; targeted Rust, Julia, MATLAB comparisons (optional tool availability, especially MATLAB). Exit: correctness-preserving Python/C++ extension and benchmark; alternative when native environment unavailable must still demonstrate concepts. |
| **12 — Scientific software design & advanced Python** | package/API design, testing, CI, reliability, maintenance | advanced data model (descriptors, metaclasses, protocols), type annotations/generics, inheritance/composition tradeoffs, context managers, concurrency/async, profiling, standard-library general-purpose program design, unfamiliar-code review and refactor; exit: maintainable package plus independent general-purpose Python tool and language-depth examination. |
| **13 — Capstone & comprehensive assessment** | independent substantial scientific software project | independent specification, math assumptions, architecture, verification, error/performance analysis, experiments, documentation, defense **plus separate** unseen debugging, language-semantics and fresh-design examination. |

## Symbolic mathematics — third computational pillar

Supplementary roadmap: [`SYMBOLIC_COMPUTING_ROADMAP.md`](SYMBOLIC_COMPUTING_ROADMAP.md). Numerical methods, symbolic mathematics, and visualization are complementary rather than competing approaches. Introduce symbolic representations and exact-vs-approximate comparisons progressively; Module 06 is the principal formal symbolic entry, and a bounded mini-CAS is an optional post-prerequisite laboratory. C++/Rust interoperability can later evaluate/compile symbolic expressions but does not automatically make an algorithm exact or correct. Do not change Module 01 or make a complete computer algebra system a graduation prerequisite.

## Mathematical spine: Modules 05–07

Keep existing numeric order. Teach explicit cross-connections:

1. Linear algebra supplies vector spaces, matrix solvers, norms, sparse operators, eigenvalues and conditioning.
2. ODE algorithms supply temporal evolution, local/global error ideas, adaptive integration and stability reasoning.
3. PDE discretization often produces linear systems and semi-discrete ODE systems. Show how spatial discretization, time stepping and boundary conditions interact.
4. Reuse one cumulative mathematical model **only** when its prerequisites are taught: arithmetic and loops → pure-Python cooling iteration → function-based model → Euler/RK integration → analytic/SymPy comparison → error and convergence study → profiling → optional native implementation.

## General-purpose Python and future language network

- General Python is a first-class competency, not just a side benefit of numerical work. **Module 02** introduces standard-library tasks; an optional applied path can open after the core of 02; **Module 12** verifies independent general-purpose software construction.
- **C++ refresh/verification:** future independent course, with prior C++ evidence tested rather than assumed. Module 11 explores Python/C++ integration, not complete C++ mastery.
- **Rust:** future independent systems language course; 11 may contrast PyO3 ownership and FFI without teaching Rust from scratch.
- **Julia:** future independent scientific language course; compare JIT/specialization and numerical implementation choices after NumPy and numerical methods.
- **MATLAB/Simulink:** optional engineering workflow comparison; licenses, product availability, platform and release compatibility must be checked. No proprietary dependency for Python certification.
- **Deep learning:** Module 10 provides foundations; a separate advanced deep-learning pathway can branch after the requisite mathematics/ML, and later intersect with native systems engineering.
- Every cross-language connection has its own assessable competencies (correctness, representation, ownership, boundary and benchmark). Do not mistake knowledge of two languages for proof of interoperable engineering skill.

## Module dependencies and parallelism

- Mandatory language progression: `01 -> 02 (core) -> 03`; Modules 04 and 05 follow relevant NumPy basics.
- Mathematical spine: `03 + 05 -> 06 -> 07` (include visualizations from 04 as suitable); 05 is a mathematical prerequisite for later numerical material, but earlier ODE concepts may be introduced when independently justified.
- Statistical/ML spine: `03 + 08 + numerical LA -> 09/10` with exact learning prerequisites checked before exercises; Module 10 advanced neural work follows 09.
- Performance: `02 + 03 -> 11` foundation, with numerical examples introduced after the corresponding mathematics; placement remains Module 11 in the numbered course.
- Independent engineering: `02 + sufficient practice in 03–11 -> 12`; 13 after verified prerequisites in 01–12.
- Optional general-Python studio may open after 02 core; optional Julia/Rust/C++/MATLAB standalone courses belong outside this repo.
- Completing one module does not require all its optional specialist branches. A passing prerequisite check can allow learning a later concept; module numbers are stable curriculum containers, not artificial weekly deadlines.

## Increasing learner independence

| Stage | Instructor role | Learner responsibility |
| --- | --- | --- |
| 01–02 | Explainer and exercise coach | Predictions, own code, simple tests and corrections |
| 03–07 | Algorithmic reviewer | Derivations, code design, error studies, documented validation |
| 08–11 | Examiner and technical collaborator | Experimental decisions, unfamiliar source reading, evidence-based comparison |
| 12–13 | Reviewer / research mentor | Own specifications, architecture, implementation, debugging and defense |

Keep journal overhead to three meaningful items when sufficient: **prediction/intent, key observation or mistake, final reasoning/evidence**. Git history and PR discussion carry the rest.

## Certification

Refer to `docs/MASTERY_STANDARD.md`. Finite course completion requires all 13 modules passed, an independently defended capstone, and a separate comprehensive exam; deeper Python-language mastery is confirmed through advanced language and retained-skill evidence. This is a course-internal educational certification, not accreditation or a professional license.

## Adoption sequence

**Immediate:** Register amendment and mastery standard; align syllabus cross-links; preserve active Module 01 exercises and PRs; no new Module 01 lessons required.  
**At Module 02 design:** Plan core object semantics, recursion, classes, standard-library applications and the advanced-language bridge.  
**At Modules 03–10:** Implement shared numerical validation standards incrementally.  
**At Modules 11–12:** Introduce interoperability, advanced language depth, comprehensive codebase audit and maintenance labs.  
**At Module 13:** Define unseen examination and final defense independent from the capstone implementation.

## Source and provenance notes

Original repository: `docs/SYLLABUS.md`, `docs/ASSESSMENT.md`, `docs/LEARNING_PROTOCOL.md`, `docs/CURRICULUM_DECISIONS.md`, `docs/REFERENCE_MAP.md` (read 2026-10-29). This amendment was drafted from the user's HQ request and extends rather than supersedes those materials.

Official technical anchors (verify language/runtime versions when lessons are authored):
- Python 3.13 Data Model: https://docs.python.org/3.13/reference/datamodel.html
- Python 3.13 `typing`: https://docs.python.org/3.13/library/typing.html
- Python 3.13 `asyncio`: https://docs.python.org/3.13/library/asyncio.html
- SciPy `solve_ivp`: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html
- MATLAB Engine API for Python: https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html
