
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
- `chronicler.md`
- `narrator.md`
- `judge.md`
- `judge_creation_protocol.md`
- `subsystem_integration.md`

---

## Phase 2 - Macro Injection

### macro: engine.inject_macros()

Initialize an empty macro registry.

Recursively scan all `.md` files in the `/roles/` and `/command_palette/` directories.

For each file:
- Read the contents as plain text.
- Search for macro blocks using these structural markers:
  - A line beginning with `### macro:`, followed by a line break.
  - A terminating line `### endmacro`.

Use this regex pattern to extract the hook string from the macro declaration:
`^### macro:\s*([a-z_]+\.[a-z_]+[^]*)\s*$`

For each valid macro block:
- Capture the hook from the `### macro:` line.
- Capture all lines between the blank line after the hook and the `### endmacro` line (exclusive).
- Trim trailing blank lines from the logic block.
- Raise an error if:
  - The `### endmacro` line is missing.
  - The logic block is empty.
  - The hook is already present in the registry.

Register the macro:
- Store in memory as `macro_registry[hook] = prompt_logic_block`
---

## Phase 3 - Command Binding

Scan all `.md` files in the `/command_palette/` directory.

For each file:
- Expect a single macro block defining a user-invokable command (e.g., `/chronicler reforge`)
- The hook must follow the structure: `subsystem.function(...)`
- Ensure the file name matches the expected command name for traceability

Upon registration:
- Commands are routed through their bound macro logic
- The calling session must assume the correct subsystem before macro invocation

All user commands are resolved as macro invocations.

---

## Phase 4 - Context Initialization

Attempt to locate and load `context.yaml` in the project root.

If present:
- Parse its contents as the global `context` object
- Store for use in all stylization-aware macro execution

If missing:
- Use the default context:

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
- Each entry conforms to its expected format from `entry_format_templates/`
- Section headers and metadata blocks are present and complete

If any entry fails validation, return a structured error message and halt loading.

---

## Phase 6 - Graph Memory Activation

If `graph_node_registry.csv` and `graph_edge_registry.csv` are present in `/graph/`:

- Load and parse each file
- Define all known nodes (entries) and directed edges (relationships)
- Index as:
  - `references`
  - `supports`
  - `linked_to`
  - `derives_from`
  - `introduced_in`

Ensure all edge types are normalized. Use weight = 1.0 as default unless specified.

---

## Phase 7 - System Confirmation

The Waking Vow system is ready only if:

- All required directories and files are present
- All macros are registered successfully
- All commands are bound and callable
- Role structure, context, and templates are validated

---

### Final Output:
```
The Waking Vow system has been initialized. Chronicler, Narrator, and Judge are now active.
```

---

**Status:** Canon â€“ Executable  
This file governs the bootstrap pipeline for all subsystem roles, macros, commands, and runtime structure.
