Subsystem: Graph Protocol
Function: Entry indexing, graph memory inference, and directed multigraph behavior
Role Type: Auxiliary / Structural


---

Purpose

This file defines macros and structural expectations for managing the narrative graph memory of The Waking Vow.
Graph operations are invoked by the Chronicler but must remain modular and separately declared.

All graph logic is applied inside the /graph/ directory.


---

Canonical Macros

graph.index_entry(entry)

You must:

1. Extract the entry ID from the filename


2. Generate a new row in graph_node_registry.csv with:

entry_id

entry_type

title

version

file_path



3. If an entry with the same ID and version exists, overwrite its row


4. Do not index entries without a valid ID or missing required fields




---

graph.infer_edges(entry)

You must:

1. Parse the full text of the entry


2. Identify relationships to other entries by matching:

Connected Files

Internal references

Version lineage



3. For each relationship, write a row to graph_edge_registry.csv with:

from = this entry’s ID

to = referenced entry’s ID

relation = references, linked_to, supports, introduced_in, or derives_from

weight = 1.0 unless otherwise inferred



4. Overwrite any duplicate edge with the same from → to and relation




---

Edge Semantics

references: Explicit mention or citation

linked_to: Symmetrical relation (e.g., location ↔ event)

supports: Enables growth of another entry’s theme

introduced_in: Entry was discovered or created during the target session

derives_from: Entry is a revision of a prior version



---

Invocation

Only the Chronicler may call these macros. You must:

Always call graph.index_entry(entry) after writing or rewriting a .md file

Always call graph.infer_edges(entry) if stylization or structural parsing is complete

Never execute graph logic during stylization



---

Status: Canon – Auxiliary Graph Management Active (v1.4.1)
