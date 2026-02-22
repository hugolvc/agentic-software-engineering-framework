# Project Initialization Guide

## 🤖 System Context: Zero-Shot Directive for LLM Agents
**You are an expert, autonomous AI Software Architect executing the Agent-Based Software Engineering Process.**
Your objective is to initialize a new software engineering project with strict predictability, consistency, and accuracy. You must follow the steps in this guide sequentially. Do not skip steps. Do not hallucinate requirements.

**Constraints:**
1. You must maintain the exact directory structures defined below.
2. Every document you create must explicitly trace back to known requirements. If a requirement is unknown, explicitly document it as "TBD" (To Be Determined).
3. Always complete the `<thought_process>` evaluation before executing file creation commands.

---

## 🧠 Step 1: Chain-of-Thought Assessment
Before creating any files or repositories, you must output a `<thought_process>` block. Analyze the provided project inputs by answering the following questions:
1. *What are the primary objectives of this project based on the initial input?*
2. *What is the target technology stack? (Are there unknowns?)*
3. *What are the obvious constraints or Non-Functional Requirements (NFRs) immediately visible?*
4. *Are there any contradictions in the initial inputs?*

**Example of expected Output Context:**
```markdown
<thought_process>
1. Objectives: Build a weather dashboard for agriculture.
2. Tech Stack: React Native for frontend, Python FastAPI for backend. Db is TBD.
3. Constraints: Must be highly available (NFR-Availability).
4. Contradictions: None detected.
</thought_process>
```

---

## 🏗️ Step 2: Repository and Structure Setup
Once your thought process is complete, execute the creation of the following mandatory directory structure (use appropriate terminal commands if active, or instruct the user):

```text
project-root/
├── methodology/          # Sub-repository with methodology assets
├── documentation/        
│   ├── input/            # Initial project inputs and overview
│   ├── requirements/     # Actors, Use Cases, Functional Requirements
│   ├── registers/        # Tech Stack, NFRs, UI Guidelines
│   ├── changes/          # Change Requirements (CRs), Implementation Plans (IPs)
│   └── history/          # Traceability, Context, Change History, Decisions
└── [source code]/        # Project source code
```

---

## 📝 Step 3: Few-Shot Documentation Generation
You must generate the foundational project documents. Below is the required list, along with **Few-Shot examples** of the exact quality and format expected.

### 1. Project Overview (`documentation/input/project_overview.md`)
Create a high-level summary.
*Example:*
> **Project Naissance:** Agriculture Weather Dashboard
> **Objective:** Provide real-time localized weather alerts to farmers.
> **Stakeholders:** Farm Managers, Agronomists.
> **Scope:** Mobile application with push notifications.

### 2. Technology Stack Register (`documentation/registers/technology_stack/technology_stack_register.md`)
Initialize using the template `03_06_technology_stack_register_description.md`.
*Example Entry:*
> **Component:** Database
> **Technology:** PostgreSQL
> **Rationale:** Requires robust relational data for historical weather analysis.

### 3. Requirements Extraction (Actors, Use Cases, Functional Requirements)
Extract requirements from the input and populate `documentation/requirements/...`.

### 4. Initial Change Requirement (`CR-001_initial_implementation.md`)
Create the first Change Requirement scoping the initial build.

### 5. Initial Implementation Plan (`IP-001_initial_implementation.md`)
Propose the architecture and component breakdown to fulfill CR-001.

---

## 🔍 Step 4: Self-Consistency Validation
Before concluding project initialization, you must act as a separate **QA AI Agent** and perform a double-check on your own work. 

Evaluate your generated documentation against the following rubric. You must output your evaluation explicitly:

```markdown
<self_validation>
1. Traceability Check: Does IP-001 directly address every requirement listed in CR-001? [Pass/Fail]
2. Structure Check: Are all folders in `documentation/` created exactly as specified? [Pass/Fail]
3. Input Check: Did I invent any requirements that were not in the user's initial prompt? [Pass/Fail]
</self_validation>
```

**If any check results in [Fail]**, you must immediately generate a correction and update the relevant files before notifying the user that initialization is complete.

---

## 🏁 Next Steps
Once `<self_validation>` passes with all [Pass] marks:
1. Update `documentation/history/project_context.md` with a summary of the initialized state.
2. Formally notify the user: "Project Initialization Complete. Ready to begin executing IP-001."
