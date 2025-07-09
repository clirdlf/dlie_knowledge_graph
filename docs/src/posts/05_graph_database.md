---
title: "Stitching the Graph: Saving Knowledge to Neo4j"
slug:    How our documents and entities are stored and visualized as a graph.
date: 2025-06-05
layout: post
---

So far, we’ve extracted clean text from ecological reports and used AI to identify important entities like organizations, places, and ecological concepts.

But identifying entities is only half the story. Now we need to **connect** them — to build our **knowledge graph**.

In this post, we show how we use **Neo4j**, a graph database, to stitch everything together into a network of knowledge.

---

## What is a Graph Database?

A **graph database** stores information as **nodes** (things) and **relationships** (connections).

Unlike traditional databases, which store rows and columns, a graph lets you explore:

```plaintext
(WWF Report) –MENTIONS–> (Amazon rainforest)
–CITES—–> (IPBES 2019 Report)
–MENTIONS–> (climate resilience)
```

Neo4j is the most popular open-source graph database. It’s:
- Visual
- Easy to query (using a language called Cypher)
- Designed to handle relationships efficiently

---

## 🧱 What We Store in the Graph

Each document and entity we extract becomes a **node**, and their connections are modeled as **relationships**.

### Node Types

- `:Document` — the report itself  
- `:Entity` — an extracted item (e.g. “WWF”, “Amazon rainforest”)  

Each node has properties like:

```cypher
(:Document {name: "wwf_amazon_report", lang: "en"})
(:Entity {text: "climate resilience", label: "ECO_CONCEPT"})
```

### Relationship Types

* `(:Document)-[:MENTIONS]->(:Entity)`
* `(:Document)-[:CITES]->(:Document)` (coming soon via citation parsing)

These relationships make the knowledge **navigable**, not just searchable.

## How It Works in Code

After entity tagging, we load the data into Neo4j using:

```bash
python graph_upload.py my-report.entities.json
```

This script:

1.	Loads the entity JSON file
2.	Creates the `:Document` node
3.	Creates one `:Entity` node per unique mention
4.	Connects them with `:MENTIONS` relationships

You can view this graph in Neo4j’s browser:

<http://localhost:7474>

Use the default login:

* **Username:** neo4j
* **Password:** password

And run a query like:

```cypher
MATCH (d:Document)-[:MENTIONS]->(e:Entity)
RETURN d, e
```

---

##  Try It Yourself

If you’ve run the full pipeline:

```bash
make pipeline PDF=my-report.pdf
```

The upload to Neo4j is done automatically. Otherwise, you can run it directly:

```bash
docker compose exec worker python graph_upload.py my-report.entities.json
```

Then open Neo4j in your browser and start exploring the graph!

---

## What Can You Do With It?

Once in the graph, you can:

* Find all documents mentioning a specific concept
* Discover what organizations work in similar regions
* Visualize themes and citations across languages
* Prepare data for annotation or deeper AI training

This is where our static data becomes **living knowledge**.

---

## What’s Next?

Now that our knowledge is structured and searchable, we’ll look at how to **export the data to Doccano**, a simple annotation tool that lets humans teach the system to improve over time.
