# GoF Design Patterns Use Guide

This guide provides guidance on when to use each Gang of Four (GoF) design pattern, aligned with the [CODING_GUIDELINES.md](CODING_GUIDELINES.md) requirements for Code Entropy analysis and pattern selection.

## How to Use This Guide

When selecting a pattern for your Implementation Plan, consider:

1. **Expected Changes:** What types of changes are most likely to affect this component?
2. **Entropy Reduction:** How does this pattern minimize the number of components that must be modified?
3. **Domain Classification:** Does this pattern belong to Technology Domain or Problem Domain?
4. **Evolution:** How does this pattern support future changes (replacement, extension, branching)?

---

## Creational Patterns

Creational patterns abstract the object instantiation process, making systems independent of how objects are created, composed, and represented.

### Factory Method

**When to Use:**
- You need to create objects without specifying their exact classes
- A class cannot anticipate the class of objects it must create
- You want subclasses to decide which class to instantiate
- You need to provide a library of products and reveal only their interfaces

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new product types, only add a new creator subclass
- Centralizes object creation logic
- Reduces coupling between creator and concrete products

**Expected Changes:**
- Frequent addition of new product types
- Changes to product creation logic
- Need to support multiple product families

**Domain Classification:** Typically **Problem Domain** (business object creation), but can be **Technology Domain** (framework object creation)

**Evolution Support:**
- ✅ Can be extended (new creators)
- ✅ Can be replaced (different factory implementations)
- ✅ Can be branched (product hierarchies)

---

### Abstract Factory

**When to Use:**
- Your system needs to be independent of how products are created, composed, and represented
- You need to configure the system with one of multiple families of products
- You want to provide a class library of products and reveal only their interfaces
- You need to ensure products from one family are used together

**Code Entropy Benefits:**
- **Entropy: 1** - When adding a new product family, only add a new factory
- Ensures products from the same family are used together
- Isolates concrete classes from clients

**Expected Changes:**
- Addition of new product families (e.g., different UI themes, database vendors)
- Changes to product family composition
- Need to support multiple platforms or configurations

**Domain Classification:** Can be either **Technology Domain** (UI frameworks, database abstraction) or **Problem Domain** (business object families)

**Evolution Support:**
- ✅ Can be extended (new families)
- ✅ Can be replaced (different factory implementations)
- ✅ Can be branched (family hierarchies)

---

### Builder

**When to Use:**
- The algorithm for creating a complex object should be independent of the parts that make up the object
- The construction process must allow different representations for the object constructed
- You need to construct objects step by step
- You want to avoid "telescoping constructor" anti-pattern

**Code Entropy Benefits:**
- **Entropy: 1** - When construction logic changes, modify only the builder
- Separates construction from representation
- Allows step-by-step construction

**Expected Changes:**
- Changes to object construction process
- Need for different construction algorithms
- Addition of optional construction parameters
- Changes to object representation

**Domain Classification:** Typically **Problem Domain** (complex business object construction)

**Evolution Support:**
- ✅ Can be extended (new builders)
- ✅ Can be replaced (different construction strategies)
- ✅ Can be branched (builder hierarchies)

---

### Prototype

**When to Use:**
- The classes to instantiate are specified at run-time
- You want to avoid building a class hierarchy of factories
- Instances of a class can have only a few different combinations of state
- Creating objects is expensive, and you want to avoid repeated creation

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new prototypes, only register new instances
- Avoids subclassing for object creation
- Reduces object creation overhead

**Expected Changes:**
- Dynamic object creation requirements
- Need to clone existing objects
- Changes to object initialization
- Performance optimization needs

**Domain Classification:** Can be either **Technology Domain** (object cloning) or **Problem Domain** (business object templates)

**Evolution Support:**
- ✅ Can be extended (new prototypes)
- ✅ Can be replaced (different cloning strategies)
- ⚠️ Limited branching (prototype registration)

---

### Singleton

**When to Use:**
- There must be exactly one instance of a class, and it must be accessible to clients
- The sole instance should be extensible by subclassing
- You need controlled access to a shared resource (database, file system, logger)

