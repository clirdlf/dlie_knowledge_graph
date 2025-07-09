---
title: "Building Blocks: Documents, Entities, and Relationships"
slug: How reports are transformed into structured, searchable networks of knowledge.
date: 2025-06-02
layout: post
---

In our last post, we introduced the vision: building a knowledge graph for **integral ecology**, a way to connect people, places, organizations, and ideas across languages and disciplines.

But how exactly do we turn messy PDFs and complex reports into a meaningful, searchable web of knowledge?

We start with three key building blocks:

---

## 1. Documents

The foundation of our knowledge graph is a **document** — a report, academic paper, policy brief, or even a faith-based reflection.

Each document is:

- A single file (usually a PDF)
- With a title, language, source (UNEP, WWF, OpenAlex, etc.)
- That contains many sentences — and lots of **information hidden in plain text**

We treat each document as a **node** in the graph, and from there, we extract meaning.

---

## 2. Entities

Entities are **things that the document talks about** — people, organizations, species, places, and ecological concepts.

For example:

| Entity Text          | Label       |
|----------------------|-------------|
| Amazon rainforest     | `LOCATION`  |
| WWF                   | `ORG`       |
| climate resilience    | `ECO_CONCEPT` |
| Laudato Si’           | `DOCUMENT`  |

Our system uses **Natural Language Processing (NLP)** tools to automatically recognize these entities in many languages, with models trained on large text collections.

Later, we’ll even **fine-tune our own models** to be more accurate for ecological language.

---

## 3. Relationships

The real power of a knowledge graph comes from the **connections between entities**, also called **edges** or **relationships**.

Some examples:

- A document **MENTIONS** an entity (e.g. a location, organization, etc.)
- A document **CITES** another document 
- A concept **IS_RELATED_TO** another concept 
- An organization **WORKS_IN** a specific region

These relationships turn isolated data points into an **interconnected network** — where you can explore patterns, paths, and shared meaning.

---

## Putting It Together

Here's a simple example:

```cypher
[WWF Report]–MENTIONS–>[Amazon rainforest]
–MENTIONS–>[climate resilience]
–CITES—–>[IPBES 2022 Report]
```

In the graph database, each of these is a **node** (document or entity) and each arrow is a **relationship**.

We can now:

- Search for all reports mentioning "climate resilience"
- Find which NGOs cite a particular scientific assessment
- Map ecological priorities across language and region

---

## Why It Matters

This model gives us:

- **Structure** — so we can search and analyze consistently
- **Scalability** — works for hundreds or thousands of documents
- **Interoperability** — can be visualized, queried, and shared

And it sets the stage for automation, collaboration, and learning.

---

## Try It Yourself: Clone & Run the Project

You can explore and run this pipeline locally using Docker (and the terminal)

### Prerequisites

- [Docker](https://www.docker.com/) (Desktop or CLI)  
- [Git](https://git-scm.com/)

### Step 1: Clone the Repository

```bash
git clone https://github.com/clirdlf/dlie_knowledge_graph.git
cd dlie_knowledge_graph
```

### Step 2: Build and Start the System

```bash
make build
make up
```

This will spin up:

* [GROBID](https://grobid.readthedocs.io/en/latest/) for citation parsing
* [Neo4j](https://neo4j.com/) for the knowledge graph
* [Doccano](https://doccano.github.io/doccano/) for annotation
* A Python environment for text and entity extraction

Then, you can run the full pipeline like this:

```bash
make pipeline PDF=/data/input/sample1.pdf
```

You’ll find the results in the `data/output/` and `data/doccano/` folders.


## What’s Next?

In the next post, we’ll start **extracting text from real reports**, even messy PDFs, using smart tools like PyMuPDF and GROBID.
