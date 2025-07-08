import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import spacy

load_dotenv()

# === Paths from .env or defaults ===
INPUT_DIR = Path(os.getenv("INPUT_DIR", "/data/input"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "/data/output"))

# === Language model mapping ===
SPACY_MODELS = {
    "en": "en_core_web_sm",
    "fr": "fr_core_news_sm",
    "es": "es_core_news_sm",
    "ru": "ru_core_news_sm",
    "zh": "zh_core_web_sm",
    "xx": "xx_ent_wiki_sm",
}


# === Language detection by filename (stub) ===
def detect_language(filename: str) -> str:
    fname = filename.lower()
    for lang in SPACY_MODELS:
        if lang in fname:
            return lang
    return "en"


# === Chunk text into smaller parts ===
def chunk_text(text, max_len=500_000):
    for i in range(0, len(text), max_len):
        yield i, text[i : i + max_len]


# === Load spaCy model with increased max_length ===
def load_spacy_model(model_name: str):
    nlp = spacy.load(model_name)
    nlp.max_length = 6_000_000  # just in case
    return nlp


# === Tag entities from text chunks ===
def tag_entities(text, lang):
    entities = []

    print(f"[INFO] Text length: {len(text):,} characters")

    # 1. Load primary model
    base_model = SPACY_MODELS.get(lang, "xx_ent_wiki_sm")
    base_nlp = load_spacy_model(base_model)

    for offset, chunk in chunk_text(text):
        doc = base_nlp(chunk)
        for ent in doc.ents:
            entities.append(
                {
                    "start": ent.start_char + offset,
                    "end": ent.end_char + offset,
                    "label": ent.label_,
                    "text": ent.text,
                }
            )

    # 2. English-only: run en_ner_eco_biobert in chunks
    if lang == "en":
        try:
            eco_nlp = spacy.load("en_ner_eco_biobert")
            eco_nlp.max_length = 6_000_000
            for offset, chunk in chunk_text(text):
                doc = eco_nlp(chunk)
                for ent in doc.ents:
                    entities.append(
                        {
                            "start": ent.start_char + offset,
                            "end": ent.end_char + offset,
                            "label": ent.label_,
                            "text": ent.text,
                        }
                    )
        except Exception as e:
            print(f"[WARN] Failed to load en_ner_eco_biobert: {e}")

    return entities


# === Main runner ===
def main(txt_file):
    input_path = INPUT_DIR / txt_file
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    try:
        text = input_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(f"[ERROR] Could not decode {txt_file}: {e}")
        sys.exit(1)

    lang = detect_language(txt_file)
    print(f"[INFO] Detected language: {lang}")

    entities = tag_entities(text, lang)

    output_data = {
        "filename": txt_file,
        "language": lang,
        "text": text,
        "entities": entities,
    }

    output_path = OUTPUT_DIR / f"{input_path.stem}.entities.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"[✓] Saved tagged entities to: {output_path}")


# === CLI entry point ===
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ner_pipeline.py <filename.txt>")
        sys.exit(1)

    main(sys.argv[1])
