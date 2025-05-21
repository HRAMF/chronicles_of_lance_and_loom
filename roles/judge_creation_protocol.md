judge_creation_protocol.md

Subsystem: Judge
Purpose: Define consistent rules and sources for generating .yml statblocks and item sheets that align with narrative, mechanical, and symbolic truths of The Waking Vow.


---

Character Sheet Construction Protocol

Objective

Ensure all PC and NPC .yml statblocks:

Reflect campaign-specific background and feat progression

Align with mechanical foundations (D&D 5e 2024)

Include reaction-prompting, passive traits, and multi-class logic


Source Hierarchy

1. -pc or -npc entries (role, background, emotional and narrative traits)


2. Character sheet PDFs (stats, class progression, feats)


3. Session summaries (-session) for custom rulings, reactions used, and combat behavior


4. bio memory and retcon logs for feat rationale or house rules



Steps

1. Parse Metadata: name, class, level, alignment, race


2. Build Ability Scores: use feat bonuses and character origin modifiers as defined by 5e 2024 (Background + Heritage)


3. Crosscheck Feats: Alert, Resilient, Great Weapon Master, etc.


4. Validate Subclass Features: Channel Divinity, Aura traits, Sorcery Points


5. Apply Spellcasting Framework: spell slots, known spells, prepared spells


6. Import Reactions and Passive Traits: Divine Smite, Shield, Aura of Protection


7. Structure YAML Output: include notes, tracking blocks, spellcasting metadata


8. Flag Gaps: mark incomplete or unvalidated sections clearly




---

Item Sheet Construction Protocol

Objective

Ensure .yml relics and magic items:

Reflect narrative origin (forged in myth, gifted by gods, etc.)

Align with weapon type and 5e 2024 mechanics

Preserve symbolic truth and campaign evolution


Source Hierarchy

1. -item or -relic entries


2. -lore describing crafting, mythic bond, or evolution


3. Session logs (uses of item powers, smite behavior, synergy events)


4. Public weapons database (for mastery tags and base weapon types)



Steps

1. Set Metadata: name, type, rarity, base weapon


2. Define Weapon Mastery: use appropriate tag (e.g., topple for lance)


3. Import Bonuses: attack/damage bonus, radiant bonuses, AC buffs


4. Define Features:

type: passive, reaction, special_action, or ritual_synergy

Include trigger logic and clear effect phrasing



5. Set Charges: max/recharge rules


6. Cross-reference Symbolism:

Ensure features like Wrath of Dawn or Blooming Vow match mythic texts



7. Mark Attunement: specific wielder or class restrictions


8. Flag Gaps: if a relic lacks its lore-granted power, highlight



Collaborative Creation Command

For mythic or hybrid relics that combine symbolic and mechanical sources:

The Judge must initiate /judge create_item_collab to complete the entry with player or DM oversight.

This command initiates a structured co-creation sequence:

1. Prompt for base weapon and magical inspiration (e.g., Sun Blade)


2. Request narrative origin and symbolic themes


3. Draft .yml structure


4. Revise collaboratively and finalize




This ensures narrative fidelity, correct tagging, and player-approved mythic convergence.


---

Validation Flags

All generated .yml files must be checked against:

validate_statblocks.py or validate_items.py

Canonical ability presence per source file

Narrative incompleteness (e.g., missing synergy triggers)



---

Rule Precedence

To maintain mechanical accuracy and minimize rule drift, the Judge follows this rule hierarchy:

1. Campaign Overrides and House Rules: Written into bio, item .md, or session entries


2. 5e 2024 OGC Rules: Core class, spell, weapon, and item mechanics


3. Protocol Defaults: Used only when no explicit rule or override exists



Protocols must never override OGC mechanics. They define structure, not values.


---

Linked Systems

project_instructions.md

chronicler.md

narrator.md

judge.md

validate_statblocks.py

validate_items.py



---

Note: This protocol governs Judge-generated mechanical entries and their alignment with the spiritual, emotional, and symbolic truths curated by the Chronicler and Narrator.
