import csv
import random
from datetime import datetime

# Configuration du seed pour reproductibilité
random.seed(42)

# Nombre d'étudiants
n_students = 2000

# Listes de noms et prénoms marocains
prenoms_masculins = ['Mohamed', 'Ahmed', 'Hassan', 'Omar', 'Ali', 'Karim', 'Ibrahim', 'Youssef',
                      'Hicham', 'Adil', 'Abdelhaq', 'Jamal', 'Aziz', 'Rashid', 'Samir', 'Noureddine',
                      'Fouad', 'Hamid', 'Bilal', 'Tariq', 'Walid', 'Jawad', 'Nasir', 'Khalid']

prenoms_feminins = ['Fatima', 'Aisha', 'Leila', 'Nour', 'Zahra', 'Samira', 'Laila', 'Yasmine',
                     'Amina', 'Salma', 'Dina', 'Hana', 'Rania', 'Zohra', 'Layla', 'Insaf',
                     'Jihane', 'Imane', 'Karim', 'Nadia', 'Safiya', 'Maryam', 'Hanaa', 'Rana']

noms_marocains = ['Saidi', 'Belharbi', 'Benchamsi', 'Oufkir', 'Bennani', 'Regaig', 'Abboud', 'Azzouz',
                   'Benmaya', 'Bennis', 'Zahra', 'Serfaty', 'Ettefagh', 'Douiri', 'Elmi', 'Fakhri',
                   'Filali', 'Firdaous', 'Gharib', 'Ghazali', 'Ghouti', 'Hamidoune', 'Hanania', 'Harami',
                   'Hasani', 'Hassan', 'Helali', 'Helaoui', 'Hersi', 'Hessas', 'Hijazi', 'Houbiche',
                   'Houmaidi', 'Housni', 'Hudak', 'Humeida', 'Humes', 'Humidi', 'Hunaidi', 'Hungari',
                   'Husain', 'Husam', 'Husami', 'Husayn', 'Huscai', 'Huskier', 'Husly', 'Ibrahimi',
                   'Idrissi', 'Ifrah', 'Ignjatovic', 'Ikhlas', 'Ilahi', 'Ilias', 'Ilyass', 'Imadeddine',
                   'Imaidi', 'Iman', 'Imane', 'Imani', 'Imanuel', 'Imboden', 'Imran', 'Imrani', 'Inani']

regions = ['Casablanca-Settat', 'Fez-Meknes', 'Marrakech-Safi', 
           'Tanger-Asifa', 'Rabat-Sale-Kenitra', 'Souss-Massa',
           'Beni-Mellal-Khenifra', 'Draa-Tafilat', 'Guelmim-Oued-Noun',
           'Laayoune-Sakia-Hamra']

universites = ['Université Mohammed V', 'Université Al Quaraouiyine',
               'Université Cadi Ayyad', 'Université Sidi Mohamed Ben Abdellah',
               'Université Hassan II', 'Université Abdelmalek Essaadi']

diplomes = ['Licence', 'Master', 'Diplome']

specialites = ['Informatique', 'Mathematiques', 'Physique', 'Chimie',
               'Biologie', 'IA', 'Digital', 'Economie',
               'Droit', 'Ingenierie']

langues_principales = ['Arabe', 'Francais', 'Amazigh']
niveaux_langue = ['Basique', 'Intermediaire', 'Avance']
situations = ['Faible', 'Moyen', 'Bon']
niveaux_competence = ['Faible', 'Moyen', 'Bon', 'Excellent']

# Domaines universitaires par université
domaines_email = {
    'Université Mohammed V': 'um5.ac.ma',
    'Université Al Quaraouiyine': 'uaq.ac.ma',
    'Université Cadi Ayyad': 'uca.ac.ma',
    'Université Sidi Mohamed Ben Abdellah': 'usmba.ac.ma',
    'Université Hassan II': 'uh2c.ac.ma',
    'Université Abdelmalek Essaadi': 'uae.ac.ma'
}

def generer_numero_apogee():
    """Générer un numéro Apogée unique"""
    return str(3001000 + random.randint(100000, 999999))

