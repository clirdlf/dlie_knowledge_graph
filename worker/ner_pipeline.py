import sys
import os
import json
from pathlib import Path
from dotenv import load_dotenv
import spacy

# Optional: TaxoNERD if language is English
try:
    from taxonerd import TaxoNERD

    TAXONERD_AVAILABLE = True
except ImportError:
    TAXONERD_AVAILABLE = False

load_dotenv()

# Paths
INPUT_DIR = Path(os.getenv("INPUT_DIR", "/data/input"))
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "/data/output"))

# Language-to-model map
SPACY_MODELS = {
    "en": "en_core_web_sm",
    "fr": "fr_core_news_sm",
    "es": "es_core_news_sm",
    "ru": "ru_core_news_sm",
    "zh": "zh_core_web_sm",
    "xx": "xx_ent_wiki_sm",  # fallback
}


# --- Language detection stub (replace with langdetect if needed) ---
def detect_language(filename):
    # Placeholder: you can implement a proper detector if needed
    if "fr" in filename:
        return "fr"
    elif "es" in filename:
        return "es"
    elif "ru" in filename:
        return "ru"
    elif "zh" in filename:
        return "zh"
    elif "ar" in filename:
        return "xx"
    else:
        return "en"


# --- Load spaCy model based on language ---
def load_spacy_model(lang):
    model = SPACY_MODELS.get(lang, "xx_ent_wiki_sm")
    try:
        return spacy.load(model)
    except OSError:
        print(f"[ERROR] spaCy model '{model}' not found. Ensure it's installed.")
        sys.exit(1)


# --- Run spaCy and (optional) TaxoNERD ---
def tag_entities(text, lang):
    entities = []

    # spaCy
    nlp = load_spacy_model(lang)
    doc = nlp(text)
    for ent in doc.ents:
        entities.append(
            {
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_,
                "text": ent.text,
            }
        )

    # TaxoNERD (English only)
    if lang == "en" and TAXONERD_AVAILABLE:
        try:
            taxo = TaxoNERD(model="en_ner_eco_biobert")
            taxo_doc = taxo.predict(text)
            for ent in taxo_doc["entities"]:
                entities.append(ent)
        except Exception as e:
            print(f"[WARN] TaxoNERD failed: {e}")

    return entities


# --- Main ---
def main(txt_file):
    input_path = INPUT_DIR / txt_file
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    text = input_path.read_text(encoding="utf-8")
    lang = detect_language(txt_file)
    print(f"[INFO] Detected language: {lang}")

    entities = tag_entities(text, lang)

    output = {
        "filename": txt_file,
        "language": lang,
        "text": text,
        "entities": entities,
    }

    output_path = OUTPUT_DIR / f"{input_path.stem}.entities.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"[✓] Entities saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ner_pipeline.py file.txt")
        sys.exit(1)

    main(sys.argv[1])
