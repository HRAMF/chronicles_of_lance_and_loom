macro_protocol.md

Title: Macro Execution Model for Waking Vow Framework (v1.5)
Type: Canonical Runtime Directive
Scope: Subsystem and Command Execution via Registered Hooks


---

Purpose

This document defines the structure, naming, and registration model for all executable macros in the Waking Vow framework v1.5.

Macros are the atomic execution units of the framework. They may appear in:

Subsystem role files (internal logic)

Command files (user-facing logic)



---

Canonical Declaration Format

Each macro must begin with:

### macro: [subsystem.function(param_1, param_2=default, ...)]

This must be followed immediately by:

A prompt logic block written in imperative language

No metadata, footers, or behavioral prose


Example:

### macro: chronicler.create_entry(entry_type, data, reforge=True)

Set context.source to "chronicler" if not already set.  
Load the entry template from entry_format_templates/.  
If reforge is true, parse existing entry and validate against the schema.  
Merge new content into templated structure.  
Write the updated file to graph/entries/[session]/.  
Call graph.index_entry(entry) and graph.infer_edges(entry).  
Return a success confirmation.


---

Macro Registration

Macros are registered at runtime during /load via project_instructions.md.

The engine will:

1. Recursively scan all .md files in /roles/ and /command_palette/


2. Match lines beginning with ### macro:


3. Bind the hook string (e.g., chronicler.create_entry(...)) to the logic block that follows


4. Store all bindings as runtime-callable prompt functions




---

Invocation Behavior

All commands and pipelines must call macros using their exact hook:

chronicler.create_entry(...)
judge.audit(...)
narrator.stylize_section(...)

No inference is allowed

Hook must match declaration exactly

Arguments may be expanded by the runtime during execution



---

Enforcement Rules

Only one ### macro: declaration is allowed per macro block

All macros must live in .md files within /roles/ or /command_palette/

Prompt logic must be self-contained

All macros must be declared before they are referenced



---

Status: Canon – All macro-based execution in Waking Vow v1.5 must follow this protocol.


