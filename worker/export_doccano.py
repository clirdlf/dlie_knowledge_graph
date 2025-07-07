import sys
import json
from pathlib import Path
import jsonlines

INPUT_DIR = Path("/data/output")
EXPORT_DIR = Path("/data/doccano")
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

def export_to_doccano(filename):
    input_path = INPUT_DIR / filename
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    doccano_data = {
        "text": data["text"],
        "labels": [[ent["start"], ent["end"], ent["label"]] for ent in data["entities"]]
    }

    export_path = EXPORT_DIR / f"{input_path.stem}.jsonl"
    with jsonlines.open(export_path, mode='w') as writer:
        writer.write(doccano_data)

    print(f"[✓] Doccano JSONL exported to: {export_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_doccano.py report.entities.json")
        sys.exit(1)

    filename = sys.argv[1]
    export_to_doccano(filename)