def generer_email(prenom, nom, universite):
    """Générer un email universitaire"""
    prenom_clean = prenom.lower().replace(' ', '').replace('é', 'e').replace('à', 'a')
    nom_clean = nom.lower().replace(' ', '').replace('é', 'e').replace('à', 'a')
    domaine = domaines_email.get(universite, 'universite.ac.ma')
    email = f"{prenom_clean}.{nom_clean}@{domaine}"
    return email

# Générer le CSV
print("=" * 80)
print("GÉNÉRATION DU DATASET: PRÉDICTION DES COMPÉTENCES ACADÉMIQUES")
print("Système Universitaire Marocain - MISE À JOUR")
print("=" * 80)

# Noms des colonnes
colonnes = [
    'Numero_Apogee', 'Prenom', 'Nom', 'Email', 'Genre', 'Age',
    'Region', 'Universite', 'Diplome', 'Specialite', 'Annee_Etude',
    'Note_Bac', 'Moyenne_Semestre_Precedent', 'GPA_Cumule',
    'Nombre_Cours_Suivis', 'Nombre_Absences', 'Taux_Presence_Cours',
    'Nombre_Travaux_Soumis', 'Nombre_Participations_Cours', 'Nombre_Visites_Bibliotheque_Mois',
    'Heures_Etude_Hebdo', 'Acces_Internet', 'Ordinateur_Personnel', 'Acces_Ressources_Numeriques',
    'Connexion_Plateforme_ELearning_Jour', 'Situation_Financiere', 'Emploi_Etudiant', 'Heures_Travail_Semaine',
    'Tutorat_Suivi', 'Consultation_Professeur_Mois', 'Participation_Groupes_Etude',
    'Niveau_Stress', 'Heures_Sommeil_Nuit', 'Activites_Sportives',
    'Parent_Universitaire', 'Fratrie_Etudiant_Universite',
    'Note_Mathematiques', 'Note_Sciences', 'Note_Theorie', 'Note_Pratique_TP', 'Note_Projets',
    'Score_Participation_Classe', 'Score_Qualite_Travaux', 'Score_Comprehension_Concepts',
    'Competence_Communication', 'Competence_Travail_Equipe', 'Competence_Probleme_Resolution', 'Competence_Gestion_Temps',
    'Langue_Principale', 'Niveau_Francais', 'Niveau_Anglais',
    'Motivation_Etudes', 'Interet_Specialite',
    'Niveau_Competence_Academique', 'Score_Competence_Numerique'
]

