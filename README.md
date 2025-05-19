# README.md  
**Project:** The Concord Line  
**Version:** 1.1  
**Purpose:** Narrative-Mechanical Framework for High-Fidelity Campaign Execution

---

## Overview

*The Concord Line* is a modular, role-aware framework for running, expanding, and mythologizing D&D 5e (2024 rules) campaigns. It leverages a subsystem model ”**Chronicler**, **Narrator**, and **Judge**”to preserve structure, enforce mechanics, and stylize tone in a directed memory graph.

Campaigns are executed via ChatGPT using a `.zip` archive containing this project directory.

---

## Project Folder Structure (Required in `.zip`)

```
the_concord_line/                        ← Root folder (any consistent name is accepted)
│
├── project_instructions.md            ← Required. Driver for all behavior
├── chronicler.md                      ← Subsystem behavior
├── narrator.md
├── judge.md
├── judge_creation_protocol.md
├── subsystem_integration.md
│
├── command_palette/                   ← Required. One .md file per command
│   ├── chronicler_reforge.md
│   ├── chronicler_scan.md
│   └── ... (future commands)
│
├── entry_format_templates/            ← Required. One template per entry type
│   ├── template-pc.md
│   ├── template-npc.md
│   ├── template-location.md
│   ├── template-lore.md
│   ├── template-item.md
│   ├── template-session.md
│
├── validate_schemas/                  ← Required. Python scripts for file validation
│   └── validate_entry_format.py
│
├── statblocks/                        ← Optional but recommended. Character .yml files
│   ├── baldric.yml
│   └── ...
│
├── items/                             ← Optional but recommended. Item .yml files
│   ├── dawnshard.yml
│   └── ...
│
├── 00-entries/                        ← Session folders (00-, 01-, etc.)
│   ├── 00-lore-battle_at_mithral_gate-v1.md
│   ├── 00-npc-cyrus_flambard-v1.md
│   └── ...
│
├── 01-entries/
│   └── ...
│
├── graph_node_registry.csv           ← Optional. Populates or updates directed multigraph
├── graph_edge_registry.csv           ← Optional
```

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
