---
title: "Contribute: Join the Digital Library of Integral Ecology"
slug:    How you can help build and grow this open knowledge commons.
date: 2025-06-10
layout: post
---


This project is not just about building technology — it’s about building **community**.

The Digital Library of Integral Ecology is a shared, open infrastructure for people who care about the Earth, its people, and our common future. It brings together knowledge from science, policy, spirituality, and grassroots voices — and we want you to be part of it.

---

## Ways to Get Involved

You don’t need to be a coder or a data scientist to contribute. Here are some ways anyone can help:

### Annotate Reports
Help tag ecological concepts, organizations, places, and ideas in documents using [Doccano](https://github.com/doccano/doccano). No technical skill required — just your careful reading.

### Share Reports and Sources
We’re always looking for ecological reports in **different languages** and from **diverse contexts** (NGOs, indigenous communities, policy, faith-based orgs, etc.).

Send us PDFs or links to reports that should be included in the graph.

### Train the AI
If you're technical, help us fine-tune our ecological NER models using annotated data. Or contribute to multilingual tagging tools and model evaluation.

### Translate and Extend
Want to add new languages? New entity types like **species**, **spiritual practices**, or **sacred sites**? We're building a framework that’s meant to grow with your contributions.

---

## Technical Contributors

If you’re a developer, here’s where you can help:

- Improve entity extraction and citation linking
- Enhance multilingual NLP support
- Automate ingestion from online archives
- Build interactive search and visualization tools
- Create public datasets from the graph (JSONL, CSV, RDF, etc.)

Our [GitHub repository](https://github.com/clirdlf/dlie_knowledge_graph) includes Docker-based workflows, NLP scripts, a Makefile, and blog documentation — all ready to clone and explore.

---

## How to Get Started

1. Star or fork the project on GitHub: [github.com/clirdlf/dlie_knowledge_graph](https://github.com/clirdlf/dlie_knowledge_graph)

2. Clone the repo:
   
```bash
   git clone https://github.com/clirdlf/dlie_knowledge_graph.git
   cd dlie_knowledge_graph
   make up
```

3.	Try annotating or improving a model:

```bash
make pipeline PDF=my-report.pdf
```

4. Join us on discussions (coming soon)

---

## We’re Building This Together

This project is inspired by the principles of **integral ecology**,  the idea that we must care for both the environment and the most vulnerable people it supports.

Building the Digital Library is a concrete act of hope. It’s a way to turn scattered, siloed knowledge into living, shared understanding.

Whether you’re a researcher, developer, librarian, artist, or student — you are welcome.

---

> “All it takes is one good person to restore hope.” — Pope Francis, Laudato Si’