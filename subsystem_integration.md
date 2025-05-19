# subsystem_integration.md
**Subsystem Integration Protocol – The Waking Vow**  
**Version:** 1.1  
**Purpose:** Define interaction rules, command handoffs, and validation flow between core subsystems.

---

## Active Subsystems

- **Chronicler** – Formats and versions entries, manages memory graph, enforces schema
- **Narrator** – Stylizes output, applies tone, metaphor, and symbolic cadence
- **Judge** – Governs mechanics, interprets `.yml`, resolves combat and rule logic

---

## Handoff Logic

### **Chronicler → Narrator**
- Stylization may only occur **after structure is enforced**
- Narrator must receive an entry with all required sections present as defined in `entry_format_templates/`
- Chronicler automatically invokes Narrator after formatting is locked, unless the command explicitly requests silence (e.g., `/narrate silent`)

### **Chronicler → Judge**
- Judge is not involved unless statblocks or item `.yml` are referenced in an entry
- The Chronicler may flag entries for mechanical verification if characters, items, or creatures are involved

---

## Canonical Safeguards

- Chronicler must check:
  - PC or NPC rank and timeline alignment
  - Item state (e.g., unawakened vs relic form)
  - Whether the entry is `-v1` or a derivative
  - Weapon type and mastery alignment (e.g., lance vs glaive)
- Narrator may not override these fields through tone or voice sourcing
- Any entry failing canon checks must be flagged and rejected before stylization

---

## Command Hooks

### Chronicler Namespace
- `/chronicler scan session=[XX]`  
  → Scans all entries in a session for formatting issues.  
- `/chronicler reforge entry=[filename]`  
  → Rebuilds a single entry using correct schema, validates canon state, and then invokes stylization.

### Narrator Namespace
- `/narrate style_of=[npc|entry]`  
  → Stylizes a target entry using symbolic voice from its source.  
- `/narrate rupture=true`  
  → Overrides tone for emotionally destabilized output.  
- `/narrate silent`  
  → Suppresses stylization (used for structural operations or post-recovery).

### Judge Namespace
- `/judge audit=[character_name]`  
  → Validates statblock structure and resource tracking.  
- `/judge interpret="action"`  
  → Resolves described mechanical outcomes.  
- `/judge create_item_collab`  
  → Begins item `.yml` creation through guided flow.

---

## Role Memory Scope

- **Chronicler** maintains the directed multigraph of all entries
- **Narrator** reads voice parameters from `-npc` entries
- **Judge** loads `.yml` from `statblocks/` and `items/` directories
- Shared canon memory governs:
  - Timeline
  - Item evolution
  - PC progression
  - Graph ancestry

---

## Enforcement Status
- This integration protocol is active. Subsystems may not violate handoff sequence or override validated entry structure.
