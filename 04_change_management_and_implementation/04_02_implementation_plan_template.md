# 📋 System Context: Implementation Plan Template

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must generate an Implementation Plan using exactly this template BEFORE writing any code for a Change Request.**
Your proposed Implementation Plan is your "Contract" with the user. You must populate every section. If a section does not apply, you must explicitly write "N/A" and justify why.

**Constraints:**
1. **No Output Deviation:** Copy the Markdown structure below exactly. Do not invent new headers.
2. **Strict Traceability:** You must link this Implementation Plan to a specific Change Request ID (CR-XXX).
3. **Entropy Calculation:** You must mathematically predict the Code Entropy (number of files touched) for this change and for future changes related to this component.

---

## 📝 The Template
Copy from the line below to generate your Implementation Plan.

---

# Implementation Plan: [Component/Feature Name]

**Document ID:** IP-XXX  
**Related Request:** CR-XXX  
**Status:** DRAFT (Awaiting User Approval)

## 1. Description & Scope
**What is being built/changed:**
[Provide a 2-3 sentence description]

**In Scope:**
- [List exact files, functions, or UI elements to be added/modified]

**Out of Scope:**
- [List related things you are explicitly NOT touching to prevent scope creep]

## 2. Code Entropy & Domain Analysis
**Domain Classification:** [Technology Domain OR Problem Domain]
*Justification:* [Why does it belong here?]

**Target Entropy (Files Modified):** [Number]
*Calculation Breakdown:*
- File 1: `path/to/file1.ts` (Reason: Adding new route)
- File 2: `path/to/file2.ts` (Reason: Adding new component)

**Future Entropy Protection:**
*If this feature needs to be updated next month, how many files will the next engineer need to touch? Explain how your design minimizes this number.*

## 3. GoF Pattern Selection
**Selected Pattern:** [e.g., Strategy, Factory, Adapter, None]
**Justification:** 
[Follow the `<pattern_selection_thought>` criteria from the Patterns Use Guide. If 'None', explain why the logic is too trivial to warrant a pattern.]

## 4. UI/UX & Metadata Constraints (If Applicable)
**Theme Adjustments:**
[List any new colors or spacing tokens being added to the Theme Metadata Object. If none, write "N/A - Using existing theme tokens."]

**Navigation Flow:**
[If adding a new screen, provide a Mermaid State Diagram showing how to route to it.]

## 5. Non-Functional Requirements (NFR) Validation
**Affected NFRs:**
- [e.g., NFR-PERF-012: Must load under 200ms]
**Compliance Strategy:**
[How specifically will your code satisfy these mathematical thresholds?]

## 6. Execution Steps
*This is the exact sequence of `write_to_file` or `multi_replace_file_content` actions you will take once this plan is approved.*

- [ ] Step 1: Create `path/to/new_file.ext` with boilerplate.
- [ ] Step 2: Modify `path/to/existing_file.ext` to import the new file.
- [ ] Step 3: Write unit tests in `path/to/test_file.ext`.
- [ ] Step 4: [Further detailed steps...]

## 7. Verification Plan
*How will you prove to the user that this works?*
- **Terminal Commands:** [e.g., `npm run test`, `python -m pytest`]
- **Visual Proof:** [e.g., Take a screenshot of the browser at `http://localhost:3000/new-route`]
