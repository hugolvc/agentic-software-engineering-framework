# 📄 System Context: Change Requirement (CR) Template (Prompt Object)

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you cannot execute code changes based on vague user wishes. Every change must be tracked by a formal Change Requirement (CR) Prompt Object.**

If the user says "Add a dark mode button," you must first formalize this into a CR document before proceeding to the Implementation Plan. The CR is the authoritative source of *WHAT* needs to change and *WHY*, whereas the Implementation Plan (IP) dictates *HOW*.

**Constraints:**
1. **CR ID Assignment:** Every new feature, bug fix, or request gets a sequential ID (e.g., CR-001, CR-002).
2. **Mandatory Impact Assessment:** You cannot write a CR without explicitly listing which existing Functional (REQ-XXX) and Non-Functional (NFR-XXX) requirements are affected.
3. **Save to Disk:** CRs must be saved in `documentation/changes/change_requirements/` using the filename pattern `CR-XXX_[descriptive_name].md` (see `01_05_project_documentation_structure.md`).
4. **Paired JSON:** Also write `CR-XXX_[descriptive_name].json` beside the Markdown file, validated against `schemas/change_requirement.schema.json`. See `examples/CR-001.example.json` for a filled instance; **JSON is authoritative for tooling** when both exist (see `01_02_process_description.md`).

---

## 🧠 Chain-of-Thought (CoT): CR Formalization Sub-Routine
When receiving an informal request from the user, execute this thought process to generate the CR:

```text
<cr_formalization_thought>
1. INTENT EXTRACTION: What is the underlying business goal of the user's prompt?
2. SCOPE DEFINITION: What exactly is IN scope, and what must I explicitly declare OUT of scope to prevent hallucinated features?
3. IMPACT TRACING: 
   - Does this affect an existing Actor (ACT)?
   - Does it affect an existing Use Case (UC)?
   - Does it violate any NFRs (e.g., adding a heavy library that breaks performance NFRs)?
4. TEMPLATE GENERATION: I will now fill out the CR Template.
</cr_formalization_thought>
```

---

## 📝 The Template
When generating a Change Requirement document, copy from the line below and fill out all fields.

---

# Change Requirement: [Short, Descriptive Name]

**Document ID:** CR-XXX  
**Date:** YYYY-MM-DD  
**Priority:** [Critical/High/Medium/Low]

## 1. Business Justification & Trigger
**Why are we doing this?**
[Explain the business logic. Example: "Users are requesting a dark mode for nighttime reading to reduce eye strain."]

## 2. Scope Boundaries
**In Scope:**
- [Mandatory list of what this change covers]

**Out of Scope (Anti-Hallucination Guardrails):**
- [Mandatory list of related features that the AI must explicitly NOT build during this change]

## 3. Impact Assessment
**Affected Functional Requirements:**
- [e.g., REQ-005 (User Profile Settings) - Needs a new toggle switch.]

**Affected Non-Functional Requirements:**
- [e.g., NFR-UI-001 (Accessibility) - Dark mode colors must maintain WCAG AA contrast ratios.]

**New Dependencies Required?**
- [Yes/No. If Yes, must update Technology Stack Register.]

## 4. Success Criteria
[List exactly how the AI or User will know this CR is complete. Example: "A toggle button exists on the header. Clicking it switches the CSS theme from Light to Dark. The preference persists on page reload."]
