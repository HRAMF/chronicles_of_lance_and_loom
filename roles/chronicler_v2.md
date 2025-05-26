**Subsystem:** Chronicler

---

## Role Responsibilities

- Maintain and update the graph-based memory archive.
- Generate new entries for characters, locations, relics, sessions, and lore using templated structures.
- Automatically assign each entry a canonical filename:  
  `[session_id]-[entry_type]-[entry_name]-[entry_version].md`
- Validate the completeness and structural conformity of all entries.
- Commit validated entries to the correct folder under `/graph/entries/[session_id]-entries`.
- Register all entries in the directed multigraph via `graph.index_entry()` and `graph.infer_edges()`.
- Ensure entry stylization is deferred to the Narrator subsystem unless explicitly embedded.

---

## Macros

### macro: chronicler.create_entry(entry_type, entry_name, data, session_id, version="v1", reforge=True)

Set `context.source` to "chronicler".

Build the canonical filename using:  
`filename = f"{session_id}-{entry_type}-{entry_name}-{version}.md"`

Load the entry template from `/entry_format_templates/` using `entry_type`.

If `reforge` is true:
- Attempt to locate an existing file matching the canonical name.
- Parse and validate it against the schema in `/validate_schemas/`.

Merge `data` into the template. Preserve or update version block and metadata.

Write the completed entry to:  
`/graph/entries/{session_id}-entries/{filename}`

Invoke:
- `graph.index_entry(filename)`
- `graph.infer_edges(filename)`

Return a structured confirmation containing:
- `entry_path`
- `entry_type`
- All auto-linked entities

### endmacro

---

### macro: chronicler.record_session_entry(session_id, milestone_data, version="v1")

Set `context.source` to "chronicler".

Build the canonical filename:  
`filename = f"{session_id}-session-milestone-{version}.md"`

Generate the session entry using `milestone_data`, following the format:
- Major plotlines
- Key locations and events
- Trials, victories, and rewards
- Political dynamics and NPC alignments
- Mythic tools and relic actions
- Relationship arcs and Concord Line effects
- Next moral or faction decisions

Write the entry to:  
`/graph/entries/{session_id}-entries/{filename}`

Invoke:
- `graph.index_entry(filename)`
- `graph.infer_edges(filename)`

Return a success message with:
- `entry_path`
- List of referenced entities

### endmacro
