**Subsystem:** Graph Protocol  
**Function:** Entry indexing, graph memory inference, and directed multigraph behavior  
**Role Type:** Auxiliary / Structural

---

## Purpose

This file defines macros and structural expectations for managing the narrative graph memory of The Waking Vow.  
Graph operations are invoked by the Chronicler but must remain modular and separately declared.

All graph logic is applied inside the `/graph/` directory.

---

## Canonical Macros

### macro: graph.index_entry(entry_path)

You must:
1. Extract entry metadata from the filename using this canonical format:
   `[session_id]-[entry_type]-[entry_name]-[entry_version].md`

   Extracted fields:
   - entry_id = entry_name
   - entry_type
   - version
   - session_id

2. Extract the title from the entry's frontmatter or first top-level markdown heading.

3. Ensure `graph_node_registry.csv` exists. If it does not, create it with headers:
   - entry_id,entry_type,title,version,file_path

4. Add or replace a row in `graph_node_registry.csv` with:
   - entry_id
   - entry_type
   - title
   - version
   - file_path

5. Each node must be unique by (entry_id, version).

### endmacro

---

### macro: graph.infer_edges(entry_path)

You must:
1. Parse the full text of the entry.

2. Identify relationships to other entries via:
   - Connected Files list
   - Internal references (e.g., filenames, entry IDs)
   - Version lineage (e.g., -v2, -v3 suffixes)

3. For each valid reference, write a row to `graph_edge_registry.csv`:
   - from = entry_id (this file)
   - to = referenced entry_id
   - relation = one of: references, linked_to, supports, introduced_in, derives_from
   - weight = 1.0 unless otherwise inferred

4. If `graph_edge_registry.csv` does not exist, create it with headers:
   - from,to,relation,weight

5. If an edge with the same (from to, relation) already exists, replace it.

6. Do not create edges pointing to invalid or missing entries unless relation = introduced_in.

### endmacro

---

## Edge Semantics

- references: Explicit mention or citation in text
- linked_to: Symmetrical or bi-directional relationship (e.g., place <-> event)
- supports: Thematically enables another entry
- introduced_in: Created or revealed during a session milestone
- derives_from: A later version or rewrite of a prior entry

---

## Invocation

Only the Chronicler may invoke these macros.

You must:
- Call `graph.index_entry(entry_path)` after writing or rewriting any `.md` entry file.
- Call `graph.infer_edges(entry_path)` only after stylization or structural parsing is complete.
- Never invoke graph logic during stylization itself.

---

**Status:** Canon - Auxiliary Graph Management Active (v1.5)
