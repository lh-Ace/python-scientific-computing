# Symbolic Mathematics and Computational Algebra — Course Roadmap

**Date:** 2026-10-29  
**Status:** Proposed supplemental HQ amendment; no lesson status or existing module number is changed.  
**Scope:** Modules 02–13 and a separately unlocked optional Symbolic Computing Laboratory.

## Purpose and distinctions

Scientific Python must eventually support **three complementary modes**:

1. **Numerical:** compute approximations and report errors, conditioning and convergence.
2. **Symbolic:** represent and manipulate mathematical expressions, compute exact results *when possible*, and reason about assumptions and domains.
3. **Visual:** inspect, validate and communicate computed/derived results.

Exact/symbolic does **not** mean universally more accurate, faster, or automatically correct. Symbolic transformations can change domains or introduce extraneous branches; symbolic closed forms often do not exist. Some numerical results are validated to excellent accuracy. Using C++/Rust does not itself improve mathematical exactness: chosen arithmetic, assumptions and algorithms determine correctness, while native implementations may help memory management or performance.

## Progressive course mapping (preserve Module 01)

| Existing module | New symbolic competency, introduced only when ready | Required vs optional |
| --- | --- | --- |
| **01** | Keep the original cooling *numerical iteration*; students need no SymPy or symbolic programming | No changes |
| **02** | Recursion, object trees and representations; an accessible expression-tree example may introduce symbolic concepts without solving equations | Conceptual bridge |
| **03** | Contrast exact rational arithmetic (standard library `fractions`) with binary floating point; numerical representation and assumptions | Core comparison |
| **05** | Symbolic matrix examples: exact Gaussian elimination, determinants, characteristic polynomials and parameter-dependent matrices | Selected worked comparisons |
| **06** | **Primary formal entry**: symbols, expressions, substitution, algebraic simplification, symbolic differentiation/integration, first-order ODE solutions, residual checking, limitations | Core symbolic-vs-numerical comparison |
| **07** | Manufactured PDE test solutions, exact derivatives and symbolic operators, with domain and boundary assumptions checked | Core verification technique where applicable |
| **08** | Symbolic probability formulas/derivations if appropriate; uncertainty estimates still depend on the actual statistical assumptions | Targeted examples |
| **09** | Compare symbolic differentiation, automatic differentiation and finite differences; avoid treating AD as symbolic manipulation | Core differentiation comparison |
| **10** | Symbolic gradients for small models and tests; not a substitute for actual model generalization experiments | Optional small verification |
| **11** | Compare expression evaluation or generated functions in native C++ (core integration), Rust (optional after prerequisites), FFI/ownership/layout/performance; test numerical equivalence | Cross-language specialization |
| **12** | Build and test a **limited** original symbolic engine: immutable expression nodes, rules, substitutions, differentiation, restricted simplification, structural equality and explicit domains | Advanced choice of engineering lab, not a full CAS mandate |
| **13** | Optional capstone combining symbolic derivation, numerics, verification, and performance | Domain-dependent |

No existing module is renumbered. No self-built general-purpose CAS is required to pass Modules 05–07. Students must be capable of describing *why* a symbolic answer is valid (or conditional) and comparing it with numerical evidence when available.

## Cooling-model spiral

Let initial temperature be `T_0`, ambient `T_a`, per-step fraction `alpha`, and time step `h`.

**Discrete numerical recurrence**:

`T_(n+1) = T_n + alpha (T_a - T_n)`

For a fixed ambient and constant `alpha`, the exact solution of the **discrete recurrence** is:

`T_n = T_a + (T_0 - T_a) (1-alpha)^n`.

**Continuous Newton cooling model**:

`dT/dt = -k (T - T_a)` with fixed `k >= 0`, giving:

`T(t) = T_a + (T_0 - T_a) exp(-k t)`.

Forward Euler applied to the continuous ODE with step `h` has `alpha = k h`. The discrete exact expression is *not identical* to the continuous exact solution at finite `h`; compare under matching units, parameters and initial conditions. Study stability and error later, including the consequence of `kh` becoming large.

