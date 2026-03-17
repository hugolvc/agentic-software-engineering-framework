# 📋 Framework Improvement Guide: More Actionable & Controllable (Prompting Only)

This document describes how to improve the ASE framework **without writing any code**—only by extending and optimizing the prompting base (new or revised Markdown files). The goal is to make agent behavior more **actionable** (agents know exactly what to do next) and **controllable** (humans can steer outcomes by editing config-style docs).

---

## 1. Add a Single "Control Panel" Document

**Problem:** Thresholds and rules are scattered (A-UCP 15, "every 10 tool calls", approval gates). There is no one place for a human to tune strictness or behavior without editing many files.

**Improvement:** Create **`00_control_panel.md`** (or `documentation/input/ase_control_panel.md` in applied projects) as the **single source of tunable parameters**. The agent is instructed to read this file first and override defaults only with values from this panel.

**Suggested content (copy-paste ready):**

```markdown
# ASE Control Panel (Single Source of Tunable Parameters)

**You must read this file when starting a session. These values override any defaults stated elsewhere in the methodology.**

| Parameter | Default | Description | Your action |
|-----------|---------|-------------|-------------|
| `A_UCP_ORCHESTRATOR_THRESHOLD` | 15 | If Implementation Plan A-UCP exceeds this, switch to Orchestrator; do not code. | Use this number for Orchestrator/Worker split. |
| `CANARY_REFRESH_INTERVAL` | 10 | Re-read NFR register every N tool calls. | Output `<canary_summary>` at this interval. |
| `REQUIRE_IP_APPROVAL` | true | If true, after generating IP-XXX you MUST wait for explicit user approval before coding. | Do not run Execution phase until approval. |
| `APPROVAL_PHRASES` | "approved", "proceed", "go ahead", "execute" | User message containing one of these = approval. | Treat as approval to execute IP. |
| `STRICTNESS_LEVEL` | standard | Options: minimal | standard | strict. | minimal=skip optional CoT; standard=full CoT; strict=all gates + mandatory DEC for any dependency. |
| `BLOCKED_REASONS_CATALOG` | (see below) | Canonical list of block reasons. | When blocking, use exactly one reason ID + the escalation format. |

**BLOCKED_REASONS_CATALOG (use exact ID when escalating):**
- `CONFLICTING_NFR` — Detected conflicting NFRs (e.g., PostgreSQL required but NoSQL budget).
- `MISSING_ACTOR_OR_UC` — Required Actor or Use Case missing from registers.
- `IP_EXECUTION_FAILED_3X` — Execution of IP failed 3 consecutive times.
- `AMBIGUOUS_REQUIREMENT` — User intent cannot be resolved without clarification.
```

**Why it works:** One file to edit = predictable control. Agents get a clear "read this first" hook; you get a single place to relax or tighten behavior.

---

## 2. Add Phase Checklists (Explicit "Do This Now" Steps)

**Problem:** The workflow describes phases but not a tickable, ordered checklist. Agents can skip or reorder steps.

**Improvement:** Add **checklist sections** to the Process Workflow (or a dedicated **`01_06_phase_checklists.md`**) so each phase has a **numbered, mandatory sequence** and an explicit **"Phase complete when"** line.

**Example for Phase 4 (Change Request Cycle):**

```markdown
## Phase 4: Change Request — Mandatory Checklist

Before writing any code, you MUST complete these steps in order. Output the step number and "DONE" when you complete it (e.g., "Step 4.2 DONE").

- [ ] **4.1** Read `documentation/history/agent_state.json`. If `active_cr` or `active_ip` is set, resolve or supersede first.
- [ ] **4.2** Output `<thought_process_analysis>` (past CRs, current codebase, blast radius). No file writes yet.
- [ ] **4.3** Classify: Functional / Non-Functional / Both. State which guideline file(s) you will use (02_01 and/or 03_01).
- [ ] **4.4** Retrieve and read those guideline files.
- [ ] **4.5** Create CR-XXX (`.md` and `.json`). Save to `documentation/changes/change_requirements/`.
- [ ] **4.6** Run `<functional_assessment_thought>` and/or `<non_functional_assessment_thought>`. Note which registers will be updated.
- [ ] **4.7** Create IP-XXX (`.md` and `.json`). Include register update steps in Execution Steps. Save to `documentation/changes/implementation_plans/`.
- [ ] **4.8** Update `agent_state.json`: set `active_ip`: "IP-XXX", `next_required_step`: "AWAIT_APPROVAL" or "EXECUTE" if approval not required.
- [ ] **4.9** If REQUIRE_IP_APPROVAL is true: Output "Implementation Plan IP-XXX is ready. Reply with one of: [APPROVAL_PHRASES] to proceed, or request edits." Then STOP. Do not execute code.
- [ ] **4.10** If approved (or approval not required): Proceed to Execution phase.

**Phase 4 (Planning) complete when:** CR-XXX and IP-XXX exist on disk, and either approval was given or REQUIRE_IP_APPROVAL is false.
```

