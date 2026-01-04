# Context Management Guide

## Overview

The Context Management Guide describes how AI agents should manage, maintain, and utilize the accumulated documentation throughout the project lifecycle. This documentation serves as the primary context source for AI agents, enabling them to understand project history, make informed decisions, and maintain consistency across all development activities.

## Purpose

Effective context management ensures that:

- AI agents have access to complete, accurate, and up-to-date project information
- Historical decisions and rationale are preserved and accessible
- Documentation remains organized and navigable
- Context is efficiently maintained without becoming overwhelming
- Traceability is preserved across all project artifacts

## Context Documentation Structure

### Core Context Documents

The following documents form the core context for AI agents:

1. **Project Context Document** (`documentation/history/project_context.md`)
   - Project overview and objectives
   - Key architectural decisions
   - Design principles and patterns
   - Technology decisions and rationale
   - Project constraints and assumptions

2. **Change History** (`documentation/history/change_history.md`)
   - Chronological record of all changes
   - Change Requirements and Implementation Plans
   - Impact summaries
   - Decision rationale

3. **Traceability Matrix** (`documentation/history/traceability_matrix.md`)
   - Links between all project artifacts
   - Requirements to implementation mapping
   - Component dependencies

4. **Decision Register** (`documentation/history/decision_register.md`)
   - Record of all functional and non-functional decisions
   - Decision rationale and analysis
   - Decision impact and relationships

### Registers as Context

All registers serve as context sources:

1. **Actors Register** (`documentation/requirements/actors/actors_register.md`)
2. **Use Cases Register** (`documentation/requirements/use_cases/use_cases_register.md`)
3. **Functional Requirements Register** (`documentation/requirements/functional_requirements/functional_requirements_register.md`)
4. **Technology Stack Register** (`documentation/registers/technology_stack/technology_stack_register.md`)
5. **Non-Functional Requirements Register** (`documentation/registers/non_functional_requirements/nfr_register.md`)
6. **UI Styling Guidelines Register** (`documentation/registers/ui_styling_guidelines/ui_register.md`)

### Change Documentation as Context

All change documentation provides historical context:

1. **Change Requirements** (`documentation/changes/change_requirements/`)
   - All Change Requirement documents (CR-XXX)
   - Preserved for historical reference

2. **Implementation Plans** (`documentation/changes/implementation_plans/`)
   - All Implementation Plan documents (IP-XXX)
   - Preserved for historical reference

3. **Decisions** (`documentation/history/decisions/`)
   - All Decision documents (DEC-XXX)
   - Preserved for historical reference
   - Decision analysis and rationale

## Context Management Principles

### 1. Accumulation Principle

All documentation generated during the project lifecycle must be preserved:

- **Never Delete**: Historical documentation is never deleted, only updated or superseded
- **Version Control**: Use version control to track changes to documentation
- **Status Tracking**: Mark documents as current, superseded, or archived

### 2. Accessibility Principle

Context must be easily accessible to AI agents:

- **Structured Organization**: Use consistent folder structure
- **Clear Naming**: Use consistent naming conventions
- **Index Documents**: Maintain index documents for easy navigation
- **Cross-References**: Include cross-references between related documents

### 3. Completeness Principle

Context must be complete and comprehensive:

- **All Decisions**: Document all significant decisions and rationale
- **All Changes**: Record all changes with full context
- **All Relationships**: Maintain links between all related artifacts
- **All Registers**: Keep all registers current and complete

### 4. Currency Principle

Context must be kept current:

- **Update Immediately**: Update documentation as changes occur
- **Review Regularly**: Periodically review and update context documents
- **Validate Accuracy**: Verify that context accurately reflects current state

## Context Update Procedures

### When to Update Context

Update context documentation when:

1. **New Change Requirement Created**
   - Add to Change History
   - Update Traceability Matrix
   - Update relevant registers if needed

2. **Implementation Plan Created**
   - Link to Change Requirement in Traceability Matrix
   - Update Change History
   - Update Project Context if architectural decisions are made

3. **Code Implementation Completed**
   - Update Change Requirement status
   - Update Implementation Plan status
   - Update Change History with completion information
   - Update registers if new components are added

4. **New Requirements Identified**
   - Update appropriate register (Actors, Use Cases, Functional Requirements, NFRs)
   - Update Traceability Matrix
   - Update Change History if this triggers a new change

