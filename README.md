**Project:** The Concord Line  
**Version:** 1.1  
**Purpose:** Narrative-Mechanical Framework for High-Fidelity Campaign Execution

---

## Overview

*The Concord Line* is a modular, role-aware framework for running, expanding, and mythologizing D&D 5e (2024 rules) campaigns. It leverages a subsystem model ”**Chronicler**, **Narrator**, and **Judge**”to preserve structure, enforce mechanics, and stylize tone in a directed memory graph.

Campaigns are executed via ChatGPT using a `.zip` archive containing this project directory.

---

## Subsystem Execution

Upon running `/load` with this structure:
- All subsystems are activated using `project_instructions.md`
- Each command in `command_palette/` is registered
- Format validation is enforced using templates
- Entries can be scanned, reforged, stylized, or interpreted via role-specific commands

---

## Entry Naming and Versioning

- Files must be named using `session-prefix + entry-type + unique-name + -vN.md`
- Example: `00-lore-battle_at_mithral_gate-v1.md`
- Versioning is tracked using the `derives_from` relationship in the directed graph

---

**Status:** Ready for Use with `/load`  
**Minimum Required Files:**  
- `project_instructions.md`  
- `chronicler.md`  
- `narrator.md`  
- `command_palette/` with valid command files  
- `entry_format_templates/`
