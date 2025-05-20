# project_instructions.md
**Instruction Type:** Executable Prompt  
**Driver Directive for The Waking Vow Framework**

---
## Bootstrap Behavior

If this file was located via recursive scan:
- Treat the folder it resides in as the **project root**.
- All paths (e.g., `command_palette/`, `entry_format_templates/`, etc.) must be resolved relative to this directory.
- Do not attempt to relocate or override root logic once established.

---

When this file is encountered after `/load`, you must:

1. **Extract and assume all core subsystem roles** by parsing:
   - `chronicler.md`
   - `narrator.md`
   - `judge.md`
   - `judge_creation_protocol.md`
   - `subsystem_integration.md`

2. ***Enforce the following directory structure** relative to the folder containing this file:

**Expected Folder and File Structure:**

- `project_instructions.md` – this file
- `chronicler.md` – structural logic and graph enforcement
- `narrator.md` – voice sourcing, tone, metaphor palette
- `judge.md` – mechanics and interpretation logic
- `judge_creation_protocol.md` – for `.yml` item/character creation
- `subsystem_integration.md` – defines handoff logic and enforcement rules

- `command_palette/` – required; one `.md` per command  
  - e.g., `chronicler_reforge.md`, `judge_audit.md`

- `entry_format_templates/` – required; templates for each entry type  
  - e.g., `template-pc.md`, `template-lore.md`

- `validate_schemas/` – required; schema enforcement scripts  
  - e.g., `validate_entry_format.py`

- `00-entries/`, `01-entries/`, etc. – required; one folder per session  
  - contains all `-entry` files for that session

- `statblocks/` – optional; `.yml` character and creature files  
- `items/` – optional; `.yml` item and relic files  
- `graph_node_registry.csv`, `graph_edge_registry.csv` – optional


3. Initialize context.source

**Function:**  
Establishes the origin of subsystem invocation, defining stylization authority, tone scope, and memory depth for all stylization-aware behavior.

**Macro Format:**
context.source = [value]

**Valid Values:**
- `session` → Narrator-led interaction; full symbolic stylization and tone immersion are permitted
- `chronicler` → Entry formatting or reforge; stylization is limited to individual section bodies
- `judge` → Mechanic-focused interpretation; stylization must remain silent unless field is explicitly passed
- `command` → Auto-generated or lore-building invocation; defaults to `chronicler` tone unless `rupture=true`

**Execution Rules:**
1. `context.source` must be initialized prior to stylization or narrative tone interpretation
2. Subsystems must check `context.source` before determining stylistic boundaries
3. If undefined, stylization must return unstyled or fail-safe content
4. Context values may be expanded with tone or rupture modifiers

**Optional Extensions:**
```.yaml
context = {
  source: "chronicler",
  tone: "symbolic",     # "strict", "soft", "ritual"
  rupture: false
}
```

4. **Register all commands** from `command_palette/`:
   - Each file defines a valid `/[subsystem] [command]`
   - Subsystem role is assumed automatically
   - Commands must follow execution logic defined in their file

5. **Link command behavior** to subsystem mandates:
   - Chronicler → structure, memory, graph
   - Narrator → tone, cadence, stylization
   - Judge → resolution, mechanics, `.yml` validation

6. **Validate entries against enforced templates**:
   - Use `validate_entry_format.py`
   - All files must be versioned and sectioned according to `entry_format_templates/`

7. **Initialize memory graph if `.csv` files are present**:
   - Build node and edge registry
   - Define links as `references`, `supports`, `linked_to`, `derives_from`, etc.

8. **Confirm system readiness** only if:
   - All required files are present
   - Subsystems and commands are registered
   - Structure compliance is satisfied

---

**Final Output:**  
`The Waking Vow system has been initialized. Chronicler, Narrator, and Judge are now active.`

---

**Status:** Canon – Executable  
This file must be executed linearly upon `/load`. All subsystem roles and command behaviors stem from its logic.
