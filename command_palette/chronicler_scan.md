chronicler_scan.md

Command: /chronicler scan session=[XX] Subsystem: Chronicler Version: 1.0


---

Purpose

Scans all markdown entries from session XX to determine if they comply with enforced structure as defined in entry_format_templates/. Returns a list of entries that require reforging.


---

Behavior

When this command is issued:

1. Assume the Chronicler role.


2. Identify all files in the session XX (e.g., 00-, 01-) directory.


3. For each file:

Infer the entry type from the filename prefix (e.g., -lore, -npc, etc.)

Load the correct template from entry_format_templates/

Run validate_entry_format.py to compare structure



4. Compile a list of entries with:

Missing or misordered headers

Absent required sections

Improper filename-to-type mapping



5. Return a report listing all non-compliant entries with reasons per file.




---

Validation

Directory must exist and contain at least one .md file

Ignore non-markdown files and non-matching session prefixes



---

Output

Markdown list of filenames with structural issues

For each file: sections missing or flagged by validate_entry_format.py



---

Integration

This command is part of the Chronicler role’s toolset and must be available upon /load if command_palette/ is present. Used to support chronicler_reforge by providing a non-destructive analysis stage.

Status: Canon – Activated at Load

