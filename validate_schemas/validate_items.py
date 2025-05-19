# validate_items.py
import os
import yaml

def validate_item(file_path):
    required_keys = ["name", "type", "mechanics"]
    issues = []

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as exc:
            return ["YAML parsing error"]

    for key in required_keys:
        if key not in data:
            issues.append(f"Missing required key: {key}")

    if "mechanics" in data and not isinstance(data["mechanics"], dict):
        issues.append("Mechanics block must be a dictionary")

    if "features" in data and not isinstance(data["features"], dict):
        issues.append("Features block must be a dictionary (if present)")

    if "charges" in data:
        if not
