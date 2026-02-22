# 🛠️ System Context: Technology Stack Register

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must operate exclusively within the bounds of the approved Technology Stack.**
You are strictly prohibited from importing a new third-party library, adding a new database driver, or swapping a core framework without first formally updating the `documentation/registers/technology_stack_register.md`. 

**Constraints:**
1. **No Phantom Dependencies:** If a library is not in the Technology Stack Register, you cannot use it in your code.
2. **Version Strictness:** If the Register specifies `React v18`, you cannot use features exclusive to `React v19`.
3. **Entropy Justification:** Adding a new technology increases the system's baseline Code Entropy. You must justify why an existing technology cannot handle the requirement.

---

## 🧠 Chain-of-Thought (CoT): Stack Modification Sub-Routine
When a user prompt or Change Request (CR) implies the need for a new technical capability (e.g., "Add PDF export"), execute this thought process before writing the Implementation Plan:

```text
<stack_modification_thought>
1. REQUIREMENT: What is the new technical capability needed? (e.g., PDF generation).
2. EXISTING STACK CHECK: Do we already have a library in our `technology_stack_register.md` that can do this? 
   - If YES -> Use it. Do not add a new dependency.
   - If NO -> Proceed to step 3.
3. ENTROPY COST: Does adding `Library X` require me to rewrite existing architecture, or is it a localized addition?
4. REGISTRATION: I must add `Library X` to the Technology Stack Register before writing the logic.
</stack_modification_thought>
```

---

## 📝 Few-Shot: Technology Registration Templates
When updating the `technology_stack_register.md`, use the exact markdown template below. Every field is mandatory.

### Example: Registering a Core Framework
```markdown
**Technology ID**: TECH-001
**Technology Name**: FastAPI
**Category**: Frameworks and Libraries (Backend)
**Version**: 0.103.0
**Status**: Active

**Role**: Primary
**Criticality**: Critical

**Purpose in System**: 
Serves as the primary REST API framework handling all HTTP routing, request validation (via Pydantic), and response serialization.

**Version Constraints**: 
- Minimum Version: 0.100.0 (Due to Pydantic v2 migration)

**Rationale**: 
Chosen for its native async support, automated OpenAPI documentation generation, and high performance compared to standard Flask.
```

### Example: Registering a Supporting Library
```markdown
**Technology ID**: TECH-015
**Technology Name**: Stripe Node.js SDK
**Category**: Communication and Integration
**Version**: ^14.0.0
**Status**: Planned

**Role**: Secondary
**Criticality**: Important

**Purpose in System**: 
Handles communication with the Stripe API for processing credit card payments and managing subscriptions.

**Version Constraints**: 
- Minimum Version: 14.0.0

**Rationale**: 
Required to securely process payments without exposing raw card data to our servers, fulfilling NFR-005 (PCI Compliance).
```

---

## 🔍 Self-Consistency Gate
Before concluding an Implementation Plan that involves a new technology:
1. Did I check `package.json` or `requirements.txt` to ensure this package isn't actually already installed but missing from the register?
2. Did I explicitly define the `Version Constraints` in my proposed Register entry so future AI agents know not to accidentally break the build with a major version bump?
