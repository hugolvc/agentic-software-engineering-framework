# Use Cases Identification

## Overview

Use cases represent specific interactions between actors and the software system to achieve particular goals. They describe what the system does from the user's perspective and serve as the foundation for functional requirements. This document describes the process for identifying, documenting, and registering use cases within the Agent Based Software Engineering Process methodology.

## Use Case Definition

A **use case** is a description of a sequence of actions performed by the system and its actors to achieve a specific goal. Each use case:

- Represents a discrete unit of functionality
- Has a clear, measurable goal or outcome
- Involves one or more actors
- Describes interactions from the actor's perspective
- Can be executed independently or as part of a larger workflow

Use cases capture functional requirements in a way that is understandable to both stakeholders and AI agents, providing clear context for implementation.

## Use Case Characteristics

### Essential Elements

Every use case must have:

1. **Unique Identifier**: A reference code for tracking and linking
2. **Name**: A clear, descriptive name that indicates the goal
3. **Primary Actor**: The actor that initiates the use case
4. **Goal**: The objective or outcome the use case achieves
5. **Preconditions**: Conditions that must be met before the use case can execute
6. **Main Success Scenario**: The primary sequence of steps leading to success
7. **Postconditions**: The state of the system after successful completion

### Optional Elements

Use cases may also include:

- **Secondary Actors**: Other actors that participate in the use case
- **Alternative Flows**: Variations or exceptions to the main scenario
- **Error Handling**: How the system handles failures or errors
- **Business Rules**: Constraints or rules that apply to the use case
- **Non-Functional Requirements**: Performance, security, or other quality attributes

## Use Case Registration Process

### Step 1: Identification

Identify use cases through various methods:

1. **Requirements Analysis**: Extract use cases from functional requirements documents
2. **Actor Analysis**: For each registered actor, identify what they need to accomplish
3. **Stakeholder Interviews**: Gather use cases from discussions with stakeholders
4. **Business Process Review**: Analyze business processes to identify system interactions
5. **System Boundary Definition**: Identify interactions at system boundaries

### Step 2: Validation

Validate that each identified use case:

- Has a clear, specific goal
- Involves at least one actor (previously registered)
- Represents a complete interaction from start to finish
- Is at an appropriate level of detail (not too granular, not too abstract)
- Is independent or clearly related to other use cases

### Step 3: Documentation

Document each use case with comprehensive information following the registration template.

### Step 4: Linking

Establish relationships:

- Link use cases to their participating actors (both primary and secondary)
- Identify relationships between use cases (includes, extends, generalizes)
- Link use cases to functional requirements
- Associate use cases with relevant business rules or constraints

## Use Case Documentation Template

### Basic Use Case Template

```markdown
**Use Case ID**: [UC-XXX]
**Use Case**: [UC-001] [Use Case Name]
**Actor**: [Actor Name]
**Goal**: [What the actor wants to achieve]
**Complexity**: [Simple/Average/Complex] (See 05_01_software_sizing_description.md)
**Size**: [5/10/15] UCP
**Description**: [Brief description of what the use case accomplishes]

**Primary Actor**: 
[Actor ID and Name]

**Secondary Actors**: 
- [Actor ID and Name] (if applicable)
- [Actor ID and Name] (if applicable)

**Goal**: 
[The specific goal or outcome this use case achieves]

**Scope**: 
[The system or subsystem this use case applies to]

**Preconditions**: 
- [Condition 1 that must be true before execution]
- [Condition 2 that must be true before execution]

**Main Success Scenario**: 
1. [Step 1: Actor action or system response]
2. [Step 2: Actor action or system response]
3. [Step 3: Actor action or system response]
...

**Alternative Flows**: 
- [Alt-1]: [Description of alternative path]
  - [Steps for alternative flow]
- [Alt-2]: [Description of alternative path]
  - [Steps for alternative flow]

**Error Flows**: 
- [Error-1]: [Description of error condition]
  - [How the system handles this error]
- [Error-2]: [Description of error condition]
  - [How the system handles this error]

**Postconditions**: 
- [State 1 after successful completion]
- [State 2 after successful completion]

**Business Rules**: 
- [Rule 1 that applies to this use case]
- [Rule 2 that applies to this use case]

**Non-Functional Requirements**: 
- [NFR-1]: [Non-functional requirement related to this use case]
- [NFR-2]: [Non-functional requirement related to this use case]

**Related Use Cases**: 
- [UC-XXX]: [Relationship type: includes/extends/generalizes]
- [UC-YYY]: [Relationship type: includes/extends/generalizes]

**Related Requirements**: 
- [REQ-XXX]: [Related functional requirement]
- [REQ-YYY]: [Related functional requirement]

**Notes**: 
[Any additional information, assumptions, or clarifications]
```

