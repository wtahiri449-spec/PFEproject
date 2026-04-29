# ESTBM Portal - Plateforme Académique Intelligente

## Description
Plateforme web complète pour la prédiction de performance académique, la gestion des groupes, la messagerie temps réel, et l’administration des étudiants/professeurs.

- API sécurisée (FastAPI, JWT, SQLite)
- Machine Learning (scikit-learn)
- Interface moderne (Bootstrap, Chart.js)
- Authentification et gestion des rôles (étudiant/professeur)
- Messagerie temps réel (Socket.IO)

## Installation

1. Cloner le projet et se placer dans le dossier :
   ```bash
   git clone <repo_url>
   cd SITE
   ```
2. Installer les dépendances Python :
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
3. Lancer le serveur :
   ```bash
   uvicorn main:socket_app --reload
   ```
4. Accéder à l’interface web :
   - Ouvrir index.html dans un navigateur
   - Ou déployer sur un serveur web (recommandé)

## Fonctionnalités principales
- Inscription/connexion sécurisée (étudiant & enseignant)
- Prédiction de performance académique (IA)
- Messagerie directe temps réel
- Gestion des groupes et emplois du temps
- Interface responsive et moderne

## Structure du projet
- `main.py` : API FastAPI, Socket.IO, routes principales
- `auth_routes.py` : Authentification, inscription, connexion
- `models.py` : Modèles SQLAlchemy (utilisateurs)
- `database.py` : Connexion et initialisation SQLite
- `security.py` : Hachage et vérification des mots de passe
- `auth_utils.py` : Gestion des tokens JWT
- `entrainement.py` : Entraînement et sauvegarde du modèle ML
- `generate_dataset_updated.py` : Génération de jeux de données
- `index.html`, `login.html`, `inscription.html` : Interface utilisateur

## Déploiement
- Pour un déploiement professionnel, utiliser un serveur (Render, Azure, etc.)
- Adapter la configuration CORS et les variables secrètes (voir `auth_utils.py`)

## Auteurs
- Projet ESTBM - 2026
