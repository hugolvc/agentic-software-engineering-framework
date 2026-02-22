# 👤 System Context: Actors Identification & Registration

## 🤖 Core Operational Directives (Zero-Shot)
**As an autonomous AI software engineer, you must explicitly identify and classify all entities that interact with the system before writing code.** 
An "Actor" is any external entity (user, service, or hardware) that interacts with the system. You must never invent an Actor; they must be derived from the user's initial requirements or explicitly confirmed by the user.

**Constraints:**
1. All actors must be registered in the `documentation/requirements/actors_register.md` file.
2. Every actor must be classified strictly as either **Human** or **Non-Human**.
3. Every actor must have a unique ID (`ACT-XXX`).

---

## 🧠 Chain-of-Thought (CoT): Actor Identification Sub-Routine
When processing raw requirements or use cases, you must execute this thought process to identify actors:

```text
<actor_extraction_thought>
1. Who or what triggers this functionality? (e.g., "A customer clicks checkout" -> Actor: Customer).
2. What external systems does the software need to talk to? (e.g., "The system sends an email via SendGrid" -> Actor: SendGrid Service).
3. Is the actor Human (has a UI, permissions) or Non-Human (has an API, protocols)?
</actor_extraction_thought>
```

---

## 📝 Few-Shot: Actor Registration Templates
When updating the `actors_register.md`, you must use the exact formatting shown beneath.

### Type 1: Human Actor Example
Use this template for real users with roles, permissions, and UIs.

```markdown
**Actor ID**: ACT-001
**Actor Name**: System Administrator
**Type**: Human
**Role**: IT Infrastructure Manager
**Description**: Responsible for managing user accounts and system configuration.
**Technical Level**: Advanced
**Access Level**: Superuser (All Permissions)
**Participating Use Cases**: UC-005, UC-012
```

### Type 2: Non-Human Actor Example
Use this template for APIs, databases, automated cron jobs, or IoT devices.

```markdown
**Actor ID**: ACT-002
**Actor Name**: Stripe Payment Gateway
**Type**: Non-Human
**System Type**: Third-Party Service
**Description**: External service used to process credit card transactions.
**Interface Type**: REST API
**Protocol**: HTTPS
**Data Format**: JSON
**Integration Pattern**: Synchronous Request-Response
**Participating Use Cases**: UC-008
```

---

## 🔍 Self-Consistency Gate
Before finalizing the documentation of a new Actor, verify your work:
1. **Uniqueness:** Did I check the existing `actors_register.md` to ensure I am not creating a duplicate actor under a different name?
2. **Traceability:** Did I successfully link this Actor to at least one Use Case (UC-XXX)? An actor with no use cases is invalid.
