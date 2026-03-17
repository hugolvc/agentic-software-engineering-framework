# ✅ System Context: Done Criteria & Self-Validation

## 🤖 Core Operational Directives (Zero-Shot)
**You must NOT notify the user that a task is complete until you have run the checklist below and output the `<self_validation>` block with all items Pass.**
If any item is Fail, you must fix the discrepancy before sending the completion message.

---

## Done Criteria (Do Not Notify User Until All Pass)

Before you send a completion message for an Implementation Plan execution:

- [ ] **CR-XXX and IP-XXX exist and are linked.** (Traceability: CR and IP files on disk; IP references correct CR.)
- [ ] **Code changes match the Execution Steps in IP-XXX.** (No extra files modified beyond the IP; no steps skipped.)
- [ ] **Registers updated if the assessment said so.** (Actors, use cases, functional requirements, technology stack, NFR — per your `<functional_assessment_thought>` / `<non_functional_assessment_thought>`.)
- [ ] **Traceability matrix includes new components.** (Every new or modified file listed in `documentation/history/traceability_matrix.md` with correct REQ/CR/IP mapping.)
- [ ] **Tests run successfully.** (You used `run_command` to run the test suite; full suite if possible. No silent failures.)
- [ ] **agent_state.json updated.** (`active_ip` and `active_cr` cleared if task is complete; `next_required_step` set appropriately.)

---

## Mandatory Output Before Completion Message

You MUST output the following block immediately before your final completion message to the user. Replace each `[Pass/Fail]` with the actual result.

```text
<self_validation>
Traceability: [Pass/Fail]
Execution match: [Pass/Fail]
Registers: [Pass/Fail]
Traceability matrix: [Pass/Fail]
Tests: [Pass/Fail]
State file: [Pass/Fail]
</self_validation>
```

If any line is Fail, do not send the completion message. Fix the failure, then re-run this validation until all are Pass.

---

## Phase-Level Done Criteria (Reference)

- **Phase 1 (Project Initialization) complete when:** All folders exist; CR-001 and IP-001 exist; `<self_validation>` from `01_03_project_initialization_guide.md` passes; user notified.
- **Phase 4 (Planning) complete when:** CR-XXX and IP-XXX exist on disk; either user approval was given or `REQUIRE_IP_APPROVAL` is false (see `00_control_panel.md`).
- **Execution complete when:** Code matches IP; tests pass; registers and traceability updated; the checklist above and `<self_validation>` block above are complete with all Pass; state file updated; user notified.
