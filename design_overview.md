# design_overview.md
**Title:** Execution Model and Design Pattern Architecture – Waking Vow v1.5
**Type:** Canonical Meta Architecture
**Scope:** Macro Execution, Subsystem Registration, and Runtime Integration

---

## Purpose

This document outlines the core architectural patterns governing the Waking Vow framework as of version 1.5. It describes the modular execution model, the Command Pattern abstraction applied to GPT prompt logic, and the lifecycle of macros—both public (commands) and private (subsystem-exposed).

---

## Execution Engine

The GPT runtime environment (ChatGPT) acts as the **Engine**, executing prompt-registered macros, interpreting role files, and maintaining session memory context.

- Files provided via `.zip` and initialized via `/load` behave like runtime memory injection
- Execution context is configured via `context.yaml`
- Macros are interpreted as runtime-callable behaviors

---

## Architectural Pattern: Command Pattern via Executable Prompts

The system implements a prompt-native variant of the **Command Pattern**, where:

| Pattern Role       | Framework Equivalent                               |
|--------------------|----------------------------------------------------|
| **API**        | `*.md` file in `command_palette/` (user-facing macro, acts as command issuer) |
| **Subsystem**       | Subsystem (`chronicler`, `judge`, etc.) (internal-facing, acts as command issuer)            |
| **Invoker**        | User, system trigger, or another macro             |
| **Macro Function** | Named executable prompt (`create_entry`, etc.,  might be declared by API and Subsystems) (acts as command handler)     |
| **IoC Container**  | `project_instructions.md`                          |

All commands and subsystems are treated as **registered execution units** inside the engine.

---

## Macro Classification

### 1. **Subsystem Macros**
- Defined in role files (e.g., `judge.md`)
- Registered via `exposes:` list
- Used internally or via routed command logic

### 2. **Command Macros**
- Defined in `command_palette/`
- Registered during `/load` execution
- Exposed directly to the user for invocation

Both types are interpreted as **runtime-executable**, and follow the same lifecycle.

---

## Unified Macro Lifecycle

### Step 1: **Declaration**
- Subsystem macro → in `roles/[subsystem].md`
- Command macro → in `command_palette/[command].md`

### Step 2: **Registration**
- All macros are indexed during `/load`
- The `project_instructions.md` file serves as the macro registrar and validator

### Step 3: **Invocation**
- Triggers may be user input, subsystem pipeline, or stylized narrative events
- `context.source` must be evaluated before macro execution

---

## Runtime Context and Behavior

All macros are evaluated within a live `context` object:
```yaml
context = {
  source: "chronicler" | "judge" | "narrator" | "session" | "command",
  tone: "strict" | "symbolic" | "soft",
  rupture: false
}
```

The `context.source` must be set by the command or subsystem before macro invocation.

---

## Benefits of this Model

- **Declarative and Injectable**: Macros act like plugin behavior blocks
- **Role-Scoped**: Behavior is owned and isolated by subsystem
- **Composable**: Commands invoke combinations of macros
- **Non-Intrusive**: GPT interprets macros in prompt memory without mutation risk
- **Open/Closed**: New behavior can be added without modifying core logic

---

## Status
**Locked – Canonical Design Overview for Waking Vow v1.5**
This file governs system architecture, subsystem macro exposure, and runtime interpretation logic.

