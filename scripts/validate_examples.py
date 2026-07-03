import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "name": "Settlement Review Record",
        "schema": ROOT / "schemas" / "settlement-review-record.schema.json",
        "example": ROOT / "examples" / "settlement-review-record.example.yaml",
    },
    {
        "name": "Human Settlement Gate",
        "schema": ROOT / "schemas" / "human-settlement-gate.schema.json",
        "example": ROOT / "examples" / "human-settlement-gate.example.yaml",
    },
    {
        "name": "Marketplace Rule Review",
        "schema": ROOT / "schemas" / "marketplace-rule-review.schema.json",
        "example": ROOT / "examples" / "marketplace-rule-review.example.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    failed = False

    for target in VALIDATION_TARGETS:
        print(f"[validate] {target['name']}")
        print(f"  schema : {target['schema'].relative_to(ROOT)}")
        print(f"  example: {target['example'].relative_to(ROOT)}")

        schema = load_json(target["schema"])
        example = load_yaml(target["example"])

        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

        if errors:
            failed = True
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"Error: {location}: {error.message}")
        else:
            print(f"[ok] {target['name']} example is valid")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
