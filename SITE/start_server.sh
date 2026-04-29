#!/bin/bash
# Active l'environnement virtuel et lance le serveur FastAPI
source .venv/bin/activate
uvicorn main:socket_app --reload
