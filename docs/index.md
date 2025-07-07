---
title: ""
layout: home
---

# Building a Knowledge Graph for Integral Ecology

Welcome to the Digital Library of Integral Ecology — a collaborative, open-source project exploring how we can use natural language processing (NLP), ecological knowledge, and graph databases to build better tools for environmental research and action.

This tutorial series walks through how we are building a multilingual, entity-aware, citation-rich **knowledge graph** from ecological reports and academic literature.

Whether you're a researcher, librarian, activist, or simply curious, these guides will help you understand and contribute to our work — no technical background required.

## Tutorial Series

Here’s what we’ll explore together:

1. **[What Is a Knowledge Graph for Integral Ecology?](./posts/01_intro/)**  
   Introduction to what we’re building and why it matters.

2. **[Building Blocks: Documents, Entities, and Relationships](./posts/02_building_blocks/)s**  
   How reports are transformed into structured, searchable networks of knowledge.

3. **[From PDF to Text: Extracting Meaning from Documents](./posts/03_pdf_to_text/)**  
   Learn how we pull clean, useful text from messy PDFs and scientific citations.

4. **[Tagging the World: Finding Places, Plants, and Ideas with AI](./posts/04_entity_tagging/)**  
   How NLP tools identify ecological concepts, organizations, and more.

5. **[Stitching the Graph: Saving Knowledge to Neo4j](./posts/05_graph_database/)**  
   How our documents and entities are stored and visualized as a graph.

6. **[Annotation: Teaching the System to Be Smarter](./posts/06_annotation/)**  
   A look at Doccano and how humans refine machine learning.

7. **[Training Our Own Ecological Language Model](./posts/07_training_model/)**  
   Turning annotations into a smarter, ecology-specific NER system.

8. **[Evaluating the Results: Accuracy, Speed, and Insight](./posts/08_evaluation/)**  
   Measuring how well our models work, and what they help us uncover.

9. **[Contribute: Join the Digital Library of Integral Ecology](./posts/09_contribute/)**  
   How you can help build and grow this open knowledge commons.

---

## Get Started

All code is open-source and Dockerized:

```bash
git clone https://github.com/clirdlf/dlie_knowledge_graph.git
cd dlie_knowledge_graph
make build
make pipeline PDF=your_report.pdf
```

You’ll extract entities, visualize the graph, and export data for annotation — in just a few steps.

---
## 🤝 Get Involved

* 📚 Contribute reports or documents
* 🧑‍🔬 Help annotate and improve the language models
* 🌐 Add support for your language or region
* 💻 Improve the pipeline or add visualizations

See the [GitHub]() repository for details.

---
 
*This work is open to all. Inspired by Laudato Si’ and committed to the care of our common home.*
