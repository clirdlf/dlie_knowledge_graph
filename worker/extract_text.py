import os
import sys
import fitz  # PyMuPDF
import requests
import json
from pathlib import Path

GROBID_URL = os.getenv("GROBID_URL", "http://grobid:8070/api/processHeaderDocument")
GROBID_CITATION_URL = os.getenv("GROBID_CITATION_URL", "http://grobid:8070/api/processReferences")

INPUT_DIR = Path("/data/input")
OUTPUT_DIR = Path("/data/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF using PyMuPDF"""
    doc = fitz.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    return text

def send_to_grobid(pdf_path, endpoint):
    """Sends a PDF to the GROBID server and returns the response text (XML or JSON)"""
    with open(pdf_path, 'rb') as pdf_file:
        files = {'input': (pdf_path.name, pdf_file, 'application/pdf')}
        try:
            response = requests.post(endpoint, files=files, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to connect to GROBID: {e}")
            return None

def process_pdf(pdf_file):
    pdf_path = INPUT_DIR / pdf_file
    if not pdf_path.exists():
        print(f"[ERROR] File not found: {pdf_path}")
        return

    print(f"[INFO] Processing {pdf_file}")

    # 1. Extract text
    text = extract_text_from_pdf(pdf_path)
    text_file = OUTPUT_DIR / f"{pdf_path.stem}.txt"
    text_file.write_text(text, encoding='utf-8')
    print(f"[✓] Text extracted to {text_file}")

    # 2. Extract citations and metadata using GROBID
    biblio_xml = send_to_grobid(pdf_path, GROBID_CITATION_URL)
    if biblio_xml:
        biblio_file = OUTPUT_DIR / f"{pdf_path.stem}.biblio.xml"
        biblio_file.write_text(biblio_xml, encoding='utf-8')
        print(f"[✓] Bibliography XML saved to {biblio_file}")
    else:
        print(f"[✗] GROBID citation extraction failed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_text.py report.pdf")
        sys.exit(1)

    pdf_filename = sys.argv[1]
    process_pdf(pdf_filename)