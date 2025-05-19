# validate_statblocks.py
import os
import yaml

def validate_statblock(file_path):
    required_keys = ["name", "hp", "ac", "abilities", "features", "reactions"]
    issues = []

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            return ["YAML parsing error"]

    for key in required_keys:
        if key not in data:
            issues.append(f"Missing required key: {key}")

    # Ability check
    if "abilities" in data:
        required_abilities = ["str", "dex", "con", "int", "wis", "cha"]
        if not all(attr in data["abilities"] for attr in required_abilities):
            issues.append("Incomplete abilities block")

    # Spell slot validation if features use them
    if "features" in data:
        for feature, details in data["features"].items():
            if isinstance(details, dict):
                if details.get("uses_spell_slots", False) and "slots" not in data:
                    issues.append(f"Feature '{feature}' uses spell slots but 'slots' block is missing")
                if details.get("uses_pool", False) and "pool_max" not in details:
                    issues.append(f"Feature '{feature}' uses pool but 'pool_max' is missing")

    return issues

def run_validation_on_folder(folder_path):
    results = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.yaml') or file.endswith('.yml'):
                file_path = os.path.join(root, file)
                issues = validate_statblock(file_path)
                results[file] = issues if issues else ["Valid"]
    return results

# Example usage:
# results = run_validation_on_folder("path/to/statblocks")
# for file, outcome in results.items():
#     print(f"{file}: {', '.join(outcome)}")
