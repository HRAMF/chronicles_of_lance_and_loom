# command_palette/load.md

## Command
/load

## Bound Subsystem
bootloader

## Behavior
When this command is issued, and a .zip file is present in the chat:

1. **Extract the archive** to a temporary workspace at `/mnt/data/extracted_project`.

2. **Recursively search** the extracted directory tree for folders containing a file named `project_instructions.md`.

3. **Select the shallowest valid folder** (i.e., the one with the fewest path segments) as the canonical project root.
   - If multiple candidates share the same shallow depth, raise an ambiguity error.
   - If none are found, halt and return: `project_instructions.md missing or malformed`.

4. **Set the canonical root** and store it in persistent memory under `project_root`.

5. **Defer all control to** the `project_instructions.md` found in that folder.
   - Parse and execute it exactly as if the user had manually configured from that location.

6. Upon success, respond:
```
The Waking Vow system has been initialized. Chronicler, Narrator, and Judge are now active.
```
## Status
Version 1.4.1 – Canonical root detection fixed. Now compatible with deeply nested archives.
