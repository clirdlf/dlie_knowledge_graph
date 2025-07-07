---
title: "From PDF to Text: Extracting Meaning from Documents"
layout: post
---

# From PDF to Text: Extracting Meaning from Documents

The first step in building a knowledge graph for integral ecology is simple in concept — but tricky in practice:

> How do we get clean, usable **text** from messy, multilingual **PDF reports**?

This post explains how we extract both the **raw text** and the **structured citations** from reports using two tools:
- PyMuPDF for text
- GROBID for citations and metadata

---

## Why This Matters

PDFs are designed for printing, not for reading by machines.

They can include:
- Columns and footnotes
- Images, tables, and scanned pages
- Embedded fonts or malformed characters
- Multiple languages in one document

If we want to detect entities and link knowledge later, we need high-quality **plain text**.

---

## Step 1: Extract Text with PyMuPDF

We use [`PyMuPDF`](https://pymupdf.readthedocs.io/) (also known as `fitz`) to extract the text page-by-page from a PDF.

It:
- Preserves layout well
- Handles multiple languages
- Works with scanned+OCR’d documents if text is embedded

**Example output:**

```plaintext
The Amazon rainforest is shrinking rapidly.

WWF reported that deforestation increased 12% in 2023.
```

This text gets saved as `report.txt`.

## Step 2: Extract Citations with GROBID

Next, we use [GROBID](https://github.com/kermitt2/grobid), a tool that reads the bibliography and metadata of academic papers and reports.

GROBID converts messy citation lists like:

> [12] Smith, J., “Biodiversity and Forests”, Nature, 2020

Into structured, machine-readable **TEI XML**, which can include:

* Title
* Authors
* Year
* Journal or publisher
* DOI or identifiers

We save this as `report.biblio.xml`.

Later in the pipeline, this will help us:

* Build **:CITES relationships** in the graph
* Match references across reports
* Cluster similar reports by their sources

## How This Works in Code

Our system includes a script that does this automatically:

```bash
python extract_text.py my-report.pdf
```

It will:

1.	Extract the full text using PyMuPDF → `my-report.txt`
2.	Send the PDF to the GROBID API → `my-report.biblio.xml`

The script runs inside a Docker container and outputs files to the `/data/output/` folder.

## Try It Yourself

If you’ve followed the setup from [Part 2](/posts/20_building_blocks/), you can run:

```
make pipeline PDF=my-report.pdf
```

This will:

* Extract text and citations
* Tag entities (coming up in Part 4)
* Load data into Neo4j
* Export annotated text for review

Check the results in `data/output/` — you’ll see `.txt`, `.entities.json`, and `.biblio.xml` files.

---

## What We Learned

* PDFs are tricky, but PyMuPDF gives us reliable plain text
* GROBID gives us structured citations, ready for linking
* Clean text is the foundation for everything that follows

---

What’s Next?

In the next post, we’ll explore how we tag entities in the text using AI — recognizing organizations, locations, ecological concepts, and more.

👉 [Continue to Part 4 »](04_entity_tagging)