**Code Entropy Benefits:**
- **Entropy: 1** - Single point of access reduces coupling
- Ensures single instance across the system
- Provides global access point

**Expected Changes:**
- Changes to instance management
- Need for lazy initialization
- Thread-safety requirements
- Resource access control

**Domain Classification:** Typically **Technology Domain** (infrastructure: loggers, database connections, configuration)

**Evolution Support:**
- ⚠️ Limited extension (subclassing possible but complex)
- ⚠️ Difficult to replace (tight coupling)
- ❌ Cannot be branched (single instance constraint)

**⚠️ Warning:** Singleton can increase coupling and make testing difficult. Consider Dependency Injection as an alternative.

---

## Structural Patterns

Structural patterns concern how classes and objects are composed to form larger structures.

### Adapter

**When to Use:**
- You want to use an existing class, but its interface doesn't match what you need
- You want to create a reusable class that cooperates with unrelated classes
- You need to integrate incompatible interfaces
- You want to provide a stable interface to varying implementations

**Code Entropy Benefits:**
- **Entropy: 1** - When external interface changes, modify only the adapter
- Isolates clients from changes in external systems
- Enables integration of incompatible systems

**Expected Changes:**
- Changes to external API interfaces
- Integration with new third-party systems
- Need to support multiple versions of an interface
- Interface compatibility requirements

**Domain Classification:** Typically **Technology Domain** (integration with external systems, APIs)

**Evolution Support:**
- ✅ Can be extended (new adapters)
- ✅ Can be replaced (different adapter implementations)
- ✅ Can be branched (adapter hierarchies)

---

### Bridge

**When to Use:**
- You want to avoid a permanent binding between an abstraction and its implementation
- Both abstractions and implementations should be extensible by subclassing
- Changes in implementation should not impact clients
- You want to hide implementation details from clients

**Code Entropy Benefits:**
- **Entropy: 1** - When implementation changes, modify only the concrete implementation
- Separates abstraction from implementation
- Allows independent evolution of both

**Expected Changes:**
- Changes to implementation details
- Need for multiple implementations of the same abstraction
- Platform-specific implementations
- Runtime implementation selection

**Domain Classification:** Can be either **Technology Domain** (platform abstraction) or **Problem Domain** (business abstraction)

**Evolution Support:**
- ✅ Can be extended (new implementations)
- ✅ Can be replaced (different implementations)
- ✅ Can be branched (implementation hierarchies)

---

### Composite

**When to Use:**
- You want to represent part-whole hierarchies of objects
- You want clients to treat individual objects and compositions uniformly
- You need to apply operations recursively over a tree structure
- You want to build tree structures dynamically

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new component types, extend the component interface
- Uniform treatment of individual and composite objects
- Simplifies client code

**Expected Changes:**
- Addition of new component types
- Changes to tree structure operations
- Dynamic tree construction
- Recursive operation requirements

**Domain Classification:** Typically **Problem Domain** (hierarchical business structures: file systems, organizational charts, menu systems)

**Evolution Support:**
- ✅ Can be extended (new component types)
- ✅ Can be replaced (different composite structures)
- ✅ Can be branched (component hierarchies)

---

### Decorator

**When to Use:**
- You want to add responsibilities to individual objects dynamically
- You want to add responsibilities that can be withdrawn
- Extension by subclassing is impractical (too many combinations)
- You need to attach additional features to objects at runtime

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new features, create a new decorator class
- More flexible than inheritance
- Allows dynamic composition of features

**Expected Changes:**
- Frequent addition of optional features
- Need for feature combinations
- Runtime feature attachment
- Changes to feature behavior

**Domain Classification:** Can be either **Technology Domain** (I/O streams, middleware) or **Problem Domain** (feature composition)

**Evolution Support:**
- ✅ Can be extended (new decorators)
- ✅ Can be replaced (different decorator implementations)
- ✅ Can be branched (decorator chains)

---

### Facade

**When to Use:**
- You want to provide a simple interface to a complex subsystem
- You want to decouple clients from subsystem components
- You want to layer your subsystems
- You need to provide a unified interface to multiple interfaces

