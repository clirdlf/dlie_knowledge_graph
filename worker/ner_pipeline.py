import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import spacy

load_dotenv()

# --- Paths from .env or defaults ---
INPUT_DIR = Path(os.getenv("INPUT_DIR", "/data/input"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "/data/output"))

# --- Map language codes to spaCy small models ---
SPACY_MODELS = {
    "en": "en_core_web_sm",
    "fr": "fr_core_news_sm",
    "es": "es_core_news_sm",
    "ru": "ru_core_news_sm",
    "zh": "zh_core_web_sm",
    "xx": "xx_ent_wiki_sm",  # fallback
}


# --- Simple language guesser by filename ---
def detect_language(filename: str) -> str:
    fname = filename.lower()
    for lang in SPACY_MODELS:
        if lang in fname:
            return lang
    return "en"  # default


# --- Load appropriate spaCy model ---
def load_spacy_model(lang: str) -> spacy.language.Language:
    model_name = SPACY_MODELS.get(lang, "xx_ent_wiki_sm")
    try:
        return spacy.load(model_name)
    except OSError:
        print(
            f"[WARN] Could not load spaCy model '{model_name}', falling back to multilingual."
        )
        return spacy.load("xx_ent_wiki_sm")


# --- Extract entities using spaCy + eco_biobert if English ---
def tag_entities(text: str, lang: str) -> list:
    entities = []

    # 1. Base spaCy model
    base_nlp = load_spacy_model(lang)
    base_doc = base_nlp(text)
    for ent in base_doc.ents:
        entities.append(
            {
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_,
                "text": ent.text,
            }
        )

    # 2. en_ner_eco_biobert for English
    if lang == "en":
        try:
            eco_nlp = spacy.load("en_ner_eco_biobert")
            eco_doc = eco_nlp(text)
            for ent in eco_doc.ents:
                entities.append(
                    {
                        "start": ent.start_char,
                        "end": ent.end_char,
                        "label": ent.label_,
                        "text": ent.text,
                    }
                )
        except Exception as e:
            print(f"[WARN] Failed to load en_ner_eco_biobert: {e}")

    return entities


# --- Main process ---
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


# --- Entry point ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ner_pipeline.py <input.txt>")
        sys.exit(1)

    main(sys.argv[1])
