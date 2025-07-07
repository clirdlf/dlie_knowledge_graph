# 🌿 Digital Library of Integral Ecology – Knowledge Graph Pipeline

This project builds a multilingual, entity-linked **knowledge graph** from ecological reports, NGO publications, and scientific papers. It extracts meaningful concepts (organizations, locations, ecological ideas, citations) and connects them into an interactive graph database for search, analysis, and model training.

> 💡 Designed for researchers, practitioners, and communities working at the intersection of **environmental science, ethics, policy, and spirituality**.

---

## 🔍 What It Does

- 🧾 Extracts clean text from messy PDFs using PyMuPDF and GROBID
- 🧠 Tags key entities (e.g. `ORG`, `LOC`, `ECO_CONCEPT`) using spaCy and TaxoNERD
- 🧮 Uploads them to a graph database (Neo4j)
- ✍️ Exports data to Doccano for human annotation
- 🤖 Trains custom ecological language models
- 📊 Evaluates model accuracy, speed, and multilingual coverage
- 📚 Publishes tutorials via GitHub Pages

---

## Quick Start

### ✅ Requirements

- [Docker](https://www.docker.com/)
- [Make](https://www.gnu.org/software/make/)

### Clone the repo

```bash
git clone https://github.com/clirdlf/dlie_knowledge_graph.git
cd dlie_knowledge_graph
cp .env.example .env  # or create your own
```

## Start the System

```
make build
make up
```

This launches:

* worker container (NLP + Python scripts)
* neo4j database
* grobid citation parser
* doccano annotation UI
* Jekyll blog server (optional)

## Folder Structure

```plaintext
data/
  input/       # Input PDFs
  output/      # Extracted .txt, .entities.json, .biblio.xml
  doccano/     # Annotation exports

worker/
  extract_text.py
  ner_pipeline.py
  graph_upload.py
  export_doccano.py

docs/
  posts/       # Tutorial blog posts for GitHub Pages
```

## Run the Full Pipeline

```bash
make pipeline PDF=AGR2022.pdf
```

This will:

1. Extract text and citations
2. Tag entities (spaCy + TaxoNERD)
3. Upload to Neo4j
4. Export Doccano annotation file

Results will appear in `data/output/` and `data/doccano/`.

## Annotate with Doccano

Visit: <http://localhost:8000>

Default login:

* **Username:** admin
* **Password:** admin

You can annotate extracted entities and improve training data.

## Train a Custom NER Model

```bash
make train-model
```

This will train a spaCy NER pipeline using your Doccano data.

## View the Knowledge Graph

Visit: <http://localhost:7474>


Login with:

* **Username:** neo4j
* **Password:** apassworddmin

Try a Cypher query:

```cypher
MATCH (d:Document)-[:MENTIONS]->(e:Entity)
RETURN d, e
```

## Tutorial Series (Docs)

See the full walkthrough on [GithubPages]()

## Contribute

* 📚 Suggest reports in multiple languages (PDFs welcome!)
* 🧠 Annotate documents via Doccano
* 🧑‍💻 Improve the code or spaCy pipelines
* 🌍 Help translate models and tutorials

License

This project is open-source under the [MIT License](LICENSE). Data and training outputs may be subject to original source licensing.

---

> 🕊️ Part of the Digital Library of Integral Ecology – building multilingual tools for ecological understanding and action.