# Software Sizing Description (Use Case Points for AI Agents)

## Overview

Software Sizing is the process of estimating the size and effort required for a software development task. For AI Agents operating within this framework, we utilize an adapted version of **Use Case Points (UCP)**. This method aligns perfectly with the **Use Case Register** already required by the methodology.

## Purpose

1.  ** predictability**: Provide a consistent metric to estimate the complexity of a task before execution.
2.  **Resource Management**: Estimate the **Tokens** (cost) and **Agent Steps** (time/compute) required.
3.  **Entropy Correlation**: Correlate size with **Code Entropy** to identify high-risk changes.

## The Metric: Agent Use Case Points (A-UCP)

Standard UCP measures size based on the number of transactions and actors. For AI Agents, we simplify this into a **Complexity Weighting** system applied to each Use Case in the Use Case Register.

### 1. Complexity Classification

Every Use Case must be classified into one of three complexity levels:

| Complexity | Criteria | Weight (UCP) |
| :--- | :--- | :--- |
| **Simple** | - < 4 Steps in Main Scenario<br>- < 3 Entities involved<br>- No external API calls | **5** |
| **Average** | - 4-7 Steps in Main Scenario<br>- 3-7 Entities involved<br>- Standard API calls | **10** |
| **Complex** | - > 7 Steps in Main Scenario<br>- > 7 Entities involved<br>- Complex logic, error handling, or multiple external systems | **15** |

### 2. Effort Estimation (The "Agent Velocity")

Unlike human effort (measured in man-hours), AI Agent effort is measured in **Steps** and **Tokens**.

**Baseline Conversion Formula:**
These values should be calibrated based on project history.

*   **1 UCP ≈ 2 Agent Execution Loops (Steps)**
*   **1 Agent Step ≈ 2,500 Tokens (Input + Output)**

#### Example Usage:
A project has:
-   2 Simple Use Cases (2 * 5 = 10 UCP)
-   1 Complex Use Case (1 * 15 = 15 UCP)
**Total Size**: 25 UCP

**Estimated Effort**:
-   **Steps**: 25 UCP * 2 = **50 Steps**
-   **Tokens**: 50 Steps * 2,500 = **125,000 Tokens**

## Integration with Process

1.  **Identification**: During **Initial Requirements Analysis** or **Change Request Assessment**, identify and classify Use Cases.
2.  **Registration**: Record the `Complexity` and `UCP` in the **Use Case Register**.
3.  **Planning**: implementation Plans must reference the total UCP to justify the predicted entropy and resource allocation.
4.  **Calibration**: After implementation, update the "Actual Steps" and "Actual Tokens" in the **History** to refine the conversion formula.

## Best Practices

*   **Don't Overthink It**: Sizing is an estimate, not a guarantee. Use the "Simple/Average/Complex" buckets quickly.
*   **Re-evaluate**: If a "Simple" Use Case turns out to need 20 files changed, re-classify it as "Complex" and update the register.
*   **Traceability**: Ensure every UCP is traceable to a specific Use Case ID.
