docker compose run worker python extract_text.py /data/input/AGR2022.pdf
docker compose run worker python ner_pipeline.py /data/output/AGR2022.txt
docker compose run worker python graph_upload.py /data/output/ARG2022.biblio.xml