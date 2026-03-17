# 📄 Few-Shot: Complete CR and IP Example

## 🤖 Core Directive (Zero-Shot)
**Use these examples as the canonical format when generating CR and IP documents.** Copy the structure and level of detail. Do not omit sections; use "N/A" with a one-line justification only when a section genuinely does not apply.

---

## Example: Change Requirement CR-007

# Change Requirement: Add Dark Mode Toggle

**Document ID:** CR-007  
**Date:** 2025-03-15  
**Priority:** Medium

## 1. Business Justification & Trigger
**Why are we doing this?**
Users are requesting a dark mode for nighttime reading to reduce eye strain. Support tickets and user surveys indicate this as a top-5 requested feature.

## 2. Scope Boundaries
**In Scope:**
- A single toggle control in the application header (or settings panel).
- Switching the active CSS theme from Light to Dark.
- Persisting the user's preference (e.g., localStorage or user profile) so it survives page reload.

**Out of Scope (Anti-Hallucination Guardrails):**
- Automatic theme based on system preference (may be a future CR).
- Per-component theme overrides.
- High-contrast or other accessibility themes beyond dark/light.

## 3. Impact Assessment
**Affected Functional Requirements:**
- REQ-012 (User Profile Settings) — Needs a new "Theme" or "Appearance" preference.

**Affected Non-Functional Requirements:**
- NFR-UI-001 (Accessibility) — Dark mode colors must maintain WCAG AA contrast ratios.

**New Dependencies Required?**
- No. Using existing CSS variables / theme layer.

## 4. Success Criteria
- A toggle (or dropdown) exists in the header/settings. Label: "Dark mode" or "Theme: Light / Dark".
- Clicking it switches the visible theme from Light to Dark (or vice versa) without full page reload.
- The chosen theme persists after refresh (same tab or new tab within the same origin).
- All text and interactive elements meet WCAG AA contrast in both themes.

---

### Example CR-007 (JSON)
```json
{
  "cr_id": "CR-007",
  "title": "Add Dark Mode Toggle",
  "classification": ["Functional", "Non-Functional"],
  "target_actors": ["ACT-001"],
  "target_use_cases": ["UC-003"]
}
```

---

## Example: Implementation Plan IP-007 (for CR-007)

# Implementation Plan: Dark Mode Toggle

**Document ID:** IP-007  
**Related Request:** CR-007  
**Status:** DRAFT (Awaiting User Approval)

## 1. Description & Scope
**What is being built/changed:**
Add a theme toggle to the header that switches between Light and Dark CSS themes and persists the choice in localStorage. Theme is implemented via a shared CSS variables layer already present in the app.

**In Scope:**
- `src/theme/themeTokens.json` — Add dark token set.
- `src/components/Header/ThemeToggle.tsx` — New component (toggle button).
- `src/components/Header/Header.tsx` — Import and render ThemeToggle.
- `src/hooks/useTheme.ts` — New hook: read/write theme from localStorage and apply class to document root.

**Out of Scope:**
- System preference detection (prefers-color-scheme).
- Any change to existing page layouts other than adding the toggle to the header.

## 2. Code Entropy & Domain Analysis
**Domain Classification:** Technology Domain (UI/presentation).  
*Justification:* Theme application is presentation logic; no business rules.

**Target Entropy (Files Modified):** 4  
*Calculation Breakdown:*
- `src/theme/themeTokens.json` — Add `dark` key with color tokens.
- `src/hooks/useTheme.ts` — New file; hook for theme state and persistence.
- `src/components/Header/ThemeToggle.tsx` — New file; toggle UI.
- `src/components/Header/Header.tsx` — One line: import and render `<ThemeToggle />`.

**Future Entropy Protection:**  
Adding a third theme (e.g., High Contrast) would require: (1) new tokens in themeTokens.json, (2) new option in useTheme, (3) ThemeToggle to support more than two options. No other files. Design keeps theme logic in one hook and one token file.

## 3. GoF Pattern Selection
**Selected Pattern:** Strategy (theme as interchangeable strategy applied at root).  
**Justification:** Theme selection is a family of algorithms (light vs dark). The hook selects the active strategy; the DOM class applies it. Per Patterns Use Guide, Strategy fits "interchangeable behaviors."

## 4. UI/UX & Metadata Constraints (If Applicable)
**Theme Adjustments:**  
New keys in `themeTokens.json`: `dark.background`, `dark.surface`, `dark.textPrimary`, `dark.textSecondary`, `dark.border`. All values chosen to meet WCAG AA.

**Navigation Flow:**  
N/A — Toggle lives in header; no new screens or routes.

## 5. Security Threat Model (OWASP)
**Risk Category:** None (no user input to server; no new auth; localStorage used only for preference).  
**Mitigation Strategy:** N/A — No injection or auth surface. If future work stores theme in user profile, preference will be validated server-side as a single enum value.

## 6. Non-Functional Requirements (NFR) Validation
**Affected NFRs:**  
- NFR-UI-001: All text and controls must meet WCAG AA contrast (4.5:1 normal, 3:1 large).

**Compliance Strategy:**  
Contrast ratios for dark theme tokens will be verified with a contrast checker before commit. Dark background and light text combinations will be chosen to meet 4.5:1 minimum.

## 7. Execution Steps
- [ ] Step 1: Add `dark` object to `src/theme/themeTokens.json` with required tokens.
- [ ] Step 2: Create `src/hooks/useTheme.ts`: read/write `theme` from localStorage, apply `data-theme="light"|"dark"` on document root, export `theme` and `setTheme`.
- [ ] Step 3: Create `src/components/Header/ThemeToggle.tsx`: button that calls `setTheme` to toggle; use theme tokens for icon/label.
- [ ] Step 4: In `src/components/Header/Header.tsx`, import ThemeToggle and render in header right section.
- [ ] Step 5: Add unit test for `useTheme`: default theme, toggle updates state and localStorage.
- [ ] Step 6: Verify all new functions have Domain/Pattern docstrings per `03_03_coding_guidelines.md`.
- [ ] Step 7: Update `documentation/requirements/functional_requirements_register.md` if REQ-012 is extended; update `documentation/history/traceability_matrix.md` with IP-007 and new components.

## 8. Verification Plan
- **Terminal Commands:** `npm run test` (unit tests for useTheme and ThemeToggle).
- **Visual Proof:** Run app, click toggle in header; confirm theme switches and persists on reload. Run accessibility audit (e.g., axe) on both themes.

## 9. Framework Deviations & Technology Overrides
**Technology Paradigm Conflict:** N/A — Fully compliant with general framework.  
**Justification:** Theme is metadata-driven (themeTokens.json); no hardcoded colors in components.