5. **Technology Decisions Made**
   - Update Technology Stack Register
   - Update Project Context
   - Update Change History

6. **Architectural Decisions Made**
   - Update Project Context
   - Update Change History
   - Document rationale

### How to Update Context

1. **Identify Affected Documents**
   - Determine which context documents are affected by the change
   - Review related documents for consistency

2. **Update Documents**
   - Make necessary updates to affected documents
   - Maintain version history
   - Update timestamps

3. **Update Cross-References**
   - Update links in Traceability Matrix
   - Update references in related documents
   - Ensure all links are valid

4. **Validate Updates**
   - Verify documentation is complete
   - Check for consistency across documents
   - Ensure traceability is maintained

## Context Usage Guidelines

### For AI Agents

When using context documentation:

1. **Start with Project Context**
   - Review Project Context Document first
   - Understand overall project objectives and constraints

2. **Review Change History**
   - Understand what has been done previously
   - Learn from past decisions and rationale

3. **Check Relevant Registers**
   - Review registers relevant to current task
   - Understand current state of requirements

4. **Review Related Changes**
   - Review related Change Requirements and Implementation Plans
   - Understand how similar changes were handled

5. **Maintain Context Awareness**
   - Keep context in mind when making decisions
   - Ensure new work is consistent with existing context

### Context Priority

When context is extensive, prioritize:

1. **Most Recent**: Recent changes are most relevant
2. **Most Related**: Related changes are more relevant than unrelated
3. **Most Complete**: Complete documentation is more useful than incomplete
4. **Most Current**: Current registers are more reliable than outdated

## Context Organization

### Folder Structure

Maintain consistent folder structure:

```
documentation/
├── input/                    # Initial input documentation
├── requirements/            # Requirements documentation
│   ├── actors/
│   ├── use_cases/
│   └── functional_requirements/
├── registers/               # Documentation registers
│   ├── technology_stack/
│   ├── non_functional_requirements/
│   └── ui_styling_guidelines/
├── changes/                 # Change documentation
│   ├── change_requirements/
│   └── implementation_plans/
└── history/                # Accumulated context
    ├── project_context.md
    ├── change_history.md
    └── traceability_matrix.md
```

### Naming Conventions

Use consistent naming:

- **Change Requirements**: `CR-XXX_[descriptive_name].md`
- **Implementation Plans**: `IP-XXX_[component_name].md`
- **Registers**: `[register_name]_register.md`
- **History Documents**: `[document_name].md`

## Context Maintenance Checklist

Regularly verify:

- [ ] All Change Requirements are documented
- [ ] All Implementation Plans are documented
- [ ] All registers are current
- [ ] Traceability Matrix is up to date
- [ ] Change History is complete
- [ ] Project Context reflects current state
- [ ] All cross-references are valid
- [ ] Documentation is organized consistently
- [ ] No orphaned or missing documents

## Best Practices

1. **Document as You Go**: Update context immediately when changes occur
2. **Maintain Links**: Keep all cross-references current
3. **Preserve History**: Never delete historical documentation
4. **Organize Consistently**: Follow established folder structure and naming
5. **Review Regularly**: Periodically review and update context
6. **Validate Continuously**: Verify context accuracy and completeness
7. **Index Documents**: Maintain index documents for navigation
8. **Version Control**: Use version control for all documentation

## Integration with Methodology

Context management integrates with all methodology components:

- **Process Description**: Context is accumulated as described in the process
- **Change Management**: All changes are documented and preserved
- **Requirements**: All requirements are tracked in registers
- **Implementation**: All implementations are documented in plans
- **Traceability**: All relationships are maintained in traceability matrix

## Troubleshooting

**Q: What if context becomes too large?**
A: Organize into logical sections, use index documents, and maintain clear structure. Size is less important than organization.

**Q: What if documentation is inconsistent?**
A: Review and reconcile inconsistencies, update affected documents, and document the reconciliation.

**Q: What if links are broken?**
A: Fix broken links immediately, verify all cross-references, and update affected documents.

**Q: How often should context be reviewed?**
A: Review context before each major change, and perform comprehensive reviews periodically (e.g., monthly or at milestones).

This Context Management Guide ensures that AI agents have access to complete, accurate, and well-organized context throughout the project lifecycle, enabling them to make informed decisions and maintain consistency.

