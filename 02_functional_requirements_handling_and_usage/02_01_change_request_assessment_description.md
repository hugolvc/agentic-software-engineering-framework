# 🔍 System Context: Change Request Assessment (Functional)

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must evaluate every Change Requirement (CR) for its functional impact before proposing an Implementation Plan (IP).**
A functional change modifies *what* the system does (business logic, features, actors, use cases). You are strictly prohibited from implementing functional changes without tracing their impact on the foundational requirement registers.

---

## 🧠 Chain-of-Thought (CoT): Functional Assessment Sub-Routine
Whenever you identify that a requested change has functional implications (as per `01_02_process_description.md`), you must execute the following `<functional_assessment_thought>` block before creating the Implementation Plan:

```text
<functional_assessment_thought>
1. ACTOR IMPACT: Does this change introduce a new user role/system, or modify what an existing role can do?
   - If YES -> I must update `documentation/requirements/actors_register.md`.
2. USE CASE IMPACT: Does this change alter an existing use case flow (UC-XXX) or require a new one?
   - If YES -> I must update `documentation/requirements/use_cases_register.md`.
3. REQUIREMENT IMPACT: Does this change add, modify, or deprecate a specific functional requirement (REQ-XXX)?
   - If YES -> I must update `documentation/requirements/functional_requirements_register.md`.
</functional_assessment_thought>
```

---

## 🔍 Self-Consistency Gate
Before finalizing your Implementation Plan, verify your own logic:
> *If I determined in my `<functional_assessment_thought>` that an Actor or Use Case is impacted, did I explicitly include the steps to update those specific registers in my Implementation Plan?*

If the answer is no, you must revise the Implementation Plan to include document updates alongside the code changes.