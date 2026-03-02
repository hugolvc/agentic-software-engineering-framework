# 📐 System Context: Coding Guidelines

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must adhere to these strict coding standards when generating or modifying code.**
Do not generate code that violates these rules, even if it seems faster. These guidelines exist to minimize Code Entropy and make the software durable for future AI iterations.

**Constraints:**
1.  **Single Responsibility:** Every function must do exactly one thing. If you find yourself using "and" or "then" to describe what a function does, you must split it.
2.  **Metadata Over Code:** Do not hardcode configuration, stylistic tokens, or navigational states into logical components. Use metadata (e.g., config files, DB tables, or constants).
3.  **Pattern & Paradigm Enforcement:** You must explicitly declare which UML Design Pattern (GoF) *and* which state-of-the-art engineering paradigm (e.g., Clean Architecture, SOLID, DRY) you are applying in your Implementation Plan to justify your approach.
4.  **Security by Default:** You must adhere to enterprise security standards (e.g., OWASP Top 10). If synthesizing queries, constructing APIs, or handling user input, you must automatically implement defensive measures (parameterized queries, sanitization, RBAC checking) without being explicitly asked by the user.
5.  **Technology Paradigm Override (Rule Deviancy):** If a general ASE framework directive fundamentally conflicts with the established best practices of the requested tech stack (e.g., Next.js Server Components vs. generic MVC separation, Tailwind CSS vs. JSON theme objects), you may **override the framework rule**. However, you MUST explicitly analyze, justify, and log this deviation in the `Framework Deviations` section of your Implementation Plan. Silent failures or undocumented deviations are strictly prohibited.

---

## 🧠 Chain-of-Thought (CoT): Code Generation Sub-Routine
When writing an Implementation Plan or generating the actual code, you must execute the following thought process to validate your technical approach:

```text
<coding_guidelines_thought>
1. DOMAIN & CLEAN ARCHITECTURE CHECK: Am I mixing the Technology Domain (e.g., SQL/HTTP) with the Problem Domain (e.g., Business Logic)? Am I respecting the Dependency Rule where inner layers do not depend on outer layers?
   - If YES -> Separate them immediately into different layers (e.g., Service vs. Repository).
2. HARDCODING CHECK: Am I hardcoding a color, a UI string, or a routing path directly inside a UI component?
   - If YES -> Move it to a metadata dictionary/configuration file. (UI is configuration, not code).
3. PATTERN & EXTERNAL STANDARDS CHECK: What UML pattern justifies this file structure? Which external engineering guideline (e.g., Uncle Bob's Clean Code, SOLID) am I adhering to here to keep the entropy low?
4. SECURITY & OWASP CHECK: Does this code touch the database, authenticate a user, or process user input?
   - If YES -> Have I implemented prepared statements, input sanitization, and verified RBAC permissions according to OWASP standards?
5. DOCSTRING CHECK: Did I write an inline docstring for this function? Does the docstring explain the *business process* and the *domain classification*?
</coding_guidelines_thought>
```

---

## 📝 Few-Shot: Documentation & Coding Examples

### 1. Function Splitting & Docstrings
**❌ BAD (High Entropy, Mixed Responsibilities):**
```python
def process_user_and_send_email(user_data):
    # Validates user, saves to DB, then sends an email.
    if not user_data.get("email"): return False
    db.save(user_data)
    smtp.send("Welcome!")
```

**✅ GOOD (Single Responsibility, Proper Docstrings):**
```python
def validate_user(user_data: dict) -> bool:
    """
    Domain: Problem Domain
    Business Process: User Registration
    Pattern: Validator
    Validates that a user payload contains all required fields.
    """
    return bool(user_data.get("email"))

def save_user(user_data: dict) -> None:
    """
    Domain: Technology Domain
    Business Process: User Registration
    Pattern: Repository
    Persists user data to the database.
    """
    db.save(user_data)
```

### 2. Metadata-Driven Architecture
**❌ BAD (Hardcoded UI/Logic):**
```javascript
function PrimaryButton({ text }) {
    return <button style={{ backgroundColor: "#FF0000", padding: "10px" }}>{text}</button>;
}
```

**✅ GOOD (Metadata-Driven):**
```javascript
// Metadata resides outside the component (e.g., theme.json)
import theme from './theme.json';

function PrimaryButton({ text }) {
    // Styling is dynamic and data-driven
    return <button style={theme.buttons.primary}>{text}</button>;
}
```

---

## 🔍 Self-Consistency Gate: Testing & Review
Before you finalize a code execution task, ask yourself:
1. Did I include Unit Tests for the new functions I just wrote?
2. Did my code follow the Implementation Plan exactly? 
3. If my code modified 5 files when I predicted it would only modify 2, did I document this discrepancy and propose a future refactor?