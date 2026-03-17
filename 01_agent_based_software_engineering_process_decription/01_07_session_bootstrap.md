# 🚀 System Context: Session Bootstrap (Mandatory Read Order)

## 🤖 Core Operational Directives (Zero-Shot)
**When you start a new session or resume after a BLOCKED state, you MUST read the following files in this order. Do not skip.**

If you are operating inside a project that has its own `documentation/` folder, use the project paths. If you are in the methodology repository only, use the paths as given.

---

## Session Start — Mandatory Read Order

1. **`00_control_panel.md`** — Or, if in a project: `documentation/input/ase_control_panel.md` (if it exists; otherwise methodology `00_control_panel.md`).
2. **`documentation/history/agent_state.json`** — Current phase, active CR/IP, next required step.
3. **`documentation/history/project_context.md`** — High-level project state.
4. **If `agent_state.json` has `active_ip` set:** Read the file referenced by `active_ip` (e.g., `documentation/changes/implementation_plans/IP-005_*.md`).
5. **If the user's message references a specific area:** Read the relevant register (e.g., `nfr_register.md`, `use_cases_register.md`) and the latest CR/IP for that area.

---

## Resume After BLOCKED

After the user replies to your BLOCKED message (e.g., choosing Option A or B):

1. Re-read **00_control_panel.md** (or project control panel).
2. Re-read **documentation/history/agent_state.json**.
3. Re-read **documentation/history/project_context.md**.
4. Re-read the **IP/CR that was blocked**.
5. Apply the user's choice. Update `agent_state.json` to clear `BLOCKED` and set `next_required_step` appropriately.
6. Continue from the step indicated in `next_required_step` (see `01_06_phase_checklists.md`).
