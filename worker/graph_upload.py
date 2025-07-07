import sys
import json
from pathlib import Path
from neo4j import GraphDatabase

NEO4J_URI = "bolt://neo4j:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

OUTPUT_DIR = Path("/data/output")

def upload_to_neo4j(filename):
    input_path = OUTPUT_DIR / filename
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    doc_name = input_path.stem.replace(".entities", "")
    text = data["text"]
    entities = data["entities"]

    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    with driver.session() as session:
        # Create the document node
        session.write_transaction(create_document_node, doc_name)

        # Create entity nodes and relationships
        for ent in entities:
            session.write_transaction(
                link_entity_to_document,
                doc_name,
                ent["text"],
                ent["label"]
            )

    driver.close()
    print(f"[✓] Uploaded to Neo4j: {doc_name}")

def create_document_node(tx, doc_name):
    query = """
    MERGE (d:Document {name: $name})
    RETURN d
    """
    tx.run(query, name=doc_name)

def link_entity_to_document(tx, doc_name, entity_text, label):
    query = """
    MERGE (e:Entity {text: $text, label: $label})
    ON CREATE SET e.count = 1
    ON MATCH SET e.count = e.count + 1
    WITH e
    MATCH (d:Document {name: $doc_name})
    MERGE (d)-[:MENTIONS]->(e)
    """
    tx.run(query, text=entity_text, label=label, doc_name=doc_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python graph_upload.py report.entities.json")
        sys.exit(1)

    filename = sys.argv[1]
    upload_to_neo4j(filename)