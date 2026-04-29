@echo off
REM Active l'environnement virtuel et lance le serveur FastAPI
call .venv\Scripts\activate
uvicorn main:socket_app --reload
pause