# Ouvrir le fichier CSV
with open('dataset_competences_academiques_updated.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=colonnes)
    writer.writeheader()
    
    # Générer les données
    for i in range(n_students):
        genre = random.choice(['M', 'F'])
        if genre == 'M':
            prenom = random.choice(prenoms_masculins)
        else:
            prenom = random.choice(prenoms_feminins)
        
        nom = random.choice(noms_marocains)
        universite = random.choice(universites)
        
        # Générer les scores
        gpa = round(random.gauss(11.5, 2.5), 2)
        gpa = max(5, min(20, gpa))  # Limiter entre 5 et 20
        
        note_bac = round(random.gauss(14, 3), 2)
        note_bac = max(8, min(20, note_bac))
        
        taux_presence = round(100 - (random.randint(0, 30) / random.randint(40, 80)) * 100, 2)
        taux_presence = max(50, min(100, taux_presence))
        
        heures_etude = round(random.gauss(15, 7), 2)
        heures_etude = max(1, min(50, heures_etude))
        
        emploi = random.choice([0, 1])
        heures_travail = random.randint(5, 25) if emploi == 1 else 0
        
        # Score de compétence
        competence_score = (
            gpa * 2 +
            taux_presence * 0.05 +
            heures_etude * 0.3 +
            (emploi * -2) +
            random.randint(1, 5) * 1.5 +
            (random.randint(1, 9) * -0.3) +
            random.gauss(0, 3)
        )
        
        competence_score_norm = max(0, min(100, (competence_score + 50)))
        
        if competence_score_norm <= 25:
            niveau_competence = 'Faible'
        elif competence_score_norm <= 50:
            niveau_competence = 'Moyen'
        elif competence_score_norm <= 75:
            niveau_competence = 'Bon'
        else:
            niveau_competence = 'Excellent'
        
        # Écrire la ligne
        row = {
            'Numero_Apogee': generer_numero_apogee(),
            'Prenom': prenom,
            'Nom': nom,
            'Email': generer_email(prenom, nom, universite),
            'Genre': genre,
            'Age': random.randint(18, 30),
            'Region': random.choice(regions),
            'Universite': universite,
            'Diplome': random.choice(diplomes),
            'Specialite': random.choice(specialites),
            'Annee_Etude': random.randint(1, 4),
            'Note_Bac': note_bac,
            'Moyenne_Semestre_Precedent': round(random.gauss(12, 2.5), 2),
            'GPA_Cumule': gpa,
            'Nombre_Cours_Suivis': random.randint(5, 15),
            'Nombre_Absences': random.randint(0, 30),
            'Taux_Presence_Cours': taux_presence,
            'Nombre_Travaux_Soumis': random.randint(1, 15),
            'Nombre_Participations_Cours': random.randint(0, 20),
            'Nombre_Visites_Bibliotheque_Mois': random.randint(0, 30),
            'Heures_Etude_Hebdo': heures_etude,
            'Acces_Internet': random.choice([0, 1]),
            'Ordinateur_Personnel': random.choice([0, 1]),
            'Acces_Ressources_Numeriques': random.choice([0, 1]),
            'Connexion_Plateforme_ELearning_Jour': random.randint(0, 5),
            'Situation_Financiere': random.choice(situations),
            'Emploi_Etudiant': emploi,
            'Heures_Travail_Semaine': heures_travail,
            'Tutorat_Suivi': random.choice([0, 1]),
            'Consultation_Professeur_Mois': random.randint(0, 5),
            'Participation_Groupes_Etude': random.choice([0, 1]),
            'Niveau_Stress': random.randint(1, 9),
            'Heures_Sommeil_Nuit': round(random.gauss(7, 1.5), 2),
            'Activites_Sportives': random.choice([0, 1]),
            'Parent_Universitaire': random.choice([0, 1]),
            'Fratrie_Etudiant_Universite': random.choice([0, 1]),
            'Note_Mathematiques': round(max(5, min(20, random.gauss(12, 3))), 2),
            'Note_Sciences': round(max(5, min(20, random.gauss(12.5, 3))), 2),
            'Note_Theorie': round(max(5, min(20, random.gauss(11.5, 3))), 2),
            'Note_Pratique_TP': round(max(5, min(20, random.gauss(12, 3))), 2),
            'Note_Projets': round(max(5, min(20, random.gauss(12.5, 3))), 2),
            'Score_Participation_Classe': random.randint(1, 5),
            'Score_Qualite_Travaux': random.randint(1, 5),
            'Score_Comprehension_Concepts': random.randint(1, 5),
            'Competence_Communication': random.randint(1, 5),
            'Competence_Travail_Equipe': random.randint(1, 5),
            'Competence_Probleme_Resolution': random.randint(1, 5),
            'Competence_Gestion_Temps': random.randint(1, 5),
            'Langue_Principale': random.choice(langues_principales),
            'Niveau_Francais': random.choice(niveaux_langue),
            'Niveau_Anglais': random.choice(niveaux_langue),
            'Motivation_Etudes': random.randint(1, 9),
            'Interet_Specialite': random.randint(1, 9),
            'Niveau_Competence_Academique': niveau_competence,
            'Score_Competence_Numerique': round(competence_score_norm, 2)
        }
        
        writer.writerow(row)
        
        if (i + 1) % 500 == 0:
            print(f"Progès: {i + 1}/{n_students} étudiants générés...")

print(f"\n✓ Dataset généré avec succès: dataset_competences_academiques_updated.csv")
print(f"  - {n_students} étudiants")
print(f"  - {len(colonnes)} variables")
print(f"  - Spécialités: IA et Digital (remplaçant Littérature et Histoire)")
print(f"  - Colonnes: Numero_Apogee, Prenom, Nom, Email")
