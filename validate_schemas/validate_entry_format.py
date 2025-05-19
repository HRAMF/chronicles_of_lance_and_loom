# validate_entry_format.py

import os
import re

# Define required section headers for each entry type
entry_templates = {
    "-pc": ["Name", "Race", "Class", "Title", "Origins", "Primary Calling", "Affiliations",
            "Identity and Formation", "Internal Compass", "Relationships and Imprint",
            "Emotional Landscape", "Aspirations", "Connected Files"],
    "-npc": ["Name", "Race", "Class", "Affiliation", "Role in Narrative",
             "Personality and Voice", "Key Moments with PC", "Narrative Significance", "Connected Files"],
    "-location": ["Name", "Region", "Affiliation", "Description",
                  "Historical Role", "Events or Encounters", "Spiritual / Strategic Significance", "Connected Files"],
    "-lore": ["Name", "Theme", "Timeframe", "Origin", "Expression in the World",
             "Outcome and Legacy", "Connected Files"],
    "-item": ["Name", "Item Type", "Origin", "Properties and Powers",
              "Bearer History", "Narrative Significance", "Connected Files"],
    "-session": ["Title", "Opening Tag", "Narrative Summary",
                 "Closing Statement or Teaser", "Connected Files"]
}

def validate_entry_format(file_path):
    issues = []
    file_type = None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        for entry_type, required_headers in entry_templates.items():
            if entry_type in os.path.basename(file_path):
                file_type = entry_type
                for header in required_headers:
                    if re.search(rf"^##\\s+{re.escape(header)}", content, re.MULTILINE) is None:
                        issues.append(f"Missing section: {header}")
                break

        if file_type is None:
            issues.append("Unknown entry type: unable to match naming convention (-pc, -npc, etc.)")

    except Exception as e:
        issues.append(f"File error: {e}")

    return issues

def run_format_validation(folder_path):
    results = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                result = validate_entry_format(full_path)
                if result:
                    results[file] = result
    return results
