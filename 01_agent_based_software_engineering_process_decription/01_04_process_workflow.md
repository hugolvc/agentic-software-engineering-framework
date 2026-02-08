# Process Workflow

## Overview

This document provides a comprehensive visual and logical representation of the Agent Based Software Engineering Process workflow. It shows how all methodology components integrate and interact, providing AI agents with a clear understanding of the complete process flow from project initialization through change implementation.

## Purpose

The Process Workflow document serves to:

- Provide a logical flow of the entire methodology
- Show how different components connect and interact
- Guide AI agents through the complete process
- Ensure all methodology components are addressed
- Identify decision points and process branches
- Clarify the sequence of activities

## High-Level Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROJECT INITIALIZATION                        │
│  (See: 01_03_project_initialization_guide.md)                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              REPOSITORY STRUCTURE SETUP                         │
│  - Create repository with methodology sub-repository            │
│  - Create documentation folder structure                        │
│  - Initialize all registers                                     │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              INITIAL REQUIREMENTS ANALYSIS                       │
│  - Identify Actors (02_02_actors_identification_description.md)│
│  - Identify Use Cases (02_03_use_cases_identification...)       │
│  - Identify Functional Requirements (02_04_functional...)       │
│  - Document Technology Stack (03_06_technology_stack...)        │
│  - Document NFRs (03_07_non_functional_requirements...)         │
│  - Document UI Guidelines (03_05_ui_styling_guidelines.md)       │
│  - Perform Software Sizing (05_01_software_sizing_description.md) │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│           CREATE INITIAL CHANGE REQUIREMENT                      │
│  (04_03_change_requirement_template.md)                         │
│  - Document change scope and rationale                          │
│  - Perform impact assessments                                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│            GENERATE IMPLEMENTATION PLAN                          │
│  (04_02_implementation_plan_template.md)                        │
│  - Address code entropy (03_02_code_entropy.md)                │
│  - Follow coding guidelines (03_03_coding_guidelines.md)       │
│  - Apply design patterns (03_04_patterns_use_guide.md)          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    IMPLEMENT CODE                                │
│  - Follow Implementation Plan                                   │
│  - Update documentation as needed                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
                    ┌────────────────┐
                    │  NEW CHANGE    │
                    │    REQUEST?    │
                    └────────┬───────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                   YES               NO
                    │                 │
                    │                 ▼
                    │        ┌─────────────────┐
                    │        │   PROJECT END    │
                    │        └─────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────────┐
│              CHANGE REQUEST PROCESS                              │
│  (01_02_process_description.md - Change Request Process)        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ANALYSIS PHASE                               │
│  1. Context Review                                               │
│     - Review accumulated documentation                          │
│     - Review Change Requirements history                        │
│     - Review Implementation Plans history                       │
│  2. Codebase Assessment                                         │
│     - Examine current implementation                            │
│     - Identify existing components and patterns                 │
│  3. Impact Assessment                                           │
│     - Determine scope and impact                                │
│     - Identify affected components                              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                CHANGE CLASSIFICATION                             │
│                                                                  │
│  ┌────────────────────────┐  ┌──────────────────────────┐     │
│  │ FUNCTIONAL CHANGE?     │  │ NON-FUNCTIONAL CHANGE?    │     │
│  └───────────┬─────────────┘  └────────────┬─────────────┘     │
│              │                            │                    │
│              ▼                            ▼                    │
│  ┌────────────────────────┐  ┌──────────────────────────┐   │
│  │ Functional Assessment  │  │ Non-Functional Assessment  │   │
│  │ (02_01_change_request_ │  │ (03_01_change_request_     │   │
│  │  assessment...)        │  │  assessment...)            │   │
│  │                        │  │                            │   │
│  │ - Actors?              │  │ - Technology Stack?         │   │
│  │ - Use Cases?           │  │ - NFRs?                    │   │
│  │ - Functional Reqs?     │  │ - Code Entropy?           │   │
│  └────────────────────────┘  └──────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              GUIDELINE IDENTIFICATION                            │
│  - Identify relevant methodology guidelines                     │
│  - Reference specific documentation sections                    │
│  - Functional Requirements Handling (Section 02)                │
│  - Non-Functional Requirements Handling (Section 03)            │
│  - Change Management (Section 04)                                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│           CREATE CHANGE REQUIREMENT                              │
│  (04_03_change_requirement_template.md)                         │
│  - Document change                                               │
│  - Perform assessments                                           │
│  - Document impact                                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│         GENERATE IMPLEMENTATION PLAN                              │
│  (04_02_implementation_plan_template.md)                         │
│                                                                  │
│  Address:                                                        │
│  - Code Entropy Analysis (03_02_code_entropy.md)               │
│  - Coding Guidelines (03_03_coding_guidelines.md)               │
│  - Design Patterns (03_04_patterns_use_guide.md)                │
│  - Technology Stack (03_06_technology_stack...)                 │
│  - NFRs (03_07_non_functional_requirements...)                  │
│  - UI Guidelines (03_05_ui_styling_guidelines.md)                │
│                                                                  │
│  Document Decisions:                                            │
│  - Identify decisions needed                                    │
│  - Analyze options with pros/cons/trade-offs                    │
│  - Make decisions with justification                            │
│  - Record in Decision Register (04_08_decision_register...)     │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    IMPLEMENT CODE                                │
│  - Follow Implementation Plan                                   │
│  - Update documentation                                         │
│  - Maintain traceability                                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              UPDATE DOCUMENTATION                                │
│  - Update Change Requirement status                             │
│  - Update Implementation Plan status                            │
│  - Update registers (actors, use cases, requirements)          │
│  - Update technology stack register                             │
│  - Update NFR register                                          │
│  - Update Decision Register (04_08_decision_register...)        │
│  - Update traceability matrix                                   │
│  - Update change history                                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             └─────────────────┐
                                               │
                                               ▼
                                    ┌─────────────────┐
                                    │  NEW CHANGE?    │
                                    └────────┬────────┘
                                             │
                                    ┌────────┴────────┐
                                    │                 │
                                   YES               NO
                                    │                 │
                                    │                 ▼
                                    │        ┌─────────────────┐
                                    │        │   PROJECT END    │
                                    │        └─────────────────┘
                                    │
                                    └─── (Loop back to Change Request Process)
