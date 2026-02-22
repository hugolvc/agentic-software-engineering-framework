# 📐 System Context: Software Sizing (Agent Use Case Points)

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must mathematically estimate the "cost" and complexity of a task before you begin generating code.**
You operate under resource constraints (Context Window limits, Token usage, API step limits). You must use the **Agent Use Case Points (A-UCP)** framework to predict if a task will exceed your operational limits.

**Constraints:**
1. **Mandatory Sizing:** Every Use Case (`UC-XXX`) in the Use Case Register MUST have a documented Complexity rating and A-UCP score.
2. **Entropy Correlation:** High A-UCP scores correlate with high Code Entropy. If your A-UCP calculation exceeds 15 for a single Implementation Plan, you must break the plan down into smaller, sequential steps.

---

## 🧠 Chain-of-Thought (CoT): Sizing Calculation Sub-Routine
When drafting an Implementation Plan (`IP-XXX`), execute this thought process to calculate the effort required:

```text
<sizing_calculation_thought>
1. USE CASE RETRIEVAL: Which `UC-XXX` does this Implementation Plan fulfill?
2. COMPLEXITY CLASSIFICATION:
   - Does it involve >7 files, complex error handling, or external APIs? -> COMPLEX (15 A-UCP)
   - Does it involve 4-7 files and standard logic? -> AVERAGE (10 A-UCP)
   - Does it involve <4 files and straightforward logic? -> SIMPLE (5 A-UCP)
3. RESOURCE ESTIMATION:
   - My Step Estimate: [A-UCP * 2] tool calls.
   - My Token Estimate: [Step Estimate * 2,500] tokens.
4. LIMIT CHECK: Does my Step Estimate exceed 30? If yes, this task is too large for a single session and MUST be chunked.
</sizing_calculation_thought>
```

---

## 📊 Complexity Classification Table (Few-Shot)

When updating the Use Case Register (`documentation/requirements/use_cases/use_cases_register.md`), you must append the UCP weight to each row based on this matrix:

| Classification | Triggers (If ANY match) | Weight (A-UCP) |
| :--- | :--- | :--- |
| **Simple** | CRUD on a single DB table, CSS tweaks, minor copy changes | **5** |
| **Average** | 2-3 DB tables, basic API integration, standard form validation | **10** |
| **Complex** | OAuth flows, payment gateways, multi-step wizards, heavy background jobs | **15** |

---

## 🔍 Self-Consistency Gate
Before finalizing a Use Case Register entry or an Implementation Plan:
1. Did I blindly assign an A-UCP of 5 to a task that involves integrating Stripe? (If yes, I am hallucinating simplicity. Integrate Stripe is Complex = 15).
2. Is the estimated token cost explicitly documented in the accompanying `IP-XXX`?
