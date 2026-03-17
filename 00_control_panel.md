# ASE Control Panel (Single Source of Tunable Parameters)

## 🤖 Core Directive (Zero-Shot)
**You must read this file when starting a session. These values override any defaults stated elsewhere in the methodology.**
If a project has its own `documentation/input/ase_control_panel.md`, that file overrides this one.

---

## Tunable Parameters

| Parameter | Default | Description | Your action |
|-----------|---------|-------------|-------------|
| `A_UCP_ORCHESTRATOR_THRESHOLD` | 15 | If Implementation Plan A-UCP exceeds this, switch to Orchestrator; do not code. | Use this number for Orchestrator/Worker split. |
| `CANARY_REFRESH_INTERVAL` | 10 | Re-read NFR register every N tool calls. | Output `<canary_summary>` at this interval. |
| `REQUIRE_IP_APPROVAL` | true | If true, after generating IP-XXX you MUST wait for explicit user approval before coding. | Do not run Execution phase until approval. |
| `APPROVAL_PHRASES` | "approved", "proceed", "go ahead", "execute" | User message containing one of these = approval. | Treat as approval to execute IP. |
| `STRICTNESS_LEVEL` | standard | Options: minimal \| standard \| strict. | minimal = skip optional CoT; standard = full CoT; strict = all gates + mandatory DEC for any dependency. |
| `BLOCKED_REASONS_CATALOG` | (see below) | Canonical list of block reasons. | When blocking, use exactly one reason ID + the escalation format. |

---

## BLOCKED_REASONS_CATALOG

When you must halt and escalate, use **exactly one** of these IDs. Do not invent new reasons.

- **`CONFLICTING_NFR`** — Detected conflicting NFRs (e.g., PostgreSQL required but NoSQL budget).
- **`MISSING_ACTOR_OR_UC`** — Required Actor or Use Case missing from registers.
- **`IP_EXECUTION_FAILED_3X`** — Execution of IP failed 3 consecutive times.
- **`AMBIGUOUS_REQUIREMENT`** — User intent cannot be resolved without clarification.

**Escalation format (mandatory):** *"I am BLOCKED because [Reason ID]: [Short explanation]. Option A is [X]. Option B is [Y]. How do you want to proceed?"*
