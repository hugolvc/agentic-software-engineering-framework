# 📋 System Context: Phase Checklists (Mandatory Execution Order)

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must complete the steps in each phase in the exact order given.**
Output the step number and "DONE" when you complete it (e.g., "Step 4.2 DONE"). Do not skip steps. Do not reorder.

---

## Phase 1: Project Initialization — Mandatory Checklist

*Reference: `01_03_project_initialization_guide.md`*

- [ ] **1.1** Output `<thought_process>`: objectives, target tech stack, obvious NFRs, contradictions. No file writes yet.
- [ ] **1.2** Create repository structure: `documentation/` with `input/`, `requirements/`, `registers/`, `changes/`, `history/`.
- [ ] **1.3** Create `documentation/history/agent_state.json` with initial state (e.g., `current_phase`, `next_required_step`).
- [ ] **1.4** Create `documentation/input/project_overview.md`.
- [ ] **1.5** Create Technology Stack Register (template: `03_06_technology_stack_register_description.md`).
- [ ] **1.6** Extract and populate Actors Register, Use Cases Register, Functional Requirements Register (from input).
- [ ] **1.7** Create CR-001 (initial implementation). Save to `documentation/changes/change_requirements/`.
- [ ] **1.8** Create IP-001 (initial implementation). Save to `documentation/changes/implementation_plans/`.
- [ ] **1.9** Run `<self_validation>`: Traceability, Structure, Input (no invented requirements). Fix any [Fail] before proceeding.
- [ ] **1.10** Update `documentation/history/project_context.md`. Notify user: "Project Initialization Complete. Ready to begin executing IP-001."

**Phase 1 complete when:** All folders exist, CR-001 and IP-001 exist, self_validation passes, user notified.

---

## Phase 4: Change Request (Planning) — Mandatory Checklist

*Reference: `01_02_process_description.md`, `01_04_process_workflow.md`*

Before writing any code, you MUST complete these steps in order.

- [ ] **4.1** Read `documentation/history/agent_state.json`. If `active_cr` or `active_ip` is set, resolve or supersede first.
- [ ] **4.2** Output `<thought_process_analysis>` (structured format per `01_02_process_description.md`). No file writes yet.
- [ ] **4.3** Output `<thought_process_classification>`: Functional / Non-Functional / Both. State which guideline file(s) you will use (02_01 and/or 03_01).
- [ ] **4.4** Retrieve and read those guideline files.
- [ ] **4.5** Create CR-XXX (`.md` and `.json`). Save to `documentation/changes/change_requirements/`.
- [ ] **4.6** Run `<functional_assessment_thought>` and/or `<non_functional_assessment_thought>`. Note which registers will be updated.
- [ ] **4.7** Create IP-XXX (`.md` and `.json`). Include register update steps in Execution Steps. Save to `documentation/changes/implementation_plans/`.
- [ ] **4.8** Update `agent_state.json`: set `active_ip`: "IP-XXX", `next_required_step`: "AWAIT_APPROVAL" or "EXECUTE" (if approval not required per Control Panel).
- [ ] **4.9** If REQUIRE_IP_APPROVAL is true (from `00_control_panel.md`): Output "Implementation Plan IP-XXX is ready. Reply with one of: [APPROVAL_PHRASES from Control Panel] to proceed, or request edits." Then STOP. Do not execute code.
- [ ] **4.10** If approved (or approval not required): Proceed to Execution phase.

**Phase 4 (Planning) complete when:** CR-XXX and IP-XXX exist on disk, and either approval was given or REQUIRE_IP_APPROVAL is false.

---

## Execution Phase — Mandatory Checklist

*Reference: `04_02_implementation_plan_template.md`, `04_06_validation_and_testing_procedures.md`*

- [ ] **E.1** Read the approved IP-XXX. Do not deviate from the Execution Steps listed.
- [ ] **E.2** Execute each step in the IP-XXX Execution Steps in order. Use only the files and actions specified.
- [ ] **E.3** Run tests as specified in the IP Verification Plan. Use `run_command`; do not assume tests pass.
- [ ] **E.4** Update registers (actors, use cases, NFR, tech stack) as stated in the IP and in your assessment thoughts.
- [ ] **E.5** Update `documentation/history/traceability_matrix.md` with new components.
- [ ] **E.6** Update `documentation/history/change_history.md` (if present).
- [ ] **E.7** Run the Done Criteria checklist from `04_10_done_criteria_and_validation.md`. Output `<self_validation>`.
- [ ] **E.8** Update `agent_state.json`: clear `active_ip` and `active_cr` if task is complete; set `next_required_step` appropriately.
- [ ] **E.9** Notify user with completion summary.

**Execution complete when:** Code matches IP, tests pass, registers and traceability updated, self_validation all Pass, state file updated, user notified.
