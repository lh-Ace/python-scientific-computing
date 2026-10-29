# Scientific Validation Standard (Modules 03–13)

Use only the checks appropriate to the mathematics and implementation maturity; do not force advanced tests into beginner lessons.

## Validation checklist

1. **Problem and assumptions:** governing equations, domains, initial/boundary conditions, units, invariants, regularity assumptions, expected range and failure modes.
2. **Reference oracle:** exact/analytic result when available, independent derivation, manufactured solution, trusted library reference, or carefully justified invariant. A matching library output alone is not a proof.
3. **Discretization and error:** truncation and floating-point error; quantify residual, error norms and error propagation as appropriate. Distinguish local from global error and model error from implementation error.
4. **Conditioning versus stability:** distinguish sensitivity of the underlying problem from errors introduced or amplified by the algorithm.
5. **Convergence:** change mesh/step size or tolerance where appropriate; check observed rate rather than relying on one plot.
6. **Sensitivity and uncertainty:** perturb inputs/parameters or sample distributions when justified; explain limits of conclusions.
7. **Performance:** record environment, input sizes, warm-up and timing methodology, memory use and accuracy; never compare mismatched mathematical problems.
8. **Reproducibility:** pin dependency versions, seed stochastic experiments when necessary, document commands and data generation; retain source code for figures.
9. **Interpretation:** describe what is established, what is only observed, and what remains unverified.

## Domain-specific examples

| Module | Minimum domain-appropriate verification |
| --- | --- |
| 03 Numerical arrays | shape/type/stride/view tests, floating-point counterexamples, meaningful benchmark |
| 04 Visualization | faithful axis scales, units, data provenance, no misleading interpolation |
| 05 Linear algebra | residual, conditioning, stable-vs-naive solver comparison |
| 06 ODE | analytic/ref comparison, step refinement, global error, tolerance experiment |
| 07 PDE | boundary consistency, grid refinement, stability and conservation/invariant where applicable |
| 08 Statistics | simulation checks, uncertainty intervals, sampling and sensitivity |
| 09 Optimization | gradient check, objective change, stopping criteria, numerical stability |
| 10 ML | held-out evaluation, leakage guard, baseline, seed/configuration and uncertainty |
| 11 Performance/FFI | numerical equivalence + data ownership and transfer costs; benchmarks include overhead |
| 12–13 Engineering | regression tests, clear API contracts, reproducible scientific reports and limits |

## Cumulative teaching example: Newton's law of cooling

- **01:** arithmetic and loops, predict a discrete update; describe fixed step and stopping criterion.
- **02:** function/data contract, simple test cases, configurable parameters.
- **03–04:** array trajectories, numeric behavior and plot with labeled units.
- **06:** derive continuous model and analytic solution, implement/compare Euler and RK, convergence.
- **08–09:** parameter uncertainty, fitting/optimization or sensitivity, as justified.
- **11:** profile and optionally compare C++ kernel overhead against Python and NumPy.
- **12–13:** package only if it is chosen for an appropriate independent engineering deliverable.

A symbolic result does not automatically certify a numerical implementation; a numerical agreement does not certify the mathematical model. Explicitly state the kind of evidence obtained.


## Symbolic correctness and mathematical domains

Symbolic derivations provide valuable independent references but require checking assumptions. When relevant:

- State domains, branch conventions, parameter restrictions and initial/boundary conditions.
- Distinguish the exact solution of a discrete recurrence from that of a continuous ODE; they are not interchangeable.
- Use substitution/differentiation/residual checks for candidate exact solutions, and verify initial/boundary conditions separately.
- Test transformations that could be invalid outside stated domains; distinguish structural equality from mathematical equivalence.
- Compare symbolic expressions with numerical evaluations at valid sample points, without assuming numerical agreement alone proves symbolic identity.
- Explicitly document when closed-form expressions are unavailable, impractical or unreliable and a validated numerical method is preferable.

See `docs/SYMBOLIC_COMPUTING_ROADMAP.md` for the module placement and optional mini-CAS learning laboratory.
