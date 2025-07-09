---
title: "Tagging the World: Finding Places, Plants, and Ideas with AI"
slug: How NLP tools identify ecological concepts, organizations, and more.
layout: post
---

Once we've extracted clean text from a PDF, the next step is to **understand what’s being talked about**.

That’s where Natural Language Processing (NLP) comes in.

We use NLP to scan the text and find key pieces of information — like:

- Locations (e.g. "Amazon rainforest")
- Organizations (e.g. "WWF")
- Ecological concepts (e.g. "resilience", "biodiversity loss")
- Citations (e.g. "IPBES 2019 Report")

Each of these is called an **entity**, and this process is called **Named Entity Recognition (NER)**.

---

## What is Named Entity Recognition?

NER is a type of AI model that reads text and labels the parts that represent real-world things.

Example:

```plaintext
Original text:
The WWF report on the Amazon rainforest highlights climate resilience strategies.

NER output:
[ORG: WWF], [LOC: Amazon rainforest], [ECO_CONCEPT: climate resilience]
```

This gives us structured data from unstructured sentences, and helps us populate our knowledge graph with **nodes and connections**.

---

## Tools We Use

### spaCy

We use spaCy, a popular open-source NLP library that can:

* Work in English, Spanish, French, Chinese, Russian, and more
* Recognize standard entities like ORG, LOC, PERSON, etc.
* Run fast and integrate easily with Python

### TaxoNERD

For ecological texts, general NLP isn’t enough — so we also use TaxoNERD, a tool trained to detect ecological and taxonomic entities, like:

* Ecosystem types
* Species groups
* Environmental terms

TaxoNERD uses a model called BioBERT and is specialized for ecological language.

### Multilingual Support

We also include spaCy models for:

* fr_core_news_lg (French)
* es_core_news_lg (Spanish)
* zh_core_web_trf (Chinese)
* xx_ent_wiki_sm (basic multilingual)

This makes the system l**anguage-aware**, even when documents span continents.

--- 

## How It Works in Code

The tagging is handled by this command:

```bash
python ner_pipeline.py my-report.txt
```

Which produces:

```json
{
  "text": "...",
  "entities": [
    {"start": 4, "end": 22, "label": "LOC", "text": "Amazon rainforest"},
    {"start": 31, "end": 34, "label": "ORG", "text": "WWF"},
    {"start": 45, "end": 63, "label": "ECO_CONCEPT", "text": "climate resilience"}
  ]
}
```

This is saved as `my-report.entities.json` in the `data/output/` folder.

---

## Why This Matters

Recognizing entities allows us to:
* Link a sentence to the right concepts
* Group reports by theme or region
* Connect related documents, even across languages
* Support annotation and model training

It’s the first step toward turning plain text into a semantic map.

---

## Try It Yourself

If you’ve already extracted text using:

```bash
make pipeline PDF=my-report.pdf
```

The entity tagging will run automatically. Check the output in:

```bash
data/output/my-report.entities.json
```

You can also run it independently:

```bash
docker compose exec worker python ner_pipeline.py my-report.txt
```

---

## What’s Next?

Next, we’ll take these entities and load them into Neo4j — our graph database — where we can start to visualize and query relationships.

