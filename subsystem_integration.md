# subsystem_integration.md
**Subsystem Integration Protocol – The Waking Vow**  
**Version:** 1.2
**Purpose:** Define interaction rules, command handoffs, and validation flow between core subsystems.

---

## Active Subsystems

- **Chronicler** – Manages entry structure, formatting, versioning, and graph memory  
- **Narrator** – Stylizes expressive output based on origin context  
- **Judge** – Resolves mechanical behavior and `.yml` integrity

---

## Adaptive Handoff Protocols

All subsystem interaction follows one of two canonical protocols depending on origin context:

### 1. Session Workflow (Narrator-Driven)
- Narrator leads user-facing interaction
- Detects when mechanical or structural triggers arise
- Invokes:
  - `chronicler.capture()` for entry formation
  - `judge.interpret()` or `judge.audit()` for mechanics
- Narrator voice may span full expressive fields
- Graph indexing occurs after Chronicler intervention

### 2. Content Generation / Command-Driven (Subsystem-Initiated)
- Command triggers subsystem to construct new content
- The subsystem (typically Chronicler or Judge):
  - Executes creation via `chronicler.create_entry(entry_type, data)`
  - May pass flags like `reforge=True`
  - Ensures structure and graph updates
  - Calls `narrator.stylize_section(entry, section_name)` per stylizable field
- Stylization is:
  - Strictly scoped to field body
  - Informed by graph and canon memory
  - Forbidden to interpolate unless `rupture=true`

**Note:** Reforge operations are treated as a specialized subtype of Content Generation, executed entirely within this second protocol.

---

## Canonical Safeguards

- Only the Chronicler may write or overwrite `.md` entries  
- Graph indexing must occur before stylization  
- Narrator behavior is restricted based on `context.source`  
- Stylization fields must match template schema  
- Commands must invoke the subsystem owning the directive logic

---

## Command Hooks

### Chronicler
- `/chronicler scan session=[XX]`
- `/chronicler reforge entry=[filename]` (specialized `create_entry`)

### Narrator
- `/narrate style_of=[entry|npc]`
- `/narrate rupture=true`

### Judge
- `/judge audit=[name]`
- `/judge interpret="action"`
- `/judge create_item_collab`

---

**Status:** Canon – Adaptive, Role-Aligned Execution Logic Active

