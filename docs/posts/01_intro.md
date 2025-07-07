---
title: "What is a Knowledge Graph for Integral Ecology?"
layout: post
---

# What is a Knowledge Graph for Integral Ecology?

We live in an age of overwhelming information, but ecological knowledge, wisdom, and action often remain **fragmented**, buried in reports, scattered across languages, or locked in formats only specialists can access.

That’s where the **Digital Library of Integral Ecology** comes in. Our mission is to bring this information together, from scientific papers to NGO reports to faith-based reflections, into a single, interconnected digital library that helps researchers, educators, and communities act for the common good. One of the tools that helps us discovery and interrogate integral ecology is a knowledge graph. This codebase and set of tutorials will walk you through the technologies, opportunities, and tradeoffs in building this feature of the Digitial Library of Integral Ecology.

---

## What Do We Mean by "Integral Ecology"?

The term *integral ecology* comes from *[Laudato Si’](https://www.vatican.va/content/francesco/en/encyclicals/documents/papa-francesco_20150524_enciclica-laudato-si.html)*, Pope Francis' encyclical on the environment. It’s about recognizing the **deep connections between ecological, social, cultural, and spiritual concerns**. Climate change, deforestation, loss of biodiversity — these aren’t just technical problems. They are moral ones, economic ones, and spiritual ones too.

Integral ecology asks us to **think in systems**, and to see how everything is connected.

---

## And What’s a Knowledge Graph?

A **knowledge graph** is a way of storing and exploring knowledge by looking at **relationships**. Imagine a big web:

- A report mentions **“Amazon rainforest”**
- It connects to a **location**
- The report is published by **UNESCO**
- It discusses concepts like **resilience** and **biodiversity**
- It cites other documents that are connected too

All of this is represented not just as flat text, but as **linked data** — relationships between concepts, people, places, and ideas. This is what lets us ask better questions and see deeper patterns.

---

## What We're Building

We are creating a system that:

1. **Extracts text** from ecological reports and scientific papers (even in PDF format)
2. **Identifies key concepts**, organizations, places, species, and ideas — in multiple languages
3. **Links them together** in a searchable, visual graph (using Neo4j)
4. **Lets people annotate** and refine that knowledge with simple tools
5. **Trains smarter AI models** over time that understand ecology more deeply

---

## Why It Matters

- Researchers can discover connections across disciplines and languages
- NGOs can map their work to broader systems and goals
- Educators can explore real-world ecological examples interactively
- Communities can build shared understanding of their bioregions

We believe this is a project not just of technology — but of **ecological conversion**.

---

## What’s Next?

In the next post, we’ll walk through the building blocks of the graph: **documents, entities, and relationships**, and how we transform text into structure.

👉 [Continue to Part 2 »](./02_building_blocks.html)

---

*This project is part of the Digital Library of Integral Ecology — open, multilingual, and collaborative.*