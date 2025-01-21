import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Vérification des arguments
if len(sys.argv) < 3:
    print("Usage: python KNN.py Train_knight.csv Test_knight.csv")
    sys.exit(1)

train_file = sys.argv[1]
test_file = sys.argv[2]

# Charger les données
try:
    train_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)
except Exception as e:
    print(f"Erreur lors du chargement des fichiers: {e}")
    sys.exit(1)

# Vérifier la présence de la colonne 'knight'
if 'knight' not in train_data.columns:
    print("Erreur : La colonne 'knight' est absente du fichier d'entraînement."
          )
    sys.exit(1)

# Vérifier que les colonnes de test correspondent à celles d'entraînement
# (sans 'knight')
expected_columns = set(train_data.columns) - {'knight'}
if set(test_data.columns) != expected_columns:
    print("Erreur : Les colonnes du fichier de test ne correspondent pas à "
          "celles du fichier d'entraînement.")
    sys.exit(1)

# Séparer les caractéristiques et les étiquettes dans l'ensemble d'entraînement
X = train_data.drop(columns=['knight'])
y = train_data['knight']

# Diviser en ensemble d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normaliser les données (important pour KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(test_data)

# Optimiser la valeur de k en utilisant l'ensemble de validation
k_values = range(1, 31)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_val_pred = knn.predict(X_val)
    accuracies.append(accuracy_score(y_val, y_val_pred))

# Trouver le k optimal
best_k = k_values[accuracies.index(max(accuracies))]
print(f"Meilleure valeur de k: {best_k}")

# Afficher le graphique des scores
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracies, label="Accuracy", color="blue", marker="o")
plt.xlabel("Valeur de k")
plt.ylabel("Accuracy")
plt.legend()
plt.title("Optimisation de k pour KNN")
plt.grid()
plt.savefig("knn_optimization.png")
plt.show()

# Entraîner le modèle final avec le meilleur k
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_test_pred = knn.predict(X_test)

# Sauvegarder les prédictions dans un fichier
output_file = "KNN.txt"
try:
    with open(output_file, "w") as f:
        for pred in y_test_pred:
            f.write(pred + "\n")
    print(f"Prédictions sauvegardées dans {output_file}")
except Exception as e:
    print(f"Erreur lors de la sauvegarde des prédictions : {e}")
