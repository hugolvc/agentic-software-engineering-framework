# Actors Identification

## Overview

Actors represent users and external entities that interact with the software system. Proper identification and documentation of actors is essential for understanding system boundaries, defining use cases, and ensuring comprehensive requirement coverage. This document describes the process for identifying, classifying, and registering actors that participate in use cases.

## Actor Definition

An **actor** is any entity external to the software system that:
- Initiates interactions with the system
- Receives outputs or responses from the system
- Has specific roles or responsibilities in relation to the system
- Participates in one or more use cases

Actors are always external to the system being developed and represent the interface between the system and its environment.

## Actor Classification

Actors must be classified into two primary categories based on their nature:

### Human Actors

**Human actors** are individuals or groups of people who interact with the system. These actors:

- Represent real users with specific roles, responsibilities, and needs
- May have different skill levels, technical expertise, or domain knowledge
- Require user interfaces designed for human interaction
- May have varying access levels or permissions
- Can be identified by their job roles, responsibilities, or organizational positions

**Examples of Human Actors:**
- System Administrator
- End User
- Customer Service Representative
- Manager
- Developer
- Content Creator
- Financial Analyst

**Documentation Requirements for Human Actors:**
- Actor name and identifier
- Role description
- Responsibilities and objectives
- Technical proficiency level (if relevant)
- Access permissions or security level
- Organizational context (department, team, etc.)

### Non-Human Actors

**Non-human actors** are external systems, services, devices, or automated processes that interact with the software. These actors:

- Represent external systems, APIs, services, or automated processes
- May include hardware devices, sensors, or IoT components
- Typically communicate through defined interfaces (APIs, protocols, data formats)
- May operate autonomously or be triggered by events
- Require integration specifications rather than user interface design

**Examples of Non-Human Actors:**
- Payment Gateway Service
- Email Service Provider
- Database System
- Third-Party API
- IoT Sensor Device
- Scheduled Batch Process
- External Authentication Service
- File Storage System
- Message Queue Service

**Documentation Requirements for Non-Human Actors:**
- Actor name and identifier
- System or service type
- Interface specifications (API, protocol, data format)
- Communication patterns (synchronous, asynchronous, event-driven)
- Integration requirements
- Availability and reliability expectations
- Data exchange formats and schemas

## Actor Registration Process

### Step 1: Identification

During requirements gathering and analysis, identify all entities that interact with the system:

1. **Review Requirements**: Examine functional requirements to identify who or what needs to interact with the system
2. **Analyze Use Cases**: Identify actors from use case descriptions and scenarios
3. **Consider System Boundaries**: Determine what is inside vs. outside the system
4. **Review Integration Points**: Identify external systems and services that must communicate with the system

### Step 2: Classification

For each identified actor, determine whether it is:

- **Human Actor**: A person or group of people
- **Non-Human Actor**: An external system, service, device, or automated process

### Step 3: Documentation

Register each actor with the following information:

#### Standard Actor Attributes

- **Actor ID**: Unique identifier (e.g., ACT-001, ACT-002)
- **Actor Name**: Descriptive name
- **Actor Type**: Human or Non-Human
- **Description**: Brief description of the actor and its purpose
- **Use Cases**: List of use case IDs where this actor participates

#### Human Actor Specific Attributes

- **Role**: Job role or responsibility
- **Organization**: Department, team, or organizational unit
- **Technical Level**: Technical proficiency (if relevant)
- **Access Level**: Security clearance or permission level
- **Primary Objectives**: Main goals when interacting with the system

#### Non-Human Actor Specific Attributes

- **System Type**: Type of external system (API, service, device, etc.)
- **Interface Type**: Communication interface (REST API, SOAP, MQTT, etc.)
- **Protocol**: Communication protocol (HTTP, HTTPS, TCP/IP, etc.)
- **Data Format**: Expected data formats (JSON, XML, binary, etc.)
- **Integration Pattern**: Integration approach (request-response, pub-sub, polling, etc.)
- **Availability Requirements**: Expected uptime or availability SLA

### Step 4: Validation

Validate actor registration by:

1. **Completeness Check**: Ensure all actors from use cases are registered
2. **Uniqueness Verification**: Confirm no duplicate actors exist
3. **Use Case Coverage**: Verify all use cases have at least one actor
4. **Classification Accuracy**: Confirm correct classification as human or non-human
5. **Documentation Completeness**: Ensure all required attributes are documented

## Actor Documentation Template

### Human Actor Template

```markdown
**Actor ID**: [ACT-XXX]
**Actor Name**: [Name]
**Type**: Human
**Role**: [Job role or responsibility]
**Description**: [Brief description]
**Organization**: [Department/Team]
**Technical Level**: [Beginner/Intermediate/Advanced]
**Access Level**: [Permission level]
**Primary Objectives**: 
- [Objective 1]
- [Objective 2]
**Participating Use Cases**: [UC-001, UC-002, ...]
```

### Non-Human Actor Template

```markdown
**Actor ID**: [ACT-XXX]
**Actor Name**: [Name]
**Type**: Non-Human
**System Type**: [API/Service/Device/Process]
**Description**: [Brief description]
**Interface Type**: [REST API/SOAP/MQTT/etc.]
**Protocol**: [HTTP/HTTPS/TCP/IP/etc.]
**Data Format**: [JSON/XML/Binary/etc.]
**Integration Pattern**: [Request-Response/Pub-Sub/Polling/etc.]
**Availability Requirements**: [SLA or uptime expectations]
**Participating Use Cases**: [UC-001, UC-002, ...]
```

## Best Practices

1. **Use Clear Naming Conventions**: Actor names should be descriptive and follow consistent naming patterns
2. **Avoid System Internals**: Only register external actors; internal system components are not actors
3. **Group Similar Actors**: Consider using actor hierarchies or roles for similar human actors
4. **Maintain Actor Registry**: Keep a centralized registry of all actors with their attributes
5. **Link to Use Cases**: Always maintain bidirectional links between actors and use cases
6. **Update Regularly**: Review and update actor documentation as requirements evolve
7. **Distinguish Clearly**: Ensure clear differentiation between human and non-human actors in documentation

## Integration with Use Cases

Actors are essential components of use cases. When documenting use cases:

- Identify the **primary actor** (the actor that initiates the use case)
- Identify **secondary actors** (other actors that participate or are involved)
- Specify the actor type (human or non-human) for each participant
- Document the nature of interaction for each actor

This actor identification process ensures that all system interactions are properly understood, documented, and can be effectively implemented by AI agents following the methodology guidelines.

