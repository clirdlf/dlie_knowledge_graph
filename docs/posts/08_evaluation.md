---
title: "Evaluating the Results: Accuracy, Speed, and Insight"
layout: post
---

# 📊 Evaluating the Results: Accuracy, Speed, and Insight

We’ve come a long way — from PDFs to graphs, from automatic tagging to human annotation, and finally to training our own ecological NLP model.

But how do we know if it’s working?

In this post, we’ll explore how to evaluate your pipeline and model using both **standard NLP metrics** and **real-world ecological insight**.

---

## 🎯 Why Evaluate?

Evaluation helps us understand:

- ✅ Is the model tagging entities accurately?
- ✅ Does it work well across languages?
- ✅ Is it fast enough for real-world use?
- ✅ What kinds of mistakes does it make?

Evaluation isn’t just about numbers — it’s about improving **trust**, **transparency**, and **impact**.

---

## Key Metrics

### Precision
The % of predicted entities that were correct  
> Did it predict something meaningful?

### Recall
The % of correct entities that were successfully predicted  
> Did it miss important things?

### F1 Score
The balance of precision and recall  
> A good all-around indicator

These metrics are calculated by comparing your model's output to **human-annotated data**, usually exported from Doccano.

---

## How to Evaluate with spaCy

After training, spaCy automatically evaluates on your dev/test set and shows:

```bash
✔ Accuracy: 89.2%
✔ Precision: 88.5%
✔ Recall: 90.1%
✔ F1 Score: 89.3
```

You can also evaluate manually using:

```bash
python -m spacy evaluate ./output/model-best ./dev.spacy
```

Or export annotated JSONL and compare predictions programmatically.

## Speed and Runtime

You can also evaluate **how fast** your model runs:

```python
import spacy, time
nlp = spacy.load("output/model-best")
text = "The WWF is active in the Amazon on climate resilience."

start = time.time()
doc = nlp(text)
print([(ent.text, ent.label_) for ent in doc.ents])
print("Time:", round(time.time() - start, 4), "seconds")
```

This helps you decide:

* Which model is best for live pipelines vs. batch runs
* When to use sm vs. `lg` or `trf` models

---

## Beyond Accuracy: Ecological Insight

Numbers matter, but so does **usefulness**!

Ask:

* Does the graph help us find new connections?
* Are multilingual documents being fairly represented?
* Does it highlight underrepresented organizations or regions?
* Is it surfacing unexpected insights for researchers or communities?

These qualitative measures can be just as valuable as F1 score.

## Try It Yourself

After training, run:

```bash
python -m spacy evaluate output/model-best dev.spacy
```

Or test it interactively:

```python
import spacy
nlp = spacy.load("output/model-best")
doc = nlp("UNEP published a report on ecosystem resilience in East Africa.")
print([(ent.text, ent.label_) for ent in doc.ents])
```

Then compare the results to the baseline model (`en_core_web_sm`) or TaxoNERD.

---

You’ve now seen the full lifecycle:

1.	Extract text and citations from reports
2.	Tag entities across languages
3.	Upload to a knowledge graph
4.	Annotate and refine human feedback
5.	Train and evaluate your own model

You’re ready to contribute — or build your own ecological pipeline.

[👉 Continue to Part 9 »]()
