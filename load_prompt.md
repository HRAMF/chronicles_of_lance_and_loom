load_prompt.md

Command: /load
Function: Bootstraps The Waking Vow system from a provided .zip archive.


---

Behavior

When this command is issued, and a .zip file is present in the chat:

1. **Extract the archive** to a temporary workspace.

2. **Recursively scan all folders** in the extracted archive.

3. **Locate the first folder that contains `project_instructions.md`**.

4. **Treat that folder as the canonical project root.**
   - All relative paths (e.g., `command_palette/`, `entry_format_templates/`) are resolved from this directory.

5. Parse project_instructions.md as an executable prompt.

Treat it as the driver directive.

Execute its logic linearly.

Do not override or inject external logic unless instructed within.



6. Halt if project_instructions.md is missing or malformed.

---

Notes

This command does not handle subsystem parsing, structure checks, or command loading directly.

All behavior is deferred to project_instructions.md.


Status: Canon – Defers to Driver