**Why it works:** Unambiguous sequence + explicit "Phase complete when" reduces interpretation. Optional: require the agent to echo "Step X.Y DONE" so you can verify progress from the transcript.

---

## 3. Structured CoT Output Formats (Parseable Thought Blocks)

**Problem:** CoT blocks ask open-ended questions ("What is the blast radius?") so outputs vary. Hard to check programmatically or to train consistency.

**Improvement:** Define **exact output schemas** for each thought block so the agent fills slots instead of free-form prose. You can paste these into the relevant process/assessment docs.

**Example — Replace generic `<thought_process_analysis>` with:**

```markdown
You MUST output the following block. Use the exact keys. Fill every value.

<thought_process_analysis>
past_cr_summary: "[1–2 sentences: what past CRs say about this feature]"
current_codebase_state: "[1–2 sentences: relevant current state]"
blast_radius: "[List: file paths or component names likely impacted]"
</thought_process_analysis>
```

**Example — Classification block:**

```markdown
<thought_process_classification>
classification: [ "Functional" | "Non-Functional" | "Both" ]
guideline_files_to_read: [ "02_01_change_request_assessment_description.md" | "03_01_..." | "Both" ]
register_impacts: [ "actors_register" | "use_cases_register" | "functional_requirements_register" | "technology_stack_register" | "nfr_register" ] (list all that apply)
</thought_process_classification>
```

**Why it works:** Consistent structure makes it easier to validate (e.g., "did blast_radius get filled?") and to reuse outputs in later steps or tools.

---

## 4. Explicit Approval and Handoff Phrases

**Problem:** "Awaiting User Approval" is stated but the agent has no canonical list of user phrases that count as approval or as "request edits."

**Improvement:** Already partially covered in **Control Panel** (`APPROVAL_PHRASES`). In addition:

- In **04_01_description.md** or **04_04_context_management_guide.md**, add a short section:

```markdown
## Approval & Handoff (Exact Behavior)

- **Approval:** When the user's message contains any of the phrases in `APPROVAL_PHRASES` (from Control Panel), treat the last proposed IP-XXX as approved. Set `agent_state.json` → `next_required_step`: "EXECUTE" and proceed.
- **Request edits:** If the user asks to change the IP (e.g., "add step X", "use library Y instead"), do NOT execute. Update IP-XXX and re-output "Implementation Plan IP-XXX updated. Reply with [APPROVAL_PHRASES] to proceed."
- **New request:** If the user sends a completely new task (unrelated to the current IP), set `active_ip`: null, `active_cr`: null and start Phase 4 from step 4.1.
```

**Why it works:** Reduces ambiguity about when the agent is allowed to run code and when it must wait or re-plan.

---

## 5. Session Bootstrap: Ordered File List

**Problem:** "Context First" and "read project state" are stated but the exact set and order of files to read at session start are not defined. Agents may under-read or read in suboptimal order.

**Improvement:** Add **`01_07_session_bootstrap.md`** (or a section in Context Management Guide) with a **mandatory ordered reading list** for "Session Start" and "Resume After Block."

**Example:**

```markdown
# Session Bootstrap (Mandatory Read Order)

When you start a new session or resume after a BLOCKED state, you MUST read the following files in this order. Do not skip.

1. `00_control_panel.md` (or `documentation/input/ase_control_panel.md` if in project)
2. `documentation/history/agent_state.json`
3. `documentation/history/project_context.md`
4. If `agent_state.json` has `active_ip` set: the file referenced by `active_ip` (e.g., `documentation/changes/implementation_plans/IP-005_*.md`)
5. If the user's message references a specific area: the relevant register (e.g., `nfr_register.md`) and the latest CR/IP for that area

**Resume after BLOCKED:** After the user replies, re-read 1–3, then the IP/CR that was blocked. Then continue from the step indicated in `next_required_step`.
```

**Why it works:** Reduces variance in context loading and ensures control panel and state are always applied first.

---

## 6. Stronger Few-Shot: One Complete CR + One Complete IP

**Problem:** Templates are good but one full, realistic example of a CR and an IP (end-to-end) would anchor agent output format and reduce hallucination of structure.

**Improvement:** Add **`04_09_example_cr_and_ip_full.md`** (or split into two files) containing:

