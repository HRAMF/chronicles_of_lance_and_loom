**Command:** /chronicler reforge_all session=[XX] stylize=[true|false]  
**Subsystem:** Chronicler

---

## Purpose

This command revalidates and reformats structurally noncompliant entries located exclusively in `graph/entries/[XX-entries]/`, bringing them into compliance with enforced templates and registering them into the memory graph.

---

## Execution Flow

When this command is invoked:

1. Parse `session` and `stylize` parameters
2. Set `context.source = chronicler`
3. Construct path:
       path = f"graph/entries/{session}-entries"
4. For each `.md` file in `path`:
   - Determine `entry_type` from filename
   - Load file contents
   - Call:
         chronicler.create_entry(entry_type, data, reforge=True)
     - Stylization applies only if `stylize=true`
   - Write updated file back to `path`
   - Call:
         graph.index_entry(entry)
         graph.infer_edges(entry)

---

## Notes

- You must never read from or write to any directory outside `graph/entries/[XX-entries]/`
- Stylization is disabled by default unless explicitly passed
- Graph indexing must occur after structural compliance

---

## Response

    All entries in session [XX] have been reforged and indexed.
    Stylization: [enabled|disabled]

---

**Status:** Canon - Executable Prompt (v1.4.1)
