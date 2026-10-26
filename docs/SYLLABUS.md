# Course syllabus — beginner to scientific-computing proficiency

## Design principles

1. **Begin at zero Python prerequisites.** Knowing mathematics or another language does not substitute for a principled Python introduction.
2. **Sequence by prerequisites.** No premature applications: ODEs, PDEs, and ML appear when the language, mathematical, and numerical prerequisites are taught.
3. **Derive, implement, test, explain.** An algorithm is mastered only when the learner understands its assumptions, writes it independently, validates it, and explains its behavior.
4. **First the language, then the library.** Begin in the standard library; later compare independent implementations with established libraries.
5. **Expose the machinery.** Examine language runtime, memory, build systems, native extensions, numerical stability, and computational tradeoffs at appropriate levels.
6. **Reproducible artifacts.** Every milestone produces versioned code, a journal, tests or independent evidence, and reviewed feedback.

## Stage I — Python and programming foundations

| Module | Ordered learning outcomes | First applied context | Exit evidence |
| --- | --- | --- | --- |
| 01 Python foundations | programs, expressions, names, types, branching, loops, functions, collections, files, exceptions, elementary program design | arithmetic, coordinate tables, and simple mathematical rules | independent programs and explanatory oral/written check |
| 02 Internals and engineering | modules, scope, objects, iteration, types, testing, debugging, imports, environments, packaging, CPython, Git, basic complexity | reusable plain-Python arithmetic tools | documented small Python package and tests |
| 03 NumPy and numerical representation | arrays, dtypes, shape, indexing, broadcasting, views/copies, memory, vectorization, floating point, conditioning basics | arrays and tabular numerical experiments | independently implemented and benchmarked array operations |

## Stage II — Numerical and mathematical computation

| Module | Ordered learning outcomes | Applications only when ready | Exit evidence |
| --- | --- | --- | --- |
| 04 Visualization | Matplotlib, axes, dimension, data transformations, effective figures, 3D plots, uncertainty visualization | mathematical functions, vector fields, scientific figures | figure portfolio with source files and design notes |
| 05 Numerical linear algebra | linear systems, norms, matrix decompositions, eigenproblems, sparse systems, conditioning, iterative methods | linear system solver and diagnostics | comparison with established linear algebra routines |
| 06 Numerical calculus and ODE | derivatives, quadrature, interpolation, roots, Euler/RK, adaptive steps, stiffness, error estimation | ODE solver | test convergence against analytical and reference solutions |
| 07 PDE and simulation | classifications, initial/boundary conditions, discretization, finite difference, stability, convergence, FEM introduction | heat/wave/Laplace solvers | verified PDE solver with convergence study |
| 08 Statistics and probability | simulation, distributions, estimation, inference, regression, Bayesian reasoning, uncertainty | statistical simulation and analysis | reproducible research-style notebook/report |

## Stage III — Optimization, machine learning, systems

| Module | Outcomes | Exit evidence |
| --- | --- | --- |
| 09 Optimization and automatic differentiation | gradient methods, constraints, computational graphs, numerical vs automatic differentiation | from-scratch optimizer and gradient checks |
| 10 Machine learning | model design/evaluation, bias/variance, train-test leakage, regression/classification, neural networks, backpropagation, PyTorch | well-evaluated independent model study |
| 11 Performance and interoperability | profiling, compiled scientific libraries, Numba, C++/pybind11, build/linking, data crossing boundaries, concurrency, GPU introduction, optional Julia/Rust/C# comparison | correctness-preserving benchmarking and Python/C++ extension |

## Stage IV — Independent engineering

| Module | Outcomes | Exit evidence |
| --- | --- | --- |
| 12 Scientific software design | clean APIs, tests, documentation, CI, reproducibility, error handling, packaging, audits | maintainable numerical software artifact |
| 13 Capstone | mathematically justified design, implementation, scientific comparison, visualization, performance, written defense | independently reviewed capstone |

## Sequence, not scheduling pressure

No fixed weekly pace is assumed. Modules contain multiple numbered lessons; assessment gates and evidence govern advancement. A learner may read ahead but cannot claim proficiency before completing prerequisite checks. Integrations with other projects are *optional transfer exercises after concept mastery*, never a reason to skip the progression.

## Lesson standard

A substantive lesson covers: learning objective → prerequisite check → explanation and origin → worked small example → independent tasks → debugging and tests → reflection → cited sources → extension **only when prerequisites permit**. `templates/LESSON_TEMPLATE.md` standardizes the format.

## Independent proficiency

Aim for correct solutions, mathematical explanation, tests, and the ability to modify problems without repeating memorized recipes. The repository is an educational portfolio, not an accredited degree or certificate.
