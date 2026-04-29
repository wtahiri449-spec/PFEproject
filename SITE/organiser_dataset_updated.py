import csv
import os
import shutil

# Créer un dossier pour organiser les fichiers CSV mis à jour
dossier_data = 'dataset_organise_updated'
if os.path.exists(dossier_data):
    shutil.rmtree(dossier_data)
os.makedirs(dossier_data)

# Lire le fichier CSV principal
donnees = []
en_tetes = []

with open('dataset_competences_academiques_updated.csv', 'r', encoding='utf-8-sig') as f:
    lecteur = csv.DictReader(f)
    en_tetes = lecteur.fieldnames
    donnees = list(lecteur)

print(f"✓ Fichier principal chargé: {len(donnees)} étudiants")

# 1. Organiser par Université
print("\n1. Division par Université...")
universites_data = {}
for entree in donnees:
    universite = entree['Universite']
    if universite not in universites_data:
        universites_data[universite] = []
    universites_data[universite].append(entree)

# Sauvegarder par université
for universite, etudiants in universites_data.items():
    nom_fichier = f"{dossier_data}/universite_{universite.replace(' ', '_').replace('é', 'e')}.csv"
    with open(nom_fichier, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=en_tetes)
        writer.writeheader()
        writer.writerows(etudiants)
    print(f"   ✓ {universite}: {len(etudiants)} étudiants")

# 2. Organiser par Spécialité
print("\n2. Division par Spécialité...")
specialites_data = {}
for entree in donnees:
    specialite = entree['Specialite']
    if specialite not in specialites_data:
        specialites_data[specialite] = []
    specialites_data[specialite].append(entree)

# Sauvegarder par spécialité
for specialite, etudiants in specialites_data.items():
    nom_fichier = f"{dossier_data}/specialite_{specialite}.csv"
    with open(nom_fichier, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=en_tetes)
        writer.writeheader()
        writer.writerows(etudiants)
    print(f"   ✓ {specialite}: {len(etudiants)} étudiants")

# 3. Organiser par Année d'Étude
print("\n3. Division par Année d'Étude...")
annees_data = {}
for entree in donnees:
    annee = entree['Annee_Etude']
    if annee not in annees_data:
        annees_data[annee] = []
    annees_data[annee].append(entree)

# Sauvegarder par année
for annee in sorted(annees_data.keys()):
    etudiants = annees_data[annee]
    nom_fichier = f"{dossier_data}/annee_etude_{annee}.csv"
    with open(nom_fichier, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=en_tetes)
        writer.writeheader()
        writer.writerows(etudiants)
    print(f"   ✓ Année {annee}: {len(etudiants)} étudiants")

# 4. Organiser par Niveau de Compétence
print("\n4. Division par Niveau de Compétence...")
competence_data = {}
for entree in donnees:
    niveau = entree['Niveau_Competence_Academique']
    if niveau not in competence_data:
        competence_data[niveau] = []
    competence_data[niveau].append(entree)

# Sauvegarder par niveau de compétence
for niveau in ['Faible', 'Moyen', 'Bon', 'Excellent']:
    if niveau in competence_data:
        etudiants = competence_data[niveau]
        nom_fichier = f"{dossier_data}/competence_{niveau}.csv"
        with open(nom_fichier, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=en_tetes)
            writer.writeheader()
            writer.writerows(etudiants)
        print(f"   ✓ Niveau {niveau}: {len(etudiants)} étudiants")

# 5. Organiser par Genre
print("\n5. Division par Genre...")
genre_data = {'M': [], 'F': []}
for entree in donnees:
    genre = entree['Genre']
    if genre in genre_data:
        genre_data[genre].append(entree)

# Sauvegarder par genre
for genre, label in [('M', 'Masculin'), ('F', 'Feminin')]:
    etudiants = genre_data[genre]
    nom_fichier = f"{dossier_data}/genre_{label}.csv"
    with open(nom_fichier, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=en_tetes)
        writer.writeheader()
        writer.writerows(etudiants)
    print(f"   ✓ Genre {label}: {len(etudiants)} étudiants")

# 6. Organiser par Région
print("\n6. Division par Région...")
regions_data = {}
for entree in donnees:
    region = entree['Region']
    if region not in regions_data:
        regions_data[region] = []
    regions_data[region].append(entree)

