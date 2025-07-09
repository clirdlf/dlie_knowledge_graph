---
title: "Training Our Own Ecological Language Model"
slug:    Turning annotations into a smarter, ecology-specific NER system.
date: 2025-06-07
layout: post
---

# Training Our Own Ecological Language Model

We’ve built a working NLP pipeline that tags organizations, locations, and ecological concepts from multilingual reports. We’ve even used Doccano to correct and improve those tags.

Now it’s time to **teach the system** to do better — by training our own custom NER model using the annotated data.

This post explains how we take human-labeled examples and turn them into a smarter, more accurate **ecological language model**.

---

## Why Train a Custom Model?

spaCy’s built-in models are trained on general-purpose data. They work well, but they don’t understand:

- Domain-specific terms like *“climate resilience”*, *“eco-spirituality”*, or *“integral development”*
- New languages or spelling variants
- Cross-domain relationships common in integral ecology (science + ethics + economics)

Training your own model lets you:

- Add new entity types (e.g. `ECO_CONCEPT`)
- Improve accuracy for your documents
- Adapt the system to your language and context

---

## Tools We Use

We use [spaCy](https://spacy.io)’s training framework. It supports:

- Training from scratch or fine-tuning
- Evaluation metrics (precision, recall, F1)
- Easy use of exported Doccano data

---

## From Doccano to Training Data

After annotating in Doccano:

1. Export your project as `.jsonl`
2. Use a converter to turn that into spaCy format:

```bash
spacy convert yourfile.jsonl ./train_data --lang en --ner
```

This gives you `.spacy` binary files for training.

Or use a Python script to convert to `train.json`, `dev.json` split manually.

⸻

##  Training the Model

1.	Create a config file:

```bash
python -m spacy init config ./config.cfg --lang en --pipeline ner
```

2.	Edit `config.cfg `to match your needs (entity labels, GPU, batch size, etc.)
3.	Prepare training assets:

```bash
python -m spacy init fill-config config.cfg config_final.cfg
```

4. Train the model:

```bash
python -m spacy train config_final.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy
```

When done, your trained model will be in:

```bash
./output/model-best
```

You can load it like this:

```python
import spacy
nlp = spacy.load("output/model-best")
```

## Measuring Progress

During training, spaCy tracks:

* **Precision** — how many predicted entities were correct
* **Recall** — how many true entities it found
* **F1 Score** — a balance of the two

This helps you compare:

* Pre-trained model (baseline)
* Your fine-tuned model (specialized)

⸻

## Try It Yourself

Once you have annotations from Doccano:

```bash
make train-model
```

Or step through each stage with:

```bash
python -m spacy init config ./config.cfg --lang en --pipeline ner
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy
```

Test the result:

```python
nlp = spacy.load("output/model-best")
doc = nlp("WWF works on climate resilience in the Amazon rainforest.")
print([(ent.text, ent.label_) for ent in doc.ents])
```

---

## A Living Model

As more reports are added and more annotations made, we can:

* Retrain the model periodically
* Add multilingual support (e.g. `fr`, `es`, `zh`)
* Extend to more entity types (like `SPECIES`, `DOCUMENT`, `THEOLOGICAL_TERM`)

This is how the Digital Library of Integral Ecology gets smarter over time — powered by human insight and collaborative learning.

⸻

## What’s Next?

In the final post, we’ll evaluate the full system and compare how well the pipeline performs **before and after training**, across languages and document types.
