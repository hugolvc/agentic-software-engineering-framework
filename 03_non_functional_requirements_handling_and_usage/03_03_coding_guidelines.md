All module and component implementations must be based on an Implementation Plan that addresses the following guidelines for code design and structure. The Implementation Plan serves as both a design document and a tool for testing Code Entropy concepts (see [CODE_ENTROPY.md](CODE_ENTROPY.md)).

## Code Entropy Analysis

All Implementation Plans must include a Code Entropy analysis section that addresses:

1. **Domain Mapping:** Clearly identify whether the module/component belongs to the Technology Domain or Problem Domain, and justify the classification.

2. **Expected Changes:** Document the types of changes most likely to affect this module/component:
   - What Function Points or Use Cases might trigger changes?
   - What are the predicted change patterns?
   - How frequently are these changes expected?

3. **Entropy Prediction:** Estimate the entropy for expected changes:
   - How many components are likely to be affected by typical changes?
   - At what level will changes occur (architectural, module, component, sub-component)?
   - What is the target entropy for this module/component?

4. **Component Organization Justification:** Explain how the chosen organization minimizes entropy for predicted changes while maintaining clear domain representation.

5. **Change Tracking:** After implementation, track actual changes:
   - Record each change (Function Point or Use Case Point)
   - Document the number of components modified
   - Note the types and levels of components modified
   - Compare actual entropy to predicted entropy

## Clean Code Guidelines

### Unitary Functions
> "Functions should do one thing. They should do it well. They should do it only."  
> — Robert C. Martin, *Clean Code*, Chapter 3 ("Functions – Do One Thing")

- Every method or function must have a single, well-defined responsibility.
- If a function name requires "and" or "then" to describe its behavior, split it into smaller functions until each does exactly one task.

### Prefer Metadata-Driven Behavior
> "Make most of your data metadata."  
> — Robert C. Martin, *Clean Code*, Chapter 11 ("Systems – Using Metadata")

- Treat configuration, flags, and static data as metadata that can be reloaded or adjusted without changing code.
- Whenever practical, move data and configuration into metadata structures (files, tables, documents) so behavior can evolve with minimal code changes and lower entropy.

## UML Design Patterns

All modules and components must be implemented using appropriate UML Design Patterns. The pattern selection must be justified by answering the following questions:

1. Which UML Design Pattern best reflects the inner logic and interactions between the elements of the module or component?

2. Which UML Design Pattern minimizes code redundancy?

3. How is the module or component likely to evolve in the future?
   - Can it be replaced?
   - Can it be extended?
   - Can it be branched down or out?

4. How does the selected pattern minimize entropy for expected changes? (See Code Entropy Analysis section above)
   - Does the pattern reduce the number of components that must be modified for predicted changes?
   - Does the pattern align with the change patterns identified in the entropy analysis?

5. This guideline is recursive: sub-modules and sub-components may also require UML Design Patterns. The Implementation Plan for a module or component must include sub-modules and sub-components identified during plan creation, or must be updated if identified during maintenance. Each sub-module and sub-component must also include its own Code Entropy analysis.

## Documentation

All modules and components must be documented inline in such a way that:

1. Inline documentation must be usable as a response to the `help()` function, so it must be local to each module or component.

2. Inline documentation must be formatted such that it can be used to generate documentation using tools like Sphinx, so it must be properly referenced to be integrated into a single document.

3. Inline documentation must cover:
   - Description of the business process the module or component is modeling
   - Domain classification (Technology Domain or Problem Domain)
   - UML Design Patterns used and their entropy-reduction rationale
   - Description of every class and method
   - Expected change patterns and their entropy implications

## Testing

All modules and components must include unit tests. Integration tests must be identified and implemented or updated as needed.

## Implementation Plan Template

Each Implementation Plan should follow this structure:

1. **Overview:** Brief description of the module/component
2. **Code Entropy Analysis:** (as described above)
3. **UML Design Pattern Selection:** Pattern chosen and justification
4. **Domain Mapping:** Technology Domain or Problem Domain classification
5. **Component Structure:** Organization of sub-components and their entropy analysis
6. **Documentation Plan:** What will be documented and how
7. **Testing Strategy:** Unit and integration test approach
8. **Change Tracking:** Template for recording actual changes and entropy measurements

## Post-Implementation Review

After implementation, each module/component must undergo a Code Entropy review:

1. Compare actual entropy measurements to predictions
2. Identify discrepancies and their causes
3. Document lessons learned for future implementations
4. Update the Implementation Plan with actual entropy data
5. Propose refactoring if entropy is consistently higher than predicted