# Sauvegarder par région
for region, etudiants in regions_data.items():
    nom_fichier = f"{dossier_data}/region_{region.replace('-', '_')}.csv"
    with open(nom_fichier, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=en_tetes)
        writer.writeheader()
        writer.writerows(etudiants)
    print(f"   ✓ {region}: {len(etudiants)} étudiants")

# 7. Copier le fichier complet au dossier organisé
print("\n7. Copie du fichier complet...")
with open('dataset_competences_academiques_updated.csv', 'r', encoding='utf-8-sig') as src:
    contenu = src.read()
with open(f'{dossier_data}/dataset_complet.csv', 'w', encoding='utf-8-sig') as dst:
    dst.write(contenu)
print(f"   ✓ dataset_complet.csv (tous les étudiants)")

# 8. Créer un fichier d'index
print("\n8. Création d'un index des fichiers...")
index_contenu = """ORGANISATION DU DATASET - INDEX DES FICHIERS CSV
=====================================================
Version mise à jour avec spécialités IA et Digital

FICHIER COMPLET:
- dataset_complet.csv (2000 étudiants)

SPÉCIALITÉS INCLUSES:
✓ IA (Intelligence Artificielle)
✓ Digital (Transformation numérique)
✓ Informatique
✓ Mathematiques
✓ Physique
✓ Chimie
✓ Biologie
✓ Economie
✓ Droit
✓ Ingenierie

FICHIERS PAR SPÉCIALITÉ:
"""

for specialite, etudiants in sorted(specialites_data.items()):
    nom_fichier = f"specialite_{specialite}.csv"
    index_contenu += f"\n- {nom_fichier} ({len(etudiants)} étudiants)"

index_contenu += "\n\nFICHIERS PAR UNIVERSITÉ:\n"
for universite, etudiants in sorted(universites_data.items()):
    nom_fichier = f"universite_{universite.replace(' ', '_').replace('é', 'e')}.csv"
    index_contenu += f"\n- {nom_fichier} ({len(etudiants)} étudiants)"

index_contenu += "\n\nFICHIERS PAR ANNÉE D'ÉTUDE:\n"
for annee in sorted(annees_data.keys()):
    etudiants = annees_data[annee]
    nom_fichier = f"annee_etude_{annee}.csv"
    index_contenu += f"\n- {nom_fichier} ({len(etudiants)} étudiants)"

index_contenu += "\n\nFICHIERS PAR NIVEAU DE COMPÉTENCE:\n"
for niveau in ['Faible', 'Moyen', 'Bon', 'Excellent']:
    if niveau in competence_data:
        etudiants = competence_data[niveau]
        nom_fichier = f"competence_{niveau}.csv"
        index_contenu += f"\n- {nom_fichier} ({len(etudiants)} étudiants)"

index_contenu += "\n\nFICHIERS PAR GENRE:\n"
for genre, label in [('M', 'Masculin'), ('F', 'Feminin')]:
    etudiants = genre_data[genre]
    nom_fichier = f"genre_{label}.csv"
    index_contenu += f"\n- {nom_fichier} ({len(etudiants)} étudiants)"

index_contenu += "\n\nFICHIERS PAR RÉGION (10 fichiers):\n"
for region, etudiants in sorted(regions_data.items()):
    nom_fichier = f"region_{region.replace('-', '_')}.csv"
    index_contenu += f"\n- {nom_fichier} ({len(etudiants)} étudiants)"

index_contenu += "\n\n" + "="*70
index_contenu += "\nTOTAL: " + str(len(donnees)) + " étudiants"
index_contenu += "\nNOMBRE DE FICHIERS: " + str(len(os.listdir(dossier_data)))
index_contenu += "\n" + "="*70

with open(f'{dossier_data}/INDEX.txt', 'w', encoding='utf-8') as f:
    f.write(index_contenu)
print(f"   ✓ INDEX.txt créé")

print("\n" + "="*70)
print("✓ ORGANISATION COMPLÈTE!")
print("="*70)
print(f"Tous les fichiers CSV sont dans le dossier: {dossier_data}/")
print(f"Nombre total de fichiers: {len(os.listdir(dossier_data))}")
print("="*70)
