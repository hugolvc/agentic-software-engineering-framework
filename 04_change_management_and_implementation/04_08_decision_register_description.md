# 📖 System Context: Decision Register

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must maintain a master index of all Architectural and Technical Decisions (DECs).**
Creating a `DEC-XXX.md` file (as per the Decision Log Template) is not enough. You must register that file's existence in the `documentation/history/decision_register.md`.

**Constraints:**
1. **No Ghost Decisions:** If a DEC file exists in the directory but is not listed in this register, it is considered invalid and will be ignored during context retrieval.
2. **Immutable Links:** When you enter a decision into this register, you must link to the exact Functional Requirement (REQ-XXX) or Non-Functional Requirement (NFR-XXX) that prompted the decision.

---

## 🧠 Chain-of-Thought (CoT): Register Maintenance Sub-Routine
Whenever you create or modify a decision, run this thought process:

```text
<register_maintenance_thought>
1. DECISION CONFIRMATION: I just wrote `DEC-014_use_graphql.md`.
2. REGISTRATION: 
   - I must open `documentation/history/decision_register.md`.
   - I must append a new row to the "Architecture Decisions" table.
   - I must link DEC-014 to `NFR-PERF-002` (Payload Size Reduction).
3. DEPENDENCY CHECK: Does DEC-014 supersede an older decision (like `DEC-003_use_rest`)?
   - If YES -> I must go back to the row for DEC-003, change its status to `Superseded`, and note that DEC-014 replaces it.
</register_maintenance_thought>
```

---

## 📝 The Register Template (Required Format)
The central `decision_register.md` file MUST follow this exact, machine-readable markdown table format. Do not use complex nested tables.

# Decision Register
**Last Updated**: YYYY-MM-DD

## 1. Architecture & Technology Decisions
| ID | Title | Date | Status | Impetus (REQ/NFR) |
|---|---|---|---|---|
| DEC-001 | Use React Native | 2024-01-01 | Approved | NFR-PORT-001 |
| DEC-002 | Use PostgreSQL | 2024-01-02 | Approved | NFR-RELI-004 |
| DEC-014 | Migrate to GraphQL | 2024-04-15 | Proposed | NFR-PERF-002 |

## 2. Business Logic Decisions
| ID | Title | Date | Status | Impetus (REQ/NFR) |
|---|---|---|---|---|
| DEC-008 | Rounding Currency to 4 Decimals | 2024-02-10 | Approved | REQ-045 |

---

## 🔍 Self-Consistency Gate
Before calling it a day:
1. Did I create a DEC file but forget to add it to this Register table? 
2. If I changed a decision's status to "Rejected," did I update this table so future AIs don't accidentally implement it?