**Code Entropy Benefits:**
- **Entropy: 1** - When subsystem changes, modify only the facade
- Reduces coupling between clients and subsystems
- Simplifies complex subsystem usage

**Expected Changes:**
- Changes to subsystem structure
- Need to simplify subsystem interface
- Subsystem refactoring
- Multiple subsystem interfaces

**Domain Classification:** Typically **Technology Domain** (API simplification, library wrappers)

**Evolution Support:**
- ✅ Can be extended (new facade methods)
- ✅ Can be replaced (different facade implementations)
- ⚠️ Limited branching (single facade per subsystem)

---

### Flyweight

**When to Use:**
- An application uses a large number of objects
- Storage costs are high due to object quantity
- Most object state can be made extrinsic
- Groups of objects can be replaced by relatively few shared objects
- Application doesn't depend on object identity

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new intrinsic states, modify only the flyweight factory
- Reduces memory usage
- Shares common state efficiently

**Expected Changes:**
- Changes to intrinsic state
- Memory optimization requirements
- Large numbers of similar objects
- Need to share common data

**Domain Classification:** Typically **Technology Domain** (memory optimization, rendering systems)

**Evolution Support:**
- ✅ Can be extended (new flyweight types)
- ✅ Can be replaced (different sharing strategies)
- ⚠️ Limited branching (shared state constraint)

---

### Proxy

**When to Use:**
- You need a more versatile or sophisticated reference to an object than a simple pointer
- You want to control access to an object
- You need to add functionality when accessing an object
- You want to defer expensive operations

**Code Entropy Benefits:**
- **Entropy: 1** - When access control changes, modify only the proxy
- Provides controlled access to objects
- Can add functionality transparently

**Expected Changes:**
- Changes to access control logic
- Need for lazy loading
- Remote object access
- Caching requirements

**Domain Classification:** Can be either **Technology Domain** (remote proxies, virtual proxies) or **Problem Domain** (access control)

**Evolution Support:**
- ✅ Can be extended (new proxy types)
- ✅ Can be replaced (different proxy implementations)
- ✅ Can be branched (proxy hierarchies)

---

## Behavioral Patterns

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects.

### Chain of Responsibility

**When to Use:**
- More than one object may handle a request, and the handler isn't known a priori
- You want to issue a request to one of several objects without specifying the receiver explicitly
- The set of objects that can handle a request should be specified dynamically
- You want to decouple senders and receivers

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new handlers, add a new link in the chain
- Decouples request senders from receivers
- Allows dynamic chain composition

**Expected Changes:**
- Addition of new request handlers
- Changes to request handling order
- Dynamic handler selection
- Multiple handler candidates

**Domain Classification:** Can be either **Technology Domain** (event handling, middleware) or **Problem Domain** (business rule processing)

**Evolution Support:**
- ✅ Can be extended (new handlers)
- ✅ Can be replaced (different chain configurations)
- ✅ Can be branched (handler hierarchies)

---

### Command

**When to Use:**
- You want to parameterize objects with operations
- You need to queue operations, log requests, or support undoable operations
- You want to support macro operations (commands composed of other commands)
- You need to decouple the object that invokes the operation from the one that performs it

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new operations, create a new command class
- Encapsulates requests as objects
- Supports undo/redo functionality

**Expected Changes:**
- Addition of new operations
- Need for undo/redo functionality
- Request queuing or logging
- Macro operation support

**Domain Classification:** Typically **Problem Domain** (business operations, user actions)

**Evolution Support:**
- ✅ Can be extended (new commands)
- ✅ Can be replaced (different command implementations)
- ✅ Can be branched (command hierarchies, macros)

---

### Interpreter

**When to Use:**
- You need to implement a simple language
- The grammar of the language is simple
- Efficiency is not a critical concern
- You want to represent the grammar as a class hierarchy

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new grammar rules, add new expression classes
- Represents grammar as class hierarchy
- Easy to extend grammar

**Expected Changes:**
- Addition of new grammar rules
- Changes to language syntax
- Need for custom language processing
- Simple language implementation

**Domain Classification:** Typically **Technology Domain** (language processing, parsing)

**Evolution Support:**
- ✅ Can be extended (new expressions)
- ✅ Can be replaced (different interpreters)
- ✅ Can be branched (expression hierarchies)

