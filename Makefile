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

jekyll:
	cd docs && bundle exec jekyll serve -l

# Pipeline
pipeline:
	@echo "Running full pipeline on $(PDF)"
	docker compose run worker python extract_text.py $(PDF)
	docker compose run worker python ner_pipeline.py $(BASENAME).txt
	docker compose run worker python graph_upload.py $(BASENAME).entities.json
	docker compose run worker python export_doccano.py $(BASENAME).entities.json

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