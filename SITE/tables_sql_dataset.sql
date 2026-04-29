-- Table principale des étudiants
CREATE TABLE Etudiants (
    Numero_Apogee VARCHAR(20) PRIMARY KEY,
    Prenom VARCHAR(50),
    Nom VARCHAR(50),
    Email VARCHAR(100),
    Genre CHAR(1),
    Age INT,
    Region VARCHAR(50),
    Universite VARCHAR(100),
    Diplome VARCHAR(20),
    Specialite VARCHAR(30),
    Annee_Etude INT
);

-- Table des performances académiques
CREATE TABLE Performances (
    Numero_Apogee VARCHAR(20),
    Note_Bac FLOAT,
    Moyenne_Semestre_Precedent FLOAT,
    GPA_Cumule FLOAT,
    Note_Mathematiques FLOAT,
    Note_Sciences FLOAT,
    Note_Theorie FLOAT,
    Note_Pratique_TP FLOAT,
    Note_Projets FLOAT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table d'engagement académique
CREATE TABLE Engagements (
    Numero_Apogee VARCHAR(20),
    Nombre_Cours_Suivis INT,
    Nombre_Absences INT,
    Taux_Presence_Cours FLOAT,
    Nombre_Travaux_Soumis INT,
    Nombre_Participations_Cours INT,
    Nombre_Visites_Bibliotheque_Mois INT,
    Heures_Etude_Hebdo FLOAT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table des ressources et accès technologique
CREATE TABLE Ressources_Techno (
    Numero_Apogee VARCHAR(20),
    Acces_Internet BOOLEAN,
    Ordinateur_Personnel BOOLEAN,
    Acces_Ressources_Numeriques BOOLEAN,
    Connexion_Plateforme_ELearning_Jour INT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table socio-économique
CREATE TABLE Socio_Eco (
    Numero_Apogee VARCHAR(20),
    Situation_Financiere VARCHAR(20),
    Emploi_Etudiant BOOLEAN,
    Heures_Travail_Semaine INT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table de support académique
CREATE TABLE Support_Academique (
    Numero_Apogee VARCHAR(20),
    Tutorat_Suivi BOOLEAN,
    Consultation_Professeur_Mois INT,
    Participation_Groupes_Etude BOOLEAN,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table bien-être et santé
CREATE TABLE Bien_Etre (
    Numero_Apogee VARCHAR(20),
    Niveau_Stress INT,
    Heures_Sommeil_Nuit FLOAT,
    Activites_Sportives BOOLEAN,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table antécédents familiaux
CREATE TABLE Famille (
    Numero_Apogee VARCHAR(20),
    Parent_Universitaire BOOLEAN,
    Fratrie_Etudiant_Universite BOOLEAN,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table compétences transversales et feedback
CREATE TABLE Competences (
    Numero_Apogee VARCHAR(20),
    Score_Participation_Classe INT,
    Score_Qualite_Travaux INT,
    Score_Comprehension_Concepts INT,
    Competence_Communication INT,
    Competence_Travail_Equipe INT,
    Competence_Probleme_Resolution INT,
    Competence_Gestion_Temps INT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table linguistique
CREATE TABLE Linguistique (
    Numero_Apogee VARCHAR(20),
    Langue_Principale VARCHAR(20),
    Niveau_Francais VARCHAR(20),
    Niveau_Anglais VARCHAR(20),
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table motivation et objectifs
CREATE TABLE Motivation (
    Numero_Apogee VARCHAR(20),
    Motivation_Etudes INT,
    Interet_Specialite INT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);

-- Table des résultats prédits (cible)
CREATE TABLE Resultats_Prediction (
    Numero_Apogee VARCHAR(20),
    Niveau_Competence_Academique VARCHAR(20),
    Score_Competence_Numerique FLOAT,
    PRIMARY KEY (Numero_Apogee),
    FOREIGN KEY (Numero_Apogee) REFERENCES Etudiants(Numero_Apogee)
);
