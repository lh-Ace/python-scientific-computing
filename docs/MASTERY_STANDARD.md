# Mastery, Proficiency and Graduation Standard

**Status:** HQ amendment proposed 2026-10-29. This document supplements, rather than replaces, `docs/ASSESSMENT.md`.

## Vocabulary

- **Completed lesson:** assigned activities and evidence submitted; not automatic competency verification.
- **Verified lesson:** reviewer confirms the lesson-specific competencies.
- **Passed module (proficient):** summative assessment ≥80/100, all critical prerequisites demonstrated, and revisions resolved; may advance.
- **Mastery candidate:** ≥90/100 plus strong independent explanation and implementation, subject to transfer/retention.
- **Mastered module:** mastery candidate with a new-problem transfer check and retained skill confirmed later (ideally 2–6 weeks; later authentic module work counts).
- **Course graduate:** all Modules 01–13 passed, capstone independently defended, comprehensive unseen exam passed, and critical Python/numerical validation competencies verified.

## Preserve original 100-point rubric

| Dimension | Points | Primary evidence |
| --- | ---: | --- |
| Conceptual and mathematical understanding | 25 | explain semantics, assumptions, derivations and why alternatives differ |
| Independent program construction | 25 | implement from a new specification without copied solution |
| Correctness and testing | 20 | run checks, explain failures, choose meaningful tests and edge cases |
| Clarity and engineering | 15 | maintainability, structure, comments, constraints, documentation |
| Reflection and transfer | 15 | new-domain adaptation, tradeoffs, diagnosis, key learning correction |
| **Total** | **100** | |

Grading interpretation is unchanged: <70 targeted rebuild; 70–79 developing; **80–89 pass/proficient**; **90–100 mastery candidate**. A score alone never overrides a failed critical competency. The instructor should identify critical competencies **before** the assessment; do not retroactively invent gates.

## Five mastery dimensions

Each module chooses observable demonstrations covering:

1. **Conceptual:** explain expected semantics or mathematics without executing code.
2. **Implementation:** independently write correct code for an unseen, bounded requirement.
3. **Diagnostic:** inspect and correct unfamiliar faulty code, articulate root cause and verification.
4. **Transfer:** reuse concepts in a new setting, not a memorized copy of an exercise.
5. **Retention:** demonstrate the skill again after intervening lessons; authentic later work is preferred over repetitive exams.

The same task may evidence multiple dimensions. Do not create five separate assignments solely because there are five categories. Avoid treating a polished journal as more important than correct independent work.

## Module completion protocol

1. Module overview identifies prerequisites, 3–7 critical outcomes, exam scope, practical lab and references.
2. Lessons progressively reduce scaffolding; code is written by the learner; hints before full solutions.
3. Independent laboratory: novel bounded task, tests and brief engineering rationale.
4. Module examination: new problems involving reasoning, programming, debugging and explanation; no solution key in learner's main branch beforehand.
5. Reviewer records rubric, critical competencies, SHA/PR evidence, any required repair and next dependency unlocked.
6. On ≥80 with critical outcomes satisfied, mark module `Verified` in current status register. Record **proficiency** separately from **mastery**.
7. At ≥90, schedule a low-overhead transfer/retention check through subsequent real work; mastery may be confirmed without delaying advancement.

## Distinguish language mastery from domain specialization

- **Python foundations proficiency:** Modules 01 and core 02 demonstrate reliable Python programming, debugging and essential semantics.
- **Deep Python language mastery:** verified advanced language strand in 12 (data model, descriptors, inheritance, typing/protocols, concurrency/async, interpreter tradeoffs), a substantial general-purpose tool, unseen semantic/debugging challenge and retained transfer.
- **Scientific Python course graduation:** passed 01–13; scientific/numerical validation across 03–10; capstone and comprehensive examination. This does not require expertise in every PDE method, all neural architectures, all C++ tooling or proprietary MATLAB tools.

## Final graduation gate

All conditions required:

- Every module 01–12 is **passed** (≥80/100 with its critical competencies verified); Module 13 evidence completed.
- Independent capstone earns ≥90/100 **and** passes safety/correctness-critical checks appropriate to its domain. The project includes problem formulation; assumptions; design; implementation; tests; independent or analytical validation; error/uncertainty where relevant; benchmarking; reproducibility; documentation; technical defense.
- Separate **comprehensive unseen examination** earns ≥85/100 with no critical weakness in Python semantics, unfamiliar debugging, problem decomposition, scientific validity or explanation of limitations.
- Reviewer verifies at least one delayed transfer/retention demonstration covering Python foundations and at least one advanced scientific/software-engineering competence.
- Explicitly recorded evidence links to commits/PRs/tests; no automatic certification from hours logged or assignment counts.

If a requirement is not passed, revise the weak competency and reassess **that competency**, not the entire course by default. Passing this internal standard does not confer an accredited degree, professional license or external certificate.

## Evidence and low-overhead logging

Minimum for typical lesson: own code + test/observation + a short note (intent/prediction, what changed or surprised you, final understanding). Use commit messages/PR conversation instead of duplicate diaries. Module and capstone evidence may use fuller written technical reports when relevant. Do not modify historical grades based on this amendment.