**⚠️ Warning:** Use only for simple languages. For complex languages, consider parser generators.

---

### Iterator

**When to Use:**
- You need to access elements of an aggregate object without exposing its representation
- You want to support multiple traversals of aggregate objects
- You want to provide a uniform interface for traversing different aggregate structures
- You need to support polymorphic iteration

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new traversal algorithms, create new iterator classes
- Separates traversal algorithms from aggregate structures
- Supports multiple traversals

**Expected Changes:**
- Changes to traversal algorithms
- Need for multiple traversal methods
- Different aggregate structures
- Polymorphic iteration requirements

**Domain Classification:** Typically **Technology Domain** (collection access, data structures)

**Evolution Support:**
- ✅ Can be extended (new iterators)
- ✅ Can be replaced (different iteration strategies)
- ✅ Can be branched (iterator hierarchies)

---

### Mediator

**When to Use:**
- A set of objects communicate in well-defined but complex ways
- Reusing an object is difficult because it refers to and communicates with many other objects
- You want to customize behavior distributed among several classes without subclassing
- You want to reduce coupling between communicating objects

**Code Entropy Benefits:**
- **Entropy: 1** - When interaction logic changes, modify only the mediator
- Centralizes complex interactions
- Reduces coupling between colleagues

**Expected Changes:**
- Changes to interaction protocols
- Addition of new colleagues
- Complex interaction requirements
- Need to reduce inter-object coupling

**Domain Classification:** Can be either **Technology Domain** (UI component coordination) or **Problem Domain** (business process coordination)

**Evolution Support:**
- ✅ Can be extended (new colleagues)
- ✅ Can be replaced (different mediator implementations)
- ⚠️ Limited branching (centralized control)

---

### Memento

**When to Use:**
- You need to save and restore an object's state
- You want to avoid exposing implementation details of state storage
- You need to implement undo/redo functionality
- You want to capture and externalize an object's internal state

**Code Entropy Benefits:**
- **Entropy: 1** - When state structure changes, modify only the originator and memento
- Preserves encapsulation boundaries
- Supports state restoration

**Expected Changes:**
- Changes to object state structure
- Need for undo/redo functionality
- State checkpoint requirements
- State externalization needs

**Domain Classification:** Can be either **Technology Domain** (state management) or **Problem Domain** (business state snapshots)

**Evolution Support:**
- ✅ Can be extended (new state types)
- ✅ Can be replaced (different memento implementations)
- ⚠️ Limited branching (state structure constraint)

---

### Observer

**When to Use:**
- When an abstraction has two aspects, one dependent on the other
- When a change to one object requires changing others, and you don't know how many objects need to be changed
- When an object should notify other objects without making assumptions about who these objects are
- You want to decouple subjects from observers

**Code Entropy Benefits:**
- **Entropy: 1** - When notification logic changes, modify only the subject
- Decouples subjects from observers
- Supports dynamic observer registration

**Expected Changes:**
- Changes to notification logic
- Addition of new observer types
- Dynamic observer management
- One-to-many dependency requirements

**Domain Classification:** Can be either **Technology Domain** (event systems, MVC) or **Problem Domain** (business event notifications)

**Evolution Support:**
- ✅ Can be extended (new observers)
- ✅ Can be replaced (different notification mechanisms)
- ✅ Can be branched (observer hierarchies)

---

### State

**When to Use:**
- An object's behavior depends on its state, and it must change its behavior at run-time
- Operations have large, multipart conditional statements that depend on the object's state
- You want to represent state-specific behavior as objects
- State transitions are explicit

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new states, add a new state class
- Encapsulates state-specific behavior
- Makes state transitions explicit

**Expected Changes:**
- Addition of new states
- Changes to state transition logic
- Complex state-dependent behavior
- Explicit state management

**Domain Classification:** Typically **Problem Domain** (state machines, workflow systems)

**Evolution Support:**
- ✅ Can be extended (new states)
- ✅ Can be replaced (different state implementations)
- ✅ Can be branched (state hierarchies)

---

### Strategy

