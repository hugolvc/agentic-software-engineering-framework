# 📂 System Context: Project Documentation Structure & Naming Conventions

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must adhere strictly to the directory structure and file naming conventions defined below.**
You do not have permission to create ad-hoc files in the root directory. You do not have permission to invent new documentation folders. All knowledge, requirements, and historical context must be organized exactly as specified so that your future Context Retrieval operations succeed.

---

## 🏗️ Mandatory Directory Architecture

Every project you initialize or operate within must contain the following exact structure. 
*Constraint: If you cannot find this structure, you must halt execution and build it.*

```text
project-root/
├── methodology/                    # Sub-repository: You are reading from here
├── documentation/                  # Project Context: You read and write here
│   ├── input/                      # Raw inputs provided by the user
│   ├── requirements/               # Extracted Actors, Use Cases, Functional Reqs
│   ├── registers/                  # Tracked state (Tech Stack, NFRs, UI Styles)
│   ├── changes/                    # Your generated CRs and IPs
│   └── history/                    # Traceability matrices and chronological logs
└── [source code]/                  # Your execution target
```

---

## 🏷️ Few-Shot: Naming Conventions & IDs

When creating new documents, you MUST use the exact ID format and naming convention. Do not deviate. All IDs must use three digits with leading zeros (e.g., `001`).

### 1. Requirements & Registers
*   **Actors Register:** `documentation/requirements/actors_register.md`
    *   *ID Format:* `ACT-001`
*   **Use Cases Register:** `documentation/requirements/use_cases_register.md`
    *   *ID Format:* `UC-001`
*   **Functional Requirements Register:** `documentation/requirements/functional_requirements_register.md`
    *   *ID Format:* `REQ-001`
*   **Non-Functional Requirements Register:** `documentation/registers/nfr_register.md`
    *   *ID Format:* `NFR-001`
*   **Technology Stack Register:** `documentation/registers/technology_stack_register.md`
    *   *ID Format:* `TECH-001`

### 2. Change Management Documents
Whenever you execute a change, you must increment the ID sequentially from the highest existing ID in that folder.

*   **Change Requirements:** `documentation/changes/change_requirements/CR-XXX_[descriptive_name].md`
    *   *Example:* `CR-004_oauth_login_integration.md`
*   **Implementation Plans:** `documentation/changes/implementation_plans/IP-XXX_[component_name].md`
    *   *Example:* `IP-004_authentication_service.md`

### 3. Historical Tracking
*   **Decision Register:** `documentation/history/decision_register.md`
    *   *ID Format:* `DEC-001`
*   **Traceability Matrix:** `documentation/history/traceability_matrix.md`

---

## 🧠 Chain-of-Thought (CoT): Document Creation Sub-Routine

Whenever you are tasked with creating a new document, execute this internal logic before writing the file:

```text
<document_creation_thought>
1. What type of document am I creating? (e.g., Implementation Plan).
2. What folder does this belong in? (e.g., `documentation/changes/implementation_plans/`).
3. What is the next logical ID? (e.g., The last one was IP-003, so this is IP-004).
4. Does the filename match the `[PREFIX]-XXX_[name].md` convention?
</document_creation_thought>
```

---

## 🔍 Self-Consistency Gate: Traceability
Before concluding any task that involves writing code or adding a new feature, you must perform a Traceability check.

*   Did I map the new feature (`COMP-XXX`) back to its implementation plan (`IP-XXX`), its change requirement (`CR-XXX`), and the original functional requirement (`REQ-XXX`) in the `traceability_matrix.md`?
*   If the answer is no, you must update the Traceability Matrix immediately.
