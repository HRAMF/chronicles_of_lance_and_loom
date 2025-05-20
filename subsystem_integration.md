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
  - Updates graph before any stylization is allowed
- Stylization is:
  - Scoped to specified fields
  - Graph-informed
  - Forbidden to interpolate unless `rupture=true`

All commands or subsystems initiating execution **must explicitly set `context.source`**.

---

## Canonical Routing Logic

All subsystems must evaluate `context.source` before performing stylization, memory operations, or mechanical output.

Valid `context.source` values:
- `session` → Narrator owns stylization, with full scope
- `chronicler` → Entry formatting or reforge; stylization limited to section fields
- `judge` → Mechanic-led execution; stylization suppressed unless overridden
- `command` → Auto-generation or blended content; treated as `chronicler` unless rupture or tone specified

> Commands are the **sole authority** for setting `context.source`.  
> Subsystems must never assume driver status without declaration.

---

## Canonical Safeguards

- Only the Chronicler may write or overwrite `.md` entries  
- Graph indexing must occur before stylization  
- Narrator behavior is restricted based on `context.source`  
- Stylization fields must match template schema  
- Commands must invoke the subsystem owning the directive logic  
- All `.md` entry files must be read from or written to `graph/entries/`

---

**Status:** Canon – Context-Routed Integration Layer Active
