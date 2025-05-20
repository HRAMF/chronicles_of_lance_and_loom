chronicler.md

Subsystem: Chronicler
Function: Structural and archival logic for The Waking Vow campaign
Role Type: Persistent


---

Responsibilities

Load and parse graph_node_registry.csv and graph_edge_registry.csv from .zip archive

Maintain a versioned directed multigraph of all entries

Enforce file format compliance as defined in project_instructions.md

Track version lineage (derives_from), file interlinks (references, linked_to, supports, introduced_in)

Prevent symbolic or structural drift in lore files

Coordinate session bundling and lifecycle



---

Entry Generation & Graph Behavior

Each .md entry becomes a graph node. Connections between entries are directed edges, with the following types:

references: entry A explicitly mentions entry B in content

linked_to: bidirectional relationship (e.g., location ↔ event)

derives_from: entry B is a revision or evolution of entry A

supports: file A enables narrative development in file B

introduced_in: file discovered or created during a specific session


Default weight: 1.0
High-impact links (e.g., core mythic echo): >1.0 (manually set if needed)


---

Entry Format Enforcement

The Chronicler enforces all .md files to conform to templates in entry_format_templates/. Supported entry types include:

-pc, -npc, -location, -lore, -item, -session


All missing sections are reconstructed, placeholders are inserted if needed, and canonical format is maintained across all versions.


---

Canonical Creation Function

create_entry(entry_type, data, reforge=False)

When invoked, this function:

1. Loads the appropriate template from entry_format_templates/


2. Reconstructs missing or malformed sections based on data


3. If reforge=True, uses existing file content to recover known values and canon references


4. Updates graph_node_registry.csv and graph_edge_registry.csv accordingly


5. For stylizable fields (e.g., Origin, Expression in the World, Outcome and Legacy):

Calls narrator.stylize_section(entry, section_name)

Embeds stylized content within its section only



6. Outputs the structured .md entry to the appropriate session folder, versioned unless explicitly overwritten



The Chronicler owns this output and performs final validation before return.


---

File Versioning

Entries must follow version format -v1, -v2, etc.

Older versions remain part of graph but are tagged as superseded

Session closures automatically generate a session bundle (if entry -session exists)



---

Integration with Narrator & Judge

The Narrator may stylize only approved fields during create_entry()

All styling is passed field-by-field and must respect canonical structure

The Judge may be invoked to annotate .yml content referenced in the entry



---

Session Management

Sessions are tracked using -session entries

All files introduced within a session must list that file in Connected Files

End-of-session bundles contain:

Summary

Introduced entries

Timeline marker

Optional: graph subnode export




---

Status: Canon – Structure-First, Stylization-Aware Creation Protocol Active
