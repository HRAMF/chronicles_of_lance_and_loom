# chronicler_reforge_all.md
**Command:** /chronicler reforge_all session=[XX] stylize=[true|false]  
**Subsystem:** Chronicler

---

## Purpose

Retroactively format all `.md` entries in a given session folder and ensure they are:
- Brought into compliance with their schema
- Rewritten to `graph/entries/[XX]/`
- Properly registered in the directed graph

This command is intended to resolve legacy or malformed entries by passing them through the canonical creation pipeline.

---

## Execution Flow

When this command is invoked:
1. Set `context.source = chronicler`
2. For each file in `graph/entries/[XX]/`:
   - Parse `entry_type` from filename or metadata
   - Load file content
   - Call:
     ```
     chronicler.create_entry(entry_type, data, reforge=True)
     ```
     - This triggers template enforcement
     - If `stylize = true`, invokes stylization on compliant fields
     - If `stylize = false`, skips stylization step
   - Write updated file back to `graph/entries/[XX]/`
   - Call:
     ```
     graph.index_entry(entry)
     graph.infer_edges(entry)
     ```

---

## Notes

- Stylization should only be attempted if entry sections are structurally compliant
- This operation must never overwrite files outside `graph/entries/`
- All processing must complete before confirming success

---

## Response

```
All entries in session [XX] have been reforged and indexed. Stylization: [enabled|disabled]
```

---

**Status:** Canon – Chronicler Batch Compliance Tool (v1.4.1)
