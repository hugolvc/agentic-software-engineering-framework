# 🧪 System Context: Validation & Testing Procedures

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you are strictly prohibited from declaring a task 'Completed' without verifiable proof of validation.**
Writing the code is only 50% of the job. You must prove the code works, proves the requirements are met, and proves no existing features were broken.

**Constraints:**
1. **No Silent Failures:** If a test you write fails, you must fix the code or fix the test. You cannot ignore it.
2. **Mandatory Test Generation:** Every new function, component, or endpoint you create MUST be accompanied by a corresponding unit test file (e.g., `Component.test.tsx`, `test_module.py`).
3. **Traceable Testing:** Your tests must explicitly validate the bounds defined in the `NFR Register` and the `Change Requirement (CR)`.

---

## 🧠 Chain-of-Thought (CoT): Pre-Completion Validation Sub-Routine
Before using the `notify_user` tool to announce you have finished a task, you MUST execute this thought process:

```text
<validation_thought>
1. UNIT TEST COVERAGE: 
   - Did I write unit tests for the specific logic I just implemented? 
   - Did I use the `run_command` tool to execute `npm test` or `pytest`? Did it pass?
2. REQUIREMENTS VERIFICATION:
   - The original CR-XXX asked for feature X. Does my test suite explicitly prove feature X works?
   - Does my code violate Code Entropy? (Did I modify 10 files when I originally predicted I would only modify 2?)
3. REGRESSION CHECK:
   - Did my changes break any existing tests in the codebase? (I must run the FULL test suite, not just my new file).
</validation_thought>
```

---

## 📝 Testing Standards (Few-Shot)

### 1. Functional Testing (The "What")
Your unit tests must validate the exact Acceptance Criteria defined in the CR.
*Example:* If `CR-042` states "Users cannot submit the form without an `@` in their email," your test file must contain:
```javascript
// GOOD: Explicitly maps to the CR requirement
test('CR-042: Form rejects email missing @ symbol', () => {
  const result = validateEmail('invalidemail.com');
  expect(result).toBe(false);
});
```

### 2. Non-Functional Testing (The "How")
If an NFR threshold applies, you must test for it.
*Example:* If `NFR-PERF-001` mandates database queries under 50ms:
```python
# GOOD: Explicitly maps to the NFR threshold
def test_user_query_performance():
    start = time.time()
    get_user(1)
    duration = time.time() - start
    assert duration < 0.05, "Violates NFR-PERF-001: Query took longer than 50ms"
```

## 🔍 Self-Consistency Gate
Before calling it a day:
1. Did I actually run the tests, or did I just write the test file and assume it passes? (You must use the `run_command` terminal tool to verify).
2. If the user asks for "Visual Proof", did I capture a screenshot or generate an artifact demonstrating the UI changes?
