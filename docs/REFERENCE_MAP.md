# Curated reference library — when and why each resource enters

**Do not clone, vendor, or copy entire upstream projects into this course.** These are linked references and inspirations for our own original lessons and exercises. Revisit licensing and source versions before adapting material. The reference is a teaching resource, not the authoritative implementation of our code.

| Resource | Link | Earliest module | Assimilated role |
| --- | --- | --- | --- |
| Think Python 3e, Allen Downey | https://github.com/AllenDowney/ThinkPython | 01 | First principles: expressions, variables, functions, conditionals, iteration |
| Python for Computational Science and Engineering, Hans Fangohr | https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering | 01 | Scientific context without assuming prior Python experience |
| Official Python Tutorial and language reference | https://docs.python.org/3/tutorial/ | 01 | Authoritative language behavior and standard library |
| Berkeley CS 61A | https://cs61a.org/fa26/ | 01–02 | Abstraction, function design, program structure, recursion |
| MIT Intro CS using Python | https://openlearning.mit.edu/courses-programs/mitx-courses/introduction-computer-science-and-programming-using-python | 01–02 | Problem set / examination design principles |
| Scientific Python Lectures | https://lectures.scientific-python.org/ | 03 | Scientific libraries, debugging, numerical ecosystem |
| From Python to NumPy, Nicolas Rougier | https://github.com/rougier/from-python-to-numpy | 03 | Vectorization reasoning and measurement |
| NumPy 100 exercises | https://github.com/rougier/numpy-100 | 03 | Independent array fluency exercises (original variants) |
| Python Data Science Handbook | https://github.com/jakevdp/PythonDataScienceHandbook | 03–04 | Reference notebooks for numerical and data workflows; account for vintage |
| Scientific Visualization: Python + Matplotlib | https://github.com/rougier/scientific-visualization-book | 04 | Scientific-quality figure design |
| Fundamentals of Numerical Computation (Python edition) | https://fncbook.com/python/ | 05–07 | Theory, stability, errors, numerical algorithms |
| fast.ai Computational Linear Algebra | https://github.com/fastai/numerical-linear-algebra | 05 | Matrix applications and applied demonstrations |
| SciPy docs/source | https://docs.scipy.org/doc/scipy/ ; https://github.com/scipy/scipy | 05–09 | Reference implementations and scientific verification |
| SymPy | https://docs.sympy.org/latest/ | 06+ | Symbolic checks when introduced |
| CFD Python, Barba Group | https://github.com/barbagroup/CFDPython | 07 | Progressively introducing PDE discretization |
| Finite Difference Computing with PDEs, Langtangen & Linge | https://link.springer.com/book/10.1007/978-3-319-55456-3 | 07 | Rigorous verified finite-difference methods |
| py-pde | https://github.com/zwicker-group/py-pde | 07 | Higher-level PDE workflows and design comparisons |
| FEniCSx / DOLFINx | https://github.com/FEniCS/dolfinx | 07+ | Finite elements and native integration |
| Think Stats 3e, Allen Downey | https://github.com/AllenDowney/ThinkStats | 08 | Data-backed statistical intuition and notebook exercises |
| JAX | https://github.com/jax-ml/jax | 09 | Autodiff and compilation concepts |
| scikit-learn | https://scikit-learn.org/stable/ | 10 | Model training and evaluation patterns |
| PyTorch tutorials | https://github.com/pytorch/tutorials | 10 | Neural network practice and autodiff |
| Numba examples | https://github.com/numba/numba-examples | 11 | Performance and JIT comparison |
| pybind11 / scikit-build-core example | https://github.com/pybind/scikit_build_example | 11 | Building a native C++ Python extension |
| PyO3 | https://github.com/PyO3/pyo3 | 11 (optional) | Rust interoperability contrast |
| MIT Computational Thinking (Julia) | https://github.com/mitmath/computational-thinking | 11+ (optional) | Cross-language pedagogical comparison, not Python instruction |

## How a reference becomes a lesson

1. Identify a **prerequisite concept** and why that source teaches it well.
2. Record URL, relevant section or chapter, retrieval date/version if material changes, and license/attribution conditions.
3. Explain the concept independently, referencing sources rather than copying protected prose.
4. Create new exercises calibrated to the learner's currently taught vocabulary and mathematical prerequisites.
5. Provide verification and a written explanation of the design tradeoffs.
6. Note significant source influence in the lesson's **Sources and provenance** section.

## Source audit to revisit

Some historical tutorials rely on older Python/library versions. The course targets CPython 3.13 initially and will run new implementations in its own environment rather than inheriting upstream old pinned dependencies. External source changes should trigger an explicit curriculum review, not an automatic silent rewrite.
