# subsystem_integration.md
**Subsystem Integration Protocol – The Waking Vow**  
**Version:** 1.4.1 (Modular Roles & Context-Driven Execution)  
**Purpose:** Define role interaction logic, context-aware stylization, and adaptive command collaboration.

---

## Active Subsystems

- **Chronicler** – Manages entry structure, formatting, versioning, and graph memory  
- **Narrator** – Stylizes expressive output based on source context  
- **Judge** – Resolves mechanical behavior and `.yml` integrity

---

## Adaptive Handoff Protocols

Subsystems collaborate through two primary execution models:

### 1. Session Workflow (Narrator-Driven)
- Invoked when `context.source = session`
- Narrator leads user-facing interaction
- May invoke:
  - `chronicler.capture()` for entry formation
  - `judge.interpret()` or `judge.audit()` for mechanical outcomes
- Full stylization is permitted
- Graph indexing occurs post-Narrator confirmation

### 2. Content Generation / Command-Driven (Subsystem-Initiated)
- Invoked when `context.source = chronicler`, `judge`, or `command`
- The initiating subsystem:
  - Executes creation, transformation, or audit logic
  - Invokes `narrator.stylize_section(entry, section)` if stylization is required
  - Updates graph
