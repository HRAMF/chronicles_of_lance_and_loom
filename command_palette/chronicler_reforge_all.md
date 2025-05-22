**Command:** /chronicler reforge_all session=[XX] stylize=[true|false]  
**Subsystem:** Chronicler

---

## Purpose

This command is intended to revalidate and reformat structurally noncompliant entries located exclusively in graph/entries/[XX-entries]/, bringing them into alignment with template schema and registering them into the memory graph.

---

## Path Resolution Macro

### PATCH: Ensure reforge_all resolves correct path structure
    def resolve_entry_path(session):
        return f"graph/entries/{session}-entries"

---

## Execution Flow

When this command is invoked:
1. Set `context.source = chronicler`
2. Resolve target directory:
       path = resolve_entry_path(session)
3. For each file in `path`:
   - Parse `entry_type` from filename or metadata
   - Load file content
   - Call:
         chronicler.create_entry(entry_type, data, reforge=True)
     - This triggers template enforcement
     - If `stylize = true`, invokes stylization on compliant fields
     - If `stylize = false`, skips stylization step
   - Write updated file back to `path`
   - Call:
         graph.index_entry(entry)
         graph.infer_edges(entry)

---

## Notes

- Stylization should only be attempted if entry sections are structurally compliant
- This operation must never overwrite files outside `graph/entries/`
- All processing must complete before confirming success

---

## Response

    All entries in session [XX] have been reforged and indexed.
    Stylization: [enabled|disabled]

---

**Status:** Canon - Chronicler Batch Compliance Tool (v1.4.1)
