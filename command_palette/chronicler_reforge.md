chronicler_reforge.md

Command: /chronicler reforge entry=[filename] Subsystem: Chronicler Version: 1.0


---

Purpose

Rebuilds a single markdown entry using its correct structural template, validates canon compliance, and invokes the Narrator for stylization.


---

Behavior

When this command is issued:

1. Assume the Chronicler role.


2. Locate the file [filename] in the session archive.


3. Infer the entry type from the file name prefix (e.g., -lore, -npc, etc.).


4. Load the corresponding template from entry_format_templates/.


5. Run validate_entry_format.py to identify missing or misformatted sections.


6. For each required section:

If missing, insert header and placeholder

If content is inferred from unstructured body, place it under appropriate section



7. Reconstruct the full entry in markdown using enforced headers.


8. Invoke the Narrator to stylize applicable sections:

-lore: Origin, Expression in the World, Outcome and Legacy

-npc: Role, Key Moments, Narrative Significance



9. Return the formatted, stylized .md file.




---

Validation

Abort if file is not found.

Abort if the entry type is unrecognized.

Log if entry was already compliant and skipped.



---

Output

A markdown file with:

Canonical section headers

Stylized narrative content

Structure-compliant formatting


Filename versioned as -v2 unless otherwise specified.



---

Integration

This command must be registered and executed during /load by parsing the command_palette/ directory. Subsystem behavior must defer to chronicler.md, narrator.md, and subsystem_integration.md during execution.

Status: Canon – Activated at Load

