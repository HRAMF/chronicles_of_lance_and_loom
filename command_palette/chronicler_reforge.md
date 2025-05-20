# chronicler_reforge.md
**Command:** `/chronicler reforge entry=[filename]`  
**Subsystem:** Chronicler  
**Version:** 2.0 – Structure-Preserving, Narrator-Aware

---

## Behavior

When this command is invoked:

1. **Assume the Chronicler role**

2. **Locate the entry** `[filename]` from the project root

3. **Infer entry type** from file naming convention (e.g., `-lore`, `-npc`, etc.)

4. **Load matching template** from `entry_format_templates/`

5. **Run validation** using `validate_entry_format.py`:
   - Identify missing or malformed sections
   - Flag unrecognized file structure

6. **Reconstruct file**:
   - Insert required `## [Section]` headers
   - Recover or preserve existing content when aligned
   - Insert placeholders for absent fields
   - Apply memory recovery for canon-aware restoration

7. **Update graph**:
   - Ensure entry is indexed in `graph_node_registry.csv`
   - Register or refresh links in `graph_edge_registry.csv` using `references`, `supports`, etc.

8. **Invoke the Narrator subsystem**:
   - For each stylizable section (`Origin`, `Expression in the World`, `Outcome and Legacy`, etc.):
     - Pass current section text to `Narrator.stylize_section(entry, section_name)`
     - Only style **values**, never headers or container structure
     - Narrator may not invent events unless `rupture=true`

9. **Merge stylized sections** into the reforged file

10. **Save** the entry as `[filename]` (overwrites) or `[filename-v2]` (default behavior unless suppressed)

11. **Return the final `.md` entry** in correct format with stylized content scoped within proper section headers

---

## Output

- A structurally compliant markdown entry
- Stylized fields embedded within proper scaffolding
- File indexed to graph memory

---

## Notes

- Narrator must respect structure
- Graph must be updated before stylization
- Chronicler owns the final `.md` output

---

**Status:** Canon – Enforced Handoff Logic Active
