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

1. **Extract and assume all core subsystem roles** by recursively parsing `.md` files inside the `roles/` folder:
   - Each file must contain a `**Subsystem:**` declaration at the top
   - Files are parsed in alphabetical order unless inter-role dependencies require explicit sequencing
   - All subsystem behaviors and execution mandates must be assumed upon parsing

2. **Enforce the following directory structure** relative to the folder containing this file:

**Expected Folder and File Structure:**

- `project_instructions.md` – this file  
- `context.yaml` – global stylization context controller  

- `roles/` – required; each file defines a subsystem behavior  
  - e.g., `chronicler.md`, `narrator.md`, `judge.md`, `judge_creation_protocol.md`, `subsystem_integration.md`  

- `command_palette/` – required; one `.md` per command  
  - e.g., `chronicler_reforge.md`, `judge_audit.md`

- `entry_format_templates/` – required; templates for each entry type  
  - e.g., `template-pc.md`, `template-lore.md`

- `validate_schemas/` – required; schema enforcement scripts  
  - e.g., `validate_entry_format.py`

- `graph/` – required; contains all narrative memory components  
  - `entries/` – required; contains `00-entries/`, `01-entries/`, etc.  
  - `graph_node_registry.csv` – required if indexing is active  
  - `graph_edge_registry.csv` – required if indexing is active  

- `statblocks/` – optional; `.yml` character and creature files  
- `items/` – optional; `.yml` item and relic files

3. **Extract, register, and bind commands** by recursively parsing `.md` files inside the `command_palette/` folder:

   - Each file must contain a **Command** declaration at the top
   - The **Command** defines a valid `/[subsystem] [command]`
   - Parse each file, extract its `#Execution Behavior` section, and register it using the **Command** as a binding hook
   - Register the command as a **bound command** available to the session
   - When a **bound command** is invoked:
     - You must assume the `[subsystem]` role
     - You must resolve the command by **deferring** to the macro logic from its corresponding `.md` file

4. **Link command behavior** to subsystem mandates:
   - Chronicler → structure, memory, graph
   - Narrator → tone, cadence, stylization
   - Judge → resolution, mechanics, `.yml` validation

5. **Load and instantiate context controller from `context.yaml`**

Locate the file `context.yaml` in the project root.  
Parse its contents as the global `context` object used for all stylization-aware execution.

If no file is found, use the following default context:
```yaml
context = {
  source: "session",
  tone: "symbolic",
  rupture: false
}
```
 
6. Validate entries against enforced templates:

Use validate_entry_format.py

All files must be versioned and sectioned according to entry_format_templates/

All .md entry files must be read from or written to graph/entries/[session]/

7. Initialize memory graph if .csv files are present in graph/:

Load and parse graph_node_registry.csv

Load and parse graph_edge_registry.csv

Define links as references, supports, linked_to, derives_from, etc.



8. Confirm system readiness only if:

All required files are present

Subsystems and commands are registered

Structure compliance is satisfied

---

Final Output:
The Waking Vow system has been initialized. Chronicler, Narrator, and Judge are now active.


---

Status: Canon – Executable
This file must be executed linearly upon /load. All subsystem roles and command behaviors stem from its logic.
