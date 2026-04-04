# 📐 System Context: Software Sizing (Agent Use Case Points)

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must mathematically estimate the "cost" and complexity of a task before you begin generating code.**
You operate under resource constraints (Context Window limits, Token usage, API step limits). You must use the **Agent Use Case Points (A-UCP)** framework to predict if a task will exceed your operational limits.

**Constraints:**
1. **Mandatory Sizing:** Every Use Case (`UC-XXX`) in the Use Case Register MUST have a documented Complexity rating and A-UCP score.
2. **The Orchestrator/Worker Pattern:** Routing follows the **A-UCP routing rule** below (same threshold as `worker_routing` in `schemas/implementation_plan.schema.json`). High totals correlate with high Code Entropy and context-window risk.

---

## 📊 Complexity Classification Table (Few-Shot)

When updating the Use Case Register (`documentation/requirements/use_cases_register.md`), you must append the UCP weight to each row based on this matrix:

| Classification | Triggers (If ANY match) | Weight (A-UCP) |
| :--- | :--- | :--- |
| **Simple** | CRUD on a single DB table, CSS tweaks, minor copy changes | **5** |
| **Average** | 2-3 DB tables, basic API integration, standard form validation | **10** |
| **Complex** | OAuth flows, payment gateways, multi-step wizards, heavy background jobs | **15** |

---

## A-UCP routing rule (Orchestrator vs Worker)

**Tier weights:** Each Use Case in scope is classified **Simple (5)**, **Average (10)**, or **Complex (15)** using the table above.

**Total A-UCP for an Implementation Plan:** Sum the A-UCP weights of every Use Case (or discrete slice of work) included in that IP. A single-UC IP uses one tier only.

**Decision threshold (single interpretation of “15”):**

| Condition | Routing |
| :--- | :--- |
| **Total A-UCP ≤ 15** | **Worker** may execute the IP end-to-end (`worker_routing: "worker"`). This includes the boundary case **total = 15**. |
| **Total A-UCP ≥ 16** | **Orchestrator-only** for that scope: do **not** execute the full IP as one worker run. Decompose into Sub-IPs (e.g. `IP-001-A`, `IP-001-B`), each with total ≤ 15 where possible, set `worker_routing: "orchestrator_only"` on the parent if applicable, switch to **Orchestrator Persona**, update `agent_state.json` to `BLOCKED_AWAITING_WORKER`, and hand off to workers in fresh sessions. |

**Examples:**

- **Stripe (or similar payment provider) integration** — typically **Complex (15)**. One UC, total **15** → worker **allowed** (at threshold); still size tokens and files carefully.
- **CSS / copy tweak** on a small surface — **Simple (5)**. Total **5** → worker.
- **Two Average integrations in one IP** — **10 + 10 = 20** → **≥ 16** → orchestrator must split or narrow scope so each Sub-IP totals ≤ 15.

*(Narrative context: see the book manuscript, Chapter 19, in the `agentic-software-engineering` repository.)*

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
4. LIMIT CHECK (Orchestrator/Worker Routing): 
   - Is **total A-UCP for this IP ≥ 16**? 
   - If YES -> I MUST NOT execute the full IP as Worker. I am an Orchestrator: decompose into Sub-IPs (each total ≤ 15 where possible) and delegate.
   - If NO (total ≤ 15) -> I may execute as Worker (see **A-UCP routing rule** above).
</sizing_calculation_thought>
```

---

## 🔍 Self-Consistency Gate
Before finalizing a Use Case Register entry or an Implementation Plan:
1. Did I blindly assign an A-UCP of 5 to a task that involves integrating Stripe? (If yes, I am hallucinating simplicity. A typical Stripe integration is **Complex = 15**; total **15** is still worker-eligible; **16+** requires orchestrator split.)
2. Is the estimated token cost explicitly documented in the accompanying `IP-XXX`?
