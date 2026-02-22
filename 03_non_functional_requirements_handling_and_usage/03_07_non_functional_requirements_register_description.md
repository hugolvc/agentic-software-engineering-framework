# ⚖️ System Context: Non-Functional Requirements (NFR) Register

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must treat Non-Functional Requirements (NFRs) as absolute constraints on your generated code.**
While Functional Requirements dictate *what* the system does, NFRs dictate *how well* it does it (Speed, Security, Maintainability). If your proposed Implementation Plan satisfies a Functional Requirement but violates an NFR (e.g., exposing an unauthenticated endpoint in a secure system), your plan is invalid.

**Constraints:**
1. **Mathematical Measurability:** Syntactic adjectives like "fast", "secure", or "reliable" are banned when defining NFRs. You must define NFRs using testable, mathematical thresholds (e.g., `< 200ms`, `AES-256`, `99.9%`).
2. **Registration:** All NFRs must be strictly tracked in `documentation/registers/nfr_register.md`.
3. **Traceability:** Every NFR must link to the specific system components it affects.

---

## 🧠 Chain-of-Thought (CoT): NFR Validation Sub-Routine
When drafting an `Implementation Plan` or writing code, you must execute this thought process against the NFR Register:

```text
<nfr_validation_thought>
1. SECURITY CHECK (NFR-SEC): Does my new feature handle user input? Are there specific NFRs for escaping data or authentication middleware I must apply?
2. PERFORMANCE CHECK (NFR-PERF): Does my new database query involve a table scan? Does the NFR Register mandate a strict `< 300ms` response time for this endpoint? (If YES -> I must add a database index or caching layer to my plan).
3. MAINTAINABILITY CHECK (NFR-MNT): Is my proposed code increasing Code Entropy beyond acceptable limits?
</nfr_validation_thought>
```

---

## 📝 Few-Shot: NFR Registration Templates
When defining or updating an NFR in the `nfr_register.md`, use the exact markdown formats below.

### Example: Performance NFR (Good vs Bad)
**❌ BAD (Unmeasurable):**
> "The API should be fast when searching for users."

**✅ GOOD (Testable):**
```markdown
**Requirement ID**: NFR-PERF-012
**Requirement Name**: User Search Latency
**Category**: Performance
**Priority**: High

**Measurable Criteria**:
- Metric: P95 Response Time
- Target Value: < 250 milliseconds
- Measurement Method: API load testing with 100 concurrent users.

**Affected Components**:
- UserController
- UserSearchRepository
```

### Example: Security NFR (Good vs Bad)
**❌ BAD (Unmeasurable):**
> "The user passwords must be securely protected."

**✅ GOOD (Testable):**
```markdown
**Requirement ID**: NFR-SEC-004
**Requirement Name**: Password Hashing Standard
**Category**: Security
**Priority**: Critical

**Measurable Criteria**:
- Metric: Hashing Algorithm compliance
- Target Value: Argon2id (min 2 iterations, 19 MiB memory)
- Measurement Method: Static Code Analysis & Code Review.

**Affected Components**:
- AuthenticationService
```

---

## 🔍 Self-Consistency Gate
Before concluding your NFR analysis or Implementation Plan, verify:
> *Did I simply state that my code will be "secure and fast", or did I explicitly cite the ID of the NFR (e.g., NFR-PERF-012) and implement the exact mechanism required to meet its mathematical threshold?*
