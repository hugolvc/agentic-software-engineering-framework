# 🔗 System Context: Traceability Guide

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must maintain a mathematically unbroken chain of references from User Need → Code Component.**
You are strictly prohibited from generating "orphaned" code. Every class, module, and feature you build must be traceable back to a specific Implementation Plan (IP), which links to a Change Requirement (CR), which fulfills a Functional Requirement (REQ).

**Constraints:**
1. **Mandatory Updates:** Every time you generate an `IP-XXX` document, you MUST simultaneously append a new row to `documentation/history/traceability_matrix.md`.
2. **Bidirectional Linking:** In your source code docstrings, you must cite the `IP-XXX` that authorized the file's creation or modification.

---

## 🧠 Chain-of-Thought (CoT): Traceability Validation Sub-Routine
When proposing a new feature or writing code, execute this validation thought process:

```text
<traceability_validation_thought>
1. ORPHAN CHECK: I am about to write `PaymentGateway.ts`. Why am I writing this?
   - Is it authorized by an `IP-XXX`? Yes, IP-042.
   - Does IP-042 link to a valid `CR-XXX`? Yes, CR-015.
   - Does CR-015 link to a valid Requirement (`REQ-XXX`)? Yes, REQ-099 (Process Payments).
2. TRACEABILITY MATRIX UPDATE: I must open `traceability_matrix.md` and ensure a row exists that maps `REQ-099 -> CR-015 -> IP-042 -> PaymentGateway.ts`.
3. SOURCE CODE LINKING: I must add `Authorized by IP-042` to the top of `PaymentGateway.ts`.
</traceability_validation_thought>
```

---

## 📝 The Traceability Matrix (Required Format)
The central `documentation/history/traceability_matrix.md` file MUST follow this exact, machine-readable format. Do not use complex nested tables.

### 1. Requirements to Implementation
| Requirement ID | Type (Functional/NFR) | Change Req ID | Implementation Plan ID | Target Components |
|---|---|---|---|---|
| REQ-005 | Functional | CR-002 | IP-003 | `src/auth/LoginView.tsx`, `src/auth/AuthService.ts` |
| NFR-001 | Non-Functional | CR-002 | IP-003 | `src/auth/AuthService.ts` (Hashing logic) |

### 2. Actors to Use Cases
| Actor ID | Actor Name | Associated Use Cases (UC-XXX) |
|---|---|---|
| ACT-001 | System Administrator | UC-001, UC-005, UC-012 |

---

## 🔍 Self-Consistency Gate
Before finalizing any pull request or task resolution:
1. Did I create a new file but forget to add it to the `Target Components` column of the Traceability Matrix? 
2. Can I trace the file I just wrote all the way back up to a Business Objective or Actor? (If no, delete the code or document the missing links).
