# ⚖️ System Context: Decision Log Template

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must permanently document any architectural, structural, or dependency decision that deviates from the project's default patterns.**
Because your chat memory is cleared between sessions, future AIs will not know *why* you chose Option B over Option A unless you explicitly write it down in a Decision Record (DEC-XXX).

**Constraints:**
1. **When to write a DEC:** You must write a DEC if you add a new library, choose a specific Design Pattern over an obvious alternative, or decide *not* to fix a bug due to technical limitations.
2. **Where to save:** Save these files in the `documentation/history/decisions/` directory as `DEC-XXX_[short_name].md`.
3. **Traceability:** Every Implementation Plan (IP-XXX) that relies on this decision must link to its DEC ID.

---

## 🧠 Chain-of-Thought (CoT): Decision Logging Sub-Routine
When you arrive at a crossroads during Implementation Planning, execute this thought process:

```text
<decision_logging_thought>
1. CROSSROADS DETECTED: I need to parse CSV files. Should I use the built-in `csv` module or install `pandas`?
2. TRADE-OFF ANALYSIS:
   - `csv`: Zero new dependencies, lower RAM usage.
   - `pandas`: Faster for massive files, but adds a heavy dependency to the Tech Stack.
3. DECISION ELICITATION: The user wants speed. I will choose `pandas`.
4. REGISTRATION: Because this adds a major dependency, I MUST write a DEC-XXX document explaining *why* I rejected the built-in `csv` module, so a future AI doesn't try to "optimize" it by removing `pandas`.
</decision_logging_thought>
```

---

## 📝 The Template
When you need to log a decision, copy from the line below and populate all fields.

---

# Decision Record: [Short Title]

**Document ID:** DEC-XXX  
**Date:** YYYY-MM-DD  
**Status:** [Proposed/Accepted/Superseded]

## 1. The Context & Problem
**What is the issue?**
[Briefly describe the technical or business problem you are facing.]

**Related Documents:**
- [List any CR-XXX, IP-XXX, or NFR-XXX this relates to].

## 2. The Options Considered
**Option A: [Name]**
- *Pros:* [List]
- *Cons:* [List]

**Option B: [Name]**
- *Pros:* [List]
- *Cons:* [List]

## 3. The Decision
**Selected Option:** [e.g., Option B]

**Justification:**
[Explain mathematically or logically why this option wins. Explain why the Cons of this option are acceptable risks.]

## 4. Architectural Impact
**Affected Components:**
- [List the files or modules that will be built around this decision.]

**Entropy Impact:**
[Does this decision increase or decrease the overall Code Entropy? Explain.]
