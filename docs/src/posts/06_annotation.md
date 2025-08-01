---
title: "Annotation: Teaching the System to Be Smarter"
slug:    A look at Doccano and how humans refine machine learning.
date: 2025-06-06
layout: post
---

Our pipeline can already extract text from reports, tag entities, and build a multilingual knowledge graph, but how accurate is it?

The truth is: even good AI needs **human correction**. That's where **annotation** comes in.

In this post, we’ll show you how we use **Doccano**, a friendly web interface, to correct the output of our pipeline and help the model improve over time.

---

## Why Annotation Matters

Even the best models make mistakes:

- Misclassifying entities (e.g. "Amazon" as a product instead of a forest)
- Missing subtle ecological terms (like “resilience” or “eco-conversion”)
- Struggling with under-represented languages (like Arabic) or complex phrases

Annotation lets humans:

- Correct the labels
- Add missing terms
- Build reliable training data

It’s like proofreading, but for a machine learning system.

---

## What is Doccano?

[Doccano](https://doccano.github.io/doccano/) is an open-source tool for **annotating text for NLP tasks**.

It provides:

- A browser-based interface
- Support for named entity recognition (NER), classification, translation, and more
- Role-based user access
- Easy data import and export

We use Doccano to refine the results of running the `ner_pipeline.py` script.

---

## Exporting to Doccano Format

After entity tagging, we export the results in [JSONL format](https://github.com/doccano/doccano/blob/master/docs/api.md#annotation-format):

```bash
python export_doccano.py my-report.entities.json
```

Which creates:

```json
{
  "text": "The WWF report on the Amazon rainforest...",
  "labels": [[4, 7, "ORG"], [20, 36, "LOC"]]
}
```

This format can be imported directly into Doccano.

---

##  Using Doccano Locally

If you’re running the project with Docker Compose, Doccano is already available at:

<http://localhost:8000>

Log in with

* **Username:** `admin`
* **Password:** `password`

From there, you can 

1. Create a new NER project - be sure to select **Sequence Labeling**
2. Import your `.jsonl` file (generated in previous step - `data/output/)
3. Start tagging!

---

## The Feedback Loop

Once documents are annotated in Doccano, we:

1. Export the clean annotations
2. Convert them to spaCy training format
3. Fine-tune a custom NER model

This cycle helps the system:

* Improve tagging accuracy
* Recognize new or uncommon terms
* Adapt to multilingual and ecological contexts

We call this process **active learning**.

---

## Try It Yourself

If you’ve already run:

```bash
make pipeline PDF=my-report.pdf
```

Then a Doccano file will be created at:

```bash
data/doccano/my-report.entities.jsonl
```

Import this file into your Doccano project and try refining the labels!


## Who Can Help?

Annotation is one of the best ways to contribute, especially if you:

* Are a researcher in ecology, theology, or social sciences
* Are bilingual or multilingual
* Want to help shape AI to better understand the world

All you need is careful attention. **No coding required!**

## What’s Next?

Now that we have clean, annotated data, we’re ready to train our own **ecologically informed NER model**.

In the next post, we’ll walk through how to train a custom spaCy pipeline using your Doccano data.