- **One full CR** (e.g., "Add dark mode toggle") with every section filled, including Scope Boundaries (In/Out), Impact Assessment, Success Criteria, and optional JSON snippet.
- **One full IP** for that CR with every section filled: Description, Entropy table, Pattern, UI/NFR/Security, **Execution Steps as a numbered checklist**, Verification Plan, and "N/A" for Framework Deviations with a one-line justification.

**Why it works:** Few-shot is most effective when the example is complete. One canonical example per artifact type significantly stabilizes format and completeness.

---

## 7. Decision Tree: "If User Says X, Do Y"

**Problem:** Agents must infer whether a message is "new project," "new change," "approval," or "edit request." A small decision tree in the README or Process Workflow would make routing deterministic.

**Improvement:** Add a **routing section** at the top of the Process Workflow or README:

```markdown
## Request Routing (Do This First)

When you receive a user message, classify it into exactly one:

| User message type | Condition | Next action |
|-------------------|-----------|-------------|
| New project | User says they want to "start", "init", "create" a new project or app | Go to Project Initialization Guide; run Step 1 (CoT) then Step 2 (structure). |
| Approval | Message contains any APPROVAL_PHRASE from Control Panel and you have a DRAFT IP | Treat as approval; proceed to Execution for that IP. |
| Edit IP | User asks to change the current IP (e.g., different approach, more steps) | Do not execute; revise IP-XXX and re-output "IP updated. Reply with [phrases] to proceed." |
| New change | User describes a feature, fix, or change (and it's not approval/edit) | Go to Phase 4; start at checklist step 4.1. |
| Clarification / Block resolution | User is replying to your BLOCKED message (Option A / B) | Re-read Control Panel and agent_state; apply user's choice; unblock and continue from `next_required_step`. |
```

**Why it works:** Single place that defines "what to do first" from the user's message. Makes behavior more predictable and easier to debug.

---

## 8. Done Criteria and Self-Validation Checklist

**Problem:** Self-consistency gates say "if no, revise" but don't specify the exact checklist or what "done" looks like per phase.

**Improvement:** Add a **single "Done & Self-Validation"** section (e.g., at the end of Process Workflow or in a new **`04_10_done_criteria_and_validation.md`**) that lists:

- **Per phase:** "Phase X is DONE when [list of artifacts and conditions]."
- **Before notify_user:** A short checklist the agent must run and output (e.g., as `<self_validation>` with Pass/Fail per line).

**Example:**

```markdown
## Done Criteria (Do Not Notify User Until All Pass)

Before you send a completion message:

- [ ] CR-XXX and IP-XXX exist and are linked. (Traceability)
- [ ] Code changes match the Execution Steps in IP-XXX. (No extra files modified.)
- [ ] Registers (actors, use cases, NFR, tech stack) updated if the assessment said so. (Register impact)
- [ ] Traceability matrix includes new components. (Traceability Guide)
- [ ] Tests run successfully (`run_command` used; full suite if possible). (Validation procedures)
- [ ] agent_state.json updated: `active_ip`/`active_cr` cleared if task done; `next_required_step` set appropriately.

Output this block before your final message:

<self_validation>
Traceability: [Pass/Fail]
Execution match: [Pass/Fail]
Registers: [Pass/Fail]
Traceability matrix: [Pass/Fail]
Tests: [Pass/Fail]
State file: [Pass/Fail]
</self_validation>
```

**Why it works:** Explicit done criteria and a single validation block make it clear when the agent is allowed to say "task complete" and give you a consistent receipt to verify.

---

## 9. Summary: What to Add or Edit (No Code)

| # | Document to add or extend | Purpose |
|---|----------------------------|---------|
| 1 | **00_control_panel.md** (new) | Single place for thresholds, approval phrases, strictness, block reasons. |
| 2 | **01_06_phase_checklists.md** (new) or extend 01_04 | Numbered checklists per phase + "Phase complete when." |
| 3 | Process / assessment docs (01_02, 02_01, 03_01, etc.) | Replace free-form CoT with structured blocks (exact keys/slots). |
| 4 | **04_01** or **04_04** | Approval & handoff section (approval phrases, edit request, new request). |
| 5 | **01_07_session_bootstrap.md** (new) or 04_04 | Ordered file list for session start and resume. |
| 6 | **04_09_example_cr_and_ip_full.md** (new) | One complete CR + one complete IP as few-shot. |
| 7 | **01_04** or README | Request routing table (new project / approval / edit / new change / unblock). |
| 8 | **04_10_done_criteria_and_validation.md** (new) or 01_04 | Done criteria per phase + single `<self_validation>` checklist before notify. |

Implementing these in order (1 → 8) will make the framework more **actionable** (clear next step, checklists, bootstrap) and **controllable** (one control panel, explicit approval, routing, and validation) without any code—only by extending and optimizing the prompting base.
