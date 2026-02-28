# 🧠 System Context: Context Management Guide

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, your memory is stateless across sessions. You must rely entirely on the `documentation/` repository index to maintain project context.**
You are strictly prohibited from storing critical project decisions, API keys, or architectural layouts in your immediate chat memory. Every architectural fact must exist on disk.

**Constraints:**
1. **The Accumulation Principle:** NEVER delete historical `CR-XXX` or `IP-XXX` files. You may mark them as `Status: Superseded`, but you must retain the history.
2. **Context First:** Before proposing a change to an existing module, you MUST read its corresponding documentation files to understand the original design intent.
3. **Write-Through Context:** When you make a decision that deviates from the original plan, you MUST update the accompanying document. Do not leave the code and the documentation out of sync.
4. **State Machine Integrity:** Before you do anything else, check `documentation/history/agent_state.json`. When you finish a step, you MUST update this JSON file. You must use this file as a persistent state anchor across sessions.

---

## 🧠 Chain-of-Thought (CoT): Context Retrieval Sub-Routine
When starting a new task or resuming a session, you must execute this retrieval thought process to load the project state into your active context window:

```text
<context_retrieval_thought>
1. ENTRY POINT: I need to understand the current state of the project. I will read `documentation/history/project_context.md`.
2. TRACEABILITY: The user asked me to modify the payment gateway. 
   - I must use the `grep_search` or `find_by_name` tool to locate the relevant `IP-XXX` document for the payment gateway.
   - I must read the existing non-functional requirements (`nfr_register.md`) to ensure my changes don't violate compliance.
3. REGISTERS: Are there specific Actors (`ACT-XXX`) or Use Cases (`UC-XXX`) associated with this module? Let me check the registers.
</context_retrieval_thought>
```

---

## 📂 Expected Context Architecture (Few-Shot Structure)
You must enforce and navigate the following directory structure mapping context:

```text
documentation/
├── input/                    # Raw materials (User prompts, legacy code docs)
├── requirements/             # WHAT the system does
│   ├── actors/               # Who uses it (ACT-XXX)
│   ├── use_cases/            # Workflows (UC-XXX)
│   └── functional_requirements/ # Explicit features (REQ-XXX)
├── registers/                # HOW the system is built
│   ├── technology_stack/     # Authorized libraries (TECH-XXX)
│   ├── non_functional_requirements/ # Math constraints (NFR-XXX)
│   └── ui_styling_guidelines/ # Visual metadata
├── changes/                  # Change Management
│   ├── change_requirements/  # The 'Why' (CR-XXX)
│   └── implementation_plans/ # The 'How' (IP-XXX)
└── history/                  # Project memory
    ├── agent_state.json      # Machine-readable current state of the AI agent
    ├── project_context.md    # High-level overview
    ├── change_history.md     # Chronological log
    └── traceability_matrix.md# Dependency mapping
```

## 🔍 Self-Consistency Gate
Before executing a file modification:
1. Did I read the `IP-XXX` file for the module I am about to change? (If no, I am flying blind and must read it first).
2. After writing the code, did I update `change_history.md` to record my actions for the next AI agent session?
