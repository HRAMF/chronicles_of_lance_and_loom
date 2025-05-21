# auto_prompt_reactions.md
**Subsystem:** Judge  
**Function:** Global Feature Toggle – Reaction Prompting  

---

## Description

This file governs whether the Judge subsystem should automatically prompt players when a valid reaction, passive ability, or triggered feature becomes available during combat or narrative sequences.

---

## Behavior

- If enabled:  
  The Judge will actively scan statblocks and prompt players at key decision points (e.g., being hit, seeing a spell cast) to suggest using reactions such as:
  - **Shield**
  - **Divine Smite**
  - **Counterspell**
  - **Hellish Rebuke**
  - **Absorb Elements**

- If disabled:  
  The Judge will remain silent unless specifically queried via `/judge interpret="..."`.

---

## Configuration

```yaml
auto_prompt_reactions: true
