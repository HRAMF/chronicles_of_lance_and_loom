**Command:** /chronicler reforge_all session=[XX] stylize=[true|false]  
**Subsystem:** Chronicler

---

## Execution Behavior

When this command is invoked, you must:

1. Parse `session` and `stylize` parameters
2. Set `context.source = chronicler`
3. Construct path:
       path = f"graph/entries/{session}-entries"
4. For each `.md` file in `path`:
   - Determine `entry_type` from filename
   - Load file contents as `data`
   - Execute:
         chronicler.create_entry(entry_type, data, reforge=True)
     - Stylization applies only if `stylize=true`
   - Write updated file back to `path`
   - Execute:
         graph.index_entry(entry)
         graph.infer_edges(entry)

5. Output bundled reforged entries, graph_node_registry.csv and graph_edge_registry.csv as a downloadable .zip file

---

**Status:** Canon - Executable Prompt (v1.4.1)
