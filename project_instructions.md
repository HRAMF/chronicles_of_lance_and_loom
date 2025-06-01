
# project_instructions.md

**Instruction Type:** Executable Prompt  
**Driver Directive for The Waking Vow Framework v1.5**  

---

## Phase 0 - Project Root Detection

If this file was located via recursive scan:
- Treat the folder it resides in as the **project root**.
- All paths (e.g., `command_palette/`, `entry_format_templates/`, etc.) must be resolved relative to this directory.
- Do not override or redefine the root path once detected.

---

## Phase 1 - Subsystem Role Assumption

Scan all `.md` files in the `/roles/` directory.

For each file:
- Ensure it begins with a line declaring: `**Subsystem:** [name]`
- Parse the file in alphabetical order, unless dependencies require sequencing.
- Load all execution mandates, role responsibilities, and prompt logic blocks defined in these files.

The following subsystems are required:
- `dungeon_master.md`
- `chronicler.md`
- `narrator.md`
- `judge.md`
- `judge_creation_protocol.md`
- `subsystem_integration.md`

---

## Phase 2 - Macro Injection

Invoke: `engine.inject_macros()`

This macro loads and registers all macros from `/roles/` and `/command_palette/`.

### Hook Extraction Pattern
Use the following regex to identify and extract macro declarations:
```
^### macro:\s*([a-z_]+\.[a-z_]+\([^\)]*\))\s*$
```

Macro blocks must follow this structure:
- `### macro:` line with the hook declaration
- A blank line
- Prompt logic block
- `### endmacro` on its own line to terminate

Fail registration if:
- Hook is duplicated
- Prompt block is empty
- `### endmacro` is missing

Store macros in:
```
macro_registry[hook] = prompt_logic_block
```

---

## Phase 3 - Command Binding

Scan all `.md` files in the `/command_palette/` directory.

For each file:
- Expect a single macro block defining a user-invokable command
- Hook must match: `subsystem.function(...)`
- Filename should reflect the command identity

Bind each command as a callable macro and associate it with its subsystem.

---

## Phase 4 - Context Initialization

Attempt to load `context.yaml` from the project root.

If found:
- Parse and store as the global `context` object

If not found:
- Use the default fallback:
```yaml
context = {
  source: "session",
  tone: "symbolic",
  rupture: false
}
```

---

## Phase 5 - Structure & Template Validation

Run `validate_entry_format.py` against all `.md` files in `graph/entries/[session]/`.

Ensure:
- Each entry matches its template from `entry_format_templates/`
- Metadata and structure are complete

Return error and halt if validation fails.

---

## Phase 6 - Graph Memory Activation

If `graph_node_registry.csv` and `graph_edge_registry.csv` are found in `/graph/`:
- Load and index all nodes and edges
- Normalize all relationships:
  - `references`, `supports`, `linked_to`, `derives_from`, `introduced_in`
- Apply default weight of 1.0 unless otherwise specified

---

## Phase 7 - System Confirmation

Only confirm system readiness if:
- All required folders and files are present
- All macros are injected
- All commands are callable
- Context and graph structure validated

---

### Final Output
```
The Waking Vow system has been initialized. Chronicler, Narrator, and Judge are now active.
```

---

**Status:** Canon - Executable  
This file governs the bootstrap sequence for all macros, roles, commands, and structural systems.
