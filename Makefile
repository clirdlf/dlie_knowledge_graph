# Project Makefile for Digital Library of Integral Ecology

# Configurable file and paths
PDF ?= sample.pdf
BASENAME := $(basename $(notdir $(PDF)))
ENV_FILE := .env

# Docker targets
build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down && docker compose up -d

logs:
	docker compose logs -f

# Worker setup
install-worker:
	docker compose run worker pip install -r requirements.txt

web:
	cd docs && pnpm start

# Pipeline
pipeline:
	@echo "Running full pipeline on $(PDF)"

	docker compose run worker python extract_text.py $(PDF)
	docker compose run worker python ner_pipeline.py /data/output/$(notdir $(basename $(PDF)).txt)
	docker compose run worker python graph_upload.py /data/output/$(notdir $(basename $(PDF)).entities.json)
	docker compose run worker python export_doccano.py /data/output/$(notdir $(basename $(PDF)).entities.json)

# Run the pipeline on all PDFs in /data/input
all-pdfs:
	@for file in $$(ls data/input/*.pdf); do \
		name=$$(basename $$file); \
		echo "🔁 Running pipeline on $$name..."; \
		make pipeline PDF=$$name; \
	done

train-model:
	docker compose run worker bash -c "\
	  python -m spacy train config.cfg \
	    --paths.train /data/doccano/train.jsonl \
	    --paths.dev /data/doccano/dev.jsonl \
	    --output /data/output"

evaluate-model:
	docker compose run worker python -m spacy evaluate /data/output/model-best /data/doccano/dev.jsonl

# Doccano and Neo4j
open-doccano:
	open http://localhost:8000

open-neo4j:
	open http://localhost:7474

# Cleanup
clean:
	rm -rf data/output/*
	rm -rf data/doccano/*
	rm -rf data/grobid/*
	rm -rf data/neo4j/data/*
	rm -rf data/neo4j/logs/*

.PHONY: build up down restart logs install-worker pipeline clean open-doccano open-neo4j