## Use Case Relationships

### Types of Relationships

Use cases can have the following relationships:

1. **Includes**: A use case that always includes another use case
   - The included use case is a mandatory part of the including use case
   - Example: "Authenticate User" is included in "Process Payment"

2. **Extends**: A use case that optionally extends another use case
   - The extending use case adds optional behavior
   - Example: "Apply Discount" extends "Process Payment"

3. **Generalizes**: A parent-child relationship between use cases
   - The child use case inherits and specializes the parent's behavior
   - Example: "Process Credit Card Payment" generalizes "Process Payment"

### Documenting Relationships

When documenting relationships:

- Clearly specify the relationship type
- Document the direction of the relationship
- Explain the purpose or reason for the relationship
- Ensure relationships are bidirectional in documentation

## Use Case Levels

### User Goal Level (Primary)

These are the main use cases that represent complete user goals:

- Typically correspond to one user session
- Have clear business value
- Are the primary focus for implementation

**Example**: "Place Order", "Generate Report", "Manage Account"

### Subfunction Level

These are use cases that support user goal level use cases:

- Often included or extended by higher-level use cases
- Represent reusable functionality
- May be shared across multiple primary use cases

**Example**: "Validate Input", "Calculate Total", "Send Notification"

### Summary Level

These are high-level use cases that group related user goal level use cases:

- Provide overview of major system capabilities
- Useful for system overview and planning
- Typically broken down into user goal level use cases

**Example**: "Order Management", "User Management", "Reporting"

## Best Practices

1. **Use Clear, Action-Oriented Names**: Use case names should be verbs or verb phrases (e.g., "Place Order" not "Ordering")

2. **One Goal Per Use Case**: Each use case should have a single, clear goal

3. **Actor Perspective**: Write use cases from the actor's perspective, focusing on what they do and what they see

4. **Appropriate Granularity**: 
   - User goal level use cases should take 2-20 minutes to complete
   - Avoid overly detailed or overly abstract use cases

5. **Complete Scenarios**: Ensure main success scenarios are complete and lead to the stated goal

6. **Consistent Formatting**: Use consistent templates and formatting across all use cases

7. **Maintain Traceability**: Keep clear links between use cases, actors, and requirements

8. **Version Control**: Track versions of use cases as they evolve

9. **Review and Refine**: Regularly review use cases for clarity, completeness, and accuracy

10. **Avoid Implementation Details**: Focus on what the system does, not how it does it (at the use case level)

## Use Case Registry

Maintain a centralized registry of all use cases that includes:

- **Use Case Index**: List of all use cases with IDs, names, and status
- **Actor-Use Case Matrix**: Mapping of actors to their participating use cases
- **Use Case Dependencies**: Graph or table showing relationships between use cases
- **Requirements Traceability**: Links between use cases and functional requirements

## Integration with Actors

Use cases must reference previously registered actors:

- **Primary Actor**: Must be a registered actor (human or non-human)
- **Secondary Actors**: All secondary actors must be registered
- **Actor Validation**: Verify that all actors referenced in use cases exist in the actor registry

When registering a use case, if a required actor is not yet registered, the actor must be registered first following the process described in "2_1_actors_identification.md".

## Integration with Change Management

When changes are requested:

1. **Impact Analysis**: Identify which use cases are affected by the change
2. **Use Case Updates**: Update affected use cases or create new ones
3. **Version Tracking**: Maintain version history of use case changes
4. **Documentation Updates**: Update use case documentation as part of the change implementation

This use case identification and registration process ensures that functional requirements are properly captured, documented, and can be effectively implemented by AI agents following the methodology guidelines.

