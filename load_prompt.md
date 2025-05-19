load_prompt.md

Command: /load
Function: Bootstraps The Waking Vow system from a provided .zip archive.


---

Behavior

When this command is issued, and a .zip file is present in the chat:

1. Extract the archive and locate the root project folder (typically the_waking_vow/).


2. Locate project_instructions.md in the root.


3. Parse project_instructions.md as an executable prompt.

Treat it as the driver directive.

Execute its logic linearly.

Do not override or inject external logic unless instructed within.



4. Halt if project_instructions.md is missing or malformed.




---

Notes

This command no longer handles subsystem parsing, structure checks, or command loading directly.

All behavior is deferred to project_instructions.md.


Status: Canon – Defers to Driver