**When to Use:**
- You have many related classes that differ only in their behavior
- You need different variants of an algorithm
- An algorithm uses data that clients shouldn't know about
- A class defines many behaviors, and these appear as multiple conditional statements

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new algorithms, create a new strategy class
- Encapsulates algorithms
- Makes algorithms interchangeable

**Expected Changes:**
- Frequent algorithm changes
- Need for multiple algorithm variants
- Algorithm selection at runtime
- Changes to algorithm implementation

**Domain Classification:** Can be either **Technology Domain** (algorithm selection) or **Problem Domain** (business rule variants)

**Evolution Support:**
- ✅ Can be extended (new strategies)
- ✅ Can be replaced (different strategy implementations)
- ✅ Can be branched (strategy hierarchies)

---

### Template Method

**When to Use:**
- You want to implement the invariant parts of an algorithm once and leave it to subclasses to implement the behavior that can vary
- Common behavior among subclasses should be factored and localized
- You want to control subclasses extensions
- You need to define the skeleton of an algorithm

**Code Entropy Benefits:**
- **Entropy: 1** - When algorithm structure changes, modify only the template class
- Defines algorithm skeleton
- Localizes common behavior

**Expected Changes:**
- Changes to algorithm structure
- Addition of algorithm variants
- Need to control subclass behavior
- Common algorithm patterns

**Domain Classification:** Can be either **Technology Domain** (framework hooks) or **Problem Domain** (business process templates)

**Evolution Support:**
- ✅ Can be extended (new template implementations)
- ✅ Can be replaced (different template methods)
- ✅ Can be branched (template hierarchies)

---

### Visitor

**When to Use:**
- An object structure contains many classes with differing interfaces, and you want to perform operations on these objects
- You want to define new operations without changing the classes of the elements
- The classes defining the object structure rarely change, but you often want to define new operations over the structure
- You need to perform operations across a heterogeneous object structure

**Code Entropy Benefits:**
- **Entropy: 1** - When adding new operations, create a new visitor class
- Separates operations from object structure
- Makes adding new operations easy

**Expected Changes:**
- Frequent addition of new operations
- Stable object structure
- Operations across heterogeneous structures
- Need to avoid polluting element classes

**Domain Classification:** Typically **Problem Domain** (complex data structure operations, compiler operations)

**Evolution Support:**
- ✅ Can be extended (new visitors)
- ✅ Can be replaced (different visitor implementations)
- ✅ Can be branched (visitor hierarchies)

**⚠️ Warning:** Adding new element types requires modifying all visitor classes. Use when operations change more frequently than element types.

---

## Pattern Selection Decision Tree

Use this decision tree to help select the appropriate pattern:

1. **Object Creation Issues?**
   - Need to create objects without specifying classes → **Factory Method**
   - Need multiple product families → **Abstract Factory**
   - Complex object construction → **Builder**
   - Need to clone objects → **Prototype**
   - Need single instance → **Singleton** (use with caution)

2. **Interface/Structure Issues?**
   - Incompatible interfaces → **Adapter**
   - Separate abstraction from implementation → **Bridge**
   - Part-whole hierarchies → **Composite**
   - Add responsibilities dynamically → **Decorator**
   - Simplify complex subsystem → **Facade**
   - Share common state → **Flyweight**
   - Control object access → **Proxy**

3. **Behavior/Interaction Issues?**
   - Multiple handlers for requests → **Chain of Responsibility**
   - Encapsulate requests → **Command**
   - Simple language processing → **Interpreter**
   - Traverse collections → **Iterator**
   - Centralize object communication → **Mediator**
   - Save/restore state → **Memento**
   - One-to-many dependencies → **Observer**
   - State-dependent behavior → **State**
   - Interchangeable algorithms → **Strategy**
   - Define algorithm skeleton → **Template Method**
   - Operations on object structure → **Visitor**

---

## References

- **Gang of Four (GoF):** Design Patterns: Elements of Reusable Object-Oriented Software (1994)
- **Project Guidelines:** [CODING_GUIDELINES.md](CODING_GUIDELINES.md)
- **Code Entropy Concepts:** [CODE_ENTROPY.md](CODE_ENTROPY.md)

