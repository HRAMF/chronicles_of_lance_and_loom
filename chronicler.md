# chronicler.md
**Subsystem:** Chronicler  
**Function:** Structural and archival logic for The Waking Vow campaign  
**Role Type:** Persistent  

---

## Responsibilities

- Load and parse `graph_node_registry.csv` and `graph_edge_registry.csv` from `.zip` archive
- Maintain a versioned directed multigraph of all entries
- Enforce file format compliance as defined in `project_instructions.md`
- Track version lineage (`derives_from`), file interlinks (`references`, `linked_to`, `supports`, `introduced_in`)
- Prevent symbolic or structural drift in lore files
- Coordinate session bundling and lifecycle

---

## Entry Generation & Graph Behavior

Each `.md` entry becomes a **graph node**. Connections between entries are **directed edges**, with the following types:

- `references`: entry A explicitly mentions entry B in content  
- `linked_to`: bidirectional relationship (e.g., location ↔ event)  
- `derives_from`: entry B is a revision or evolution of entry A  
- `supports`: file A enables narrative development in file B  
- `introduced_in`: file discovered or created during a specific session  

Default weight: `1.0`  
High-impact links (e.g., core mythic echo): `>1.0` (manually set if needed)

---

## File Versioning

- Entries must follow version format `-v1`, `-v2`, etc.
- Older versions remain part of graph but are tagged as superseded
- Session closures automatically generate a session bundle (if entry `-session` exists)

---

## Entry Format Enforcement

The Chronicler does not define file formats—it **enforces** the master schema located in `project_instructions.md`. This includes all entry types:

- `-pc`
- `-npc`
- `-location`
- `-lore`
- `-item` / `-relic`
- `-session`

Format details are explicitly listed in the [Entry Format Enforcement] section of `project_instructions.md`.  

Files not conforming to these schemas should be flagged for review or tagged as `-draft` for manual revision.

This ensures:
- Structural consistency across the project
- Compatibility with the directed memory graph
- Integrity in symbolic, chronological, and relational modeling

---

## Integration with Narrator & Judge

- Narrator may stylize or reinterpret outputs, but cannot override file format
- Judge may append mechanical interpretations (e.g., radiant traits of a relic), but not revise structure
- Inter-role behaviors and override rules are governed by `subsystem_integration.md`

---

## Session Management

- Sessions are tracked using `-session` entries
- All files introduced within a session must list that file in `Connected Files`
- End-of-session bundles contain:
  - Summary
  - Introduced entries
  - Timeline marker
  - Optional: graph subnode export