```

## Detailed Process Steps

### Phase 1: Project Initialization

**Entry Point**: `01_03_project_initialization_guide.md`

1. Create repository with methodology sub-repository
2. Set up documentation folder structure
3. Initialize all registers:
   - Technology Stack Register
   - Non-Functional Requirements Register
   - UI Styling Guidelines Register (if applicable)
   - Decision Register
4. Create initial project documentation
5. Perform initial requirements analysis

### Phase 2: Initial Requirements Documentation

1. **Actors Identification** (`02_02_actors_identification_description.md`)
   - Identify all actors (human and non-human)
   - Document in actors register

2. **Use Cases Identification** (`02_03_use_cases_identification_description.md`)
   - Extract use cases from requirements
   - Link to actors
   - Document in use cases register

3. **Functional Requirements Identification** (`02_04_functional_requirements_identification_description.md`)
   - Extract functional requirements from use cases
   - Link to use cases and actors
   - Document in functional requirements register


4. **Software Sizing** (`05_01_software_sizing_description.md`)
   - Classify Use Cases by complexity
   - Calculate total Use Case Points (UCP)
   - Estimate effort in Agent Steps and Tokens

### Phase 3: Initial Change and Implementation

1. **Create Initial Change Requirement** (`04_03_change_requirement_template.md`)
   - Document initial implementation scope
   - Perform impact assessments

2. **Generate Initial Implementation Plan** (`04_02_implementation_plan_template.md`)
   - Address all methodology guidelines
   - Consider code entropy
   - Apply coding guidelines and patterns

3. **Implement Code**
   - Follow Implementation Plan
   - Update documentation

### Phase 4: Change Request Cycle

**Trigger**: New change request received

1. **Analysis Phase** (`01_02_process_description.md`)
   - Context Review
   - Codebase Assessment
   - Impact Assessment

2. **Change Classification**
   - Determine if functional, non-functional, or both
   - Perform appropriate assessments:
     - Functional: `02_01_change_request_assessment_description.md`
     - Non-Functional: `03_01_change_request_assessment_description.md`

3. **Guideline Identification**
   - Identify relevant methodology sections
   - Reference appropriate documentation

4. **Create Change Requirement**
   - Use template: `04_03_change_requirement_template.md`
   - Document all aspects of the change

5. **Generate Implementation Plan**
   - Use template: `04_02_implementation_plan_template.md`
   - Address all identified guidelines

6. **Implement Code**
   - Follow Implementation Plan
   - Maintain documentation

7. **Update Documentation**
   - Update all affected registers
   - Update traceability
   - Update change history

## Decision Points

### Change Classification Decision

```
Is the change functional, non-functional, or both?
│
├─ Functional Only
│  └─> Perform Functional Assessment (02_01)
│
├─ Non-Functional Only
│  └─> Perform Non-Functional Assessment (03_01)
│
└─ Both
   └─> Perform Both Assessments
```

### Assessment Decision Points

**Functional Assessment** (`02_01_change_request_assessment_description.md`):
- Does change affect Actors? → Update Actors Register
- Does change affect Use Cases? → Update Use Cases Register
- Does change affect Functional Requirements? → Update Functional Requirements Register

**Non-Functional Assessment** (`03_01_change_request_assessment_description.md`):
- Does change affect Technology Stack? → Update Technology Stack Register
- Does change affect NFRs? → Update NFR Register
- Does change require refactoring for entropy? → Plan refactoring

## Integration Points

### Methodology Components Integration

1. **Process Description** (`01_02_process_description.md`)
   - Defines overall process structure
   - Provides change request workflow

2. **Functional Requirements** (Section 02)
   - Actors, Use Cases, Functional Requirements
   - Change request assessment for functional changes

3. **Non-Functional Requirements** (Section 03)
   - Code Entropy, Coding Guidelines, Patterns
   - Technology Stack, NFRs, UI Guidelines
   - Change request assessment for non-functional changes

4. **Change Management** (Section 04)
   - Change Requirement Template
   - Implementation Plan Template
   - Change implementation process

### Documentation Registers Integration

All registers must be:
- Initialized during project setup
- Updated when relevant changes occur
- Referenced in Implementation Plans
- Maintained throughout project lifecycle

## Process Validation

At each phase, validate:

1. **Completeness**: All required documentation is created
2. **Consistency**: Documentation is consistent across registers
3. **Traceability**: Links between artifacts are maintained
4. **Compliance**: Methodology guidelines are followed
5. **Quality**: Documentation meets quality standards

## Best Practices

1. **Follow the Workflow**: Don't skip steps in the process
2. **Maintain Documentation**: Update documentation continuously
3. **Preserve History**: Keep all Change Requirements and Implementation Plans
4. **Maintain Traceability**: Link all related artifacts
5. **Reference Methodology**: Always refer to methodology documents
6. **Validate Continuously**: Verify compliance at each step

This Process Workflow provides AI agents with a complete understanding of how all methodology components work together to deliver software engineering projects in a controlled, predictable, and accurate manner.

