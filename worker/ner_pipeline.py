import sys
import json
from pathlib import Path
import spacy

try:
    from taxonerd import TaxoNERD
    USE_TAXONERD = True
except ImportError:
    USE_TAXONERD = False
    print("[WARN] TaxoNERD not installed. Skipping ecological tagging.")

# Config
INPUT_DIR = Path("/data/output")
OUTPUT_DIR = Path("/data/output")
SPACY_MODEL = "en_core_web_lg"  # or "xx_ent_wiki_sm" for multilingual
TAXONERD_MODEL = "en_ner_eco_biobert"

def load_spacy_model(model_name):
    print(f"[INFO] Loading spaCy model: {model_name}")
    return spacy.load(model_name)

def extract_entities_spacy(nlp, text):
    doc = nlp(text)
    return [
        {
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_,
            "text": ent.text
        } for ent in doc.ents
    ]

def extract_entities_taxonerd(text):
    if not USE_TAXONERD:
        return []
    taxonerd = TaxoNERD(model=TAXONERD_MODEL)
    entities = taxonerd.find_entities(text)
    return [
        {
            "start": ent.start_char,
            "end": ent.end_char,
            "label": ent.label_,
            "text": ent.text
        } for ent in entities.ents
    ]

def process_file(filename):
    input_path = INPUT_DIR / filename
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        return

    text = input_path.read_text(encoding='utf-8')
    nlp = load_spacy_model(SPACY_MODEL)

    print(f"[INFO] Running spaCy NER on {filename}")
    entities_spacy = extract_entities_spacy(nlp, text)

    print(f"[INFO] Running TaxoNERD (if applicable)")
    entities_taxo = extract_entities_taxonerd(text) if SPACY_MODEL.startswith("en") else []

    all_entities = entities_spacy + entities_taxo

    # Deduplicate by span+label
    seen = set()
    unique_entities = []
    for ent in all_entities:
        key = (ent["start"], ent["end"], ent["label"])
        if key not in seen:
            seen.add(key)
            unique_entities.append(ent)

    output_path = OUTPUT_DIR / f"{input_path.stem}.entities.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"text": text, "entities": unique_entities}, f, indent=2, ensure_ascii=False)

    print(f"[✓] Entity JSON saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ner_pipeline.py report.txt")
        sys.exit(1)

    text_filename = sys.argv[1]
    process_file(text_filename)