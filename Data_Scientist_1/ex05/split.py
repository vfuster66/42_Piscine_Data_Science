import pandas as pd
from sklearn.model_selection import train_test_split

# Charger le fichier Train_knight.csv
input_file = "Train_knight.csv"

try:
    # Charger les données
    df = pd.read_csv(input_file)
    print(f"Dataset chargé avec succès : {len(df)} lignes.")

    # Fractionner les données : 80% pour l'entraînement, 20% pour la validation
    train, validation = train_test_split(df, test_size=0.2, random_state=42)

    # Sauvegarder les fichiers résultants
    train.to_csv("Training_knight.csv", index=False)
    validation.to_csv("Validation_knight.csv", index=False)

    print("Fichiers générés avec succès :")
    print(f" - Training_knight.csv : {len(train)} lignes")
    print(f" - Validation_knight.csv : {len(validation)} lignes")

except Exception as e:
    print(f"Erreur : {e}")
