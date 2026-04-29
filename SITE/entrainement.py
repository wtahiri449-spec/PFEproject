
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Chargement des données
# Mettez à jour le chemin du fichier pour qu'il pointe vers l'emplacement réel dans votre Google Drive
df = pd.read_csv('dataset_competences_academiques_updated.csv') # REMPLACER 'MyDrive/' par le chemin de votre dossier si le fichier n'est pas à la racine de MyDrive

# 2. Prétraitement (Preprocessing)
# Suppression des colonnes inutiles pour la prédiction (Données non significatives)
cols_to_drop = ['Numero_Apogee', 'Prenom', 'Nom', 'Email']
df_clean = df.drop(columns=cols_to_drop)

# Encodage des variables catégorielles (Transformer le texte en nombres)
le = LabelEncoder()
categorical_cols = df_clean.select_dtypes(include=['object']).columns

for col in categorical_cols:
    if col != 'Niveau_Competence_Academique': # On garde la cible pour après
        df_clean[col] = le.fit_transform(df_clean[col])

# 3. Séparation des caractéristiques (Features) et de la cible (Target)
X = df_clean.drop(columns=['Niveau_Competence_Academique', 'Score_Competence_Numerique'])
y = df_clean['Niveau_Competence_Academique']

# 4. Division du Dataset (Train 80% / Test 20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisation (Scaling)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Création et Entraînement du Modèle (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Évaluation du Modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Précision du modèle (Accuracy) : {accuracy * 100:.2f}%")
print("\nRapport de Classification :")
print(classification_report(y_test, y_pred))

# 7. Sauvegarde du modèle et du scaler (Sérialisation)
joblib.dump(model, 'model_predictif.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("\nModèle sauvegardé sous 'model_predictif.pkl'")