Suggested progression:

- **01:** Loop over the recurrence; predict, observe and explain.
- **02:** Generalize into functions; structure data cleanly.
- **05–06:** Derive the exact discrete and continuous forms; compare them and compute residuals.
- **06:** Create symbolic expressions with SymPy, simplify and verify; compare a reference numerical ODE solver.
- **07–09:** Study error, stability and derivative semantics where appropriate.
- **11–12:** Evaluate compiled numerical kernels and a small restricted expression engine as independently justified projects.

## Optional unlock: Symbolic Computing Laboratory

**Unlock:** after the relevant Module 06 symbolic foundation plus Module 02 recursion/object concepts; Module 09 is a prerequisite only for the autodiff-comparison extension. This laboratory is an independent specialization and does not block the normal scientific-computing sequence.

Proposed subchapters:

- **S1 — Expressions and trees:** literal vs symbolic values, ASTs, canonical forms, exact rational values, names, structural equality.
- **S2 — Transformations:** substitution, local rewrite rules, associativity, simplification, expansion, collection, restrictions and assumptions.
- **S3 — Symbolic calculus:** differentiation by sum/product/chain rules; selected integrals; residual verification against derived formulas.
- **S4 — Equations and linear algebra:** restricted polynomial solving, symbolic matrix operations and parameterized algebra.
- **S5 — Numerical bridge:** substitute numbers, generate numeric callables safely, measure precision/performance, and compare with SymPy/SciPy.
- **S6 — Engineering bridge:** optional C++/Rust kernels behind a Python API; document ownership, boundary design, equality tests and benchmark limitations.

The laboratory deliberately builds a **bounded mini-CAS**. It must document unsupported operations, invalid transformations and mathematical assumptions. It is not a promise to reproduce SymPy, Mathematica, or the full calculus platform.

### Independent verification for a mini-CAS

A credible final laboratory should:

- Represent a restricted documented grammar using immutable or well-controlled expression trees.
- Implement substitution and differentiation without simply delegating its core work to SymPy.
- Distinguish expression **structural equality** from mathematical equivalence.
- Maintain correct domains (e.g. avoid unsafe `sqrt(x*x) -> x` over arbitrary real `x`, and avoid `log(a*b) -> log(a)+log(b)` without assumptions).
- Compare to independently derived small cases and SymPy as an external oracle, including nontrivial and edge cases.
- Include unit tests, intentional failure tests, performance measurements where relevant, and design explanations.

## Future language connections

- **C++:** native storage for expression nodes, evaluation engines, library interfaces, compilation and ABI tradeoffs.
- **Rust:** ownership-safe representations, exhaustive pattern matching on expression variants, FFI boundary testing, possible bindings through PyO3.
- **Julia:** multiple dispatch, symbolic/numerical expression design and alternative differentiation workflows.
- **MATLAB:** symbolic-toolbox/engineering comparisons when legally and technically available; not a course dependency.

Each language retains its own later independent course. This Python course teaches enough interface design and computational-algebra ideas to make those transitions understandable.

## Suggested authoritative sources

- SymPy official solvers / solving ODEs: https://docs.sympy.org/latest/guides/solving/solve-ode.html
- SymPy basic operations and expression trees: https://docs.sympy.org/latest/tutorials/intro-tutorial/manipulation.html
- SymPy assumptions guide: https://docs.sympy.org/latest/guides/assumptions.html
- Python `fractions`: https://docs.python.org/3/library/fractions.html
- Python AST documentation: https://docs.python.org/3/library/ast.html
- Existing course resources: `docs/REFERENCE_MAP.md`, `docs/SCIENTIFIC_VALIDATION_STANDARD.md`.

**Governance:** This roadmap supplements `docs/HQ_AMENDMENT_2026-10-29.md`, `docs/SYLLABUS.md`, and `docs/MASTERY_STANDARD.md`. The authoritative progress register is `docs/PROGRESS.md`; no work is marked completed by adopting this document.
