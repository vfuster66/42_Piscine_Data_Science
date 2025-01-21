import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import f1_score, classification_report
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Vérification des arguments
if len(sys.argv) < 3:
    print("Usage: python democracy.py Train_knight.csv Test_knight.csv")
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
    print("Erreur : La colonne 'knight' est absente du fichier "
          "d'entraînement.")
    sys.exit(1)

# Vérifier que les colonnes de test correspondent à celles
# d'entraînement (sans 'knight')
expected_columns = set(train_data.columns) - {'knight'}
if set(test_data.columns) != expected_columns:
    print("Erreur : Les colonnes du fichier de test ne correspondent pas "
          "à celles du fichier d'entraînement.")
    sys.exit(1)

# Séparer les caractéristiques et les étiquettes dans l'ensemble d'entraînement
X = train_data.drop(columns=['knight'])
y = train_data['knight']

# Diviser en ensemble d'entraînement et de validation
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normaliser les données
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(test_data)

# Initialiser les modèles individuels
knn_model = KNeighborsClassifier(n_neighbors=5)
dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
lr_model = LogisticRegression(max_iter=200, random_state=42)

# Créer le Voting Classifier
voting_clf = VotingClassifier(
    estimators=[
        ('knn', knn_model),
        ('decision_tree', dt_model),
        ('logistic_regression', lr_model)
    ],
    voting='hard'
)

# Entraîner le Voting Classifier
voting_clf.fit(X_train, y_train)

# Prédictions sur l'ensemble de validation
y_val_pred = voting_clf.predict(X_val)

# Évaluer les performances
f1 = f1_score(y_val, y_val_pred, pos_label="Jedi")
print(f"F1-score sur l'ensemble de validation : {f1:.2f}")
print("Rapport de classification :")
print(classification_report(y_val, y_val_pred))

# Vérifier si le f1-score est suffisant
if f1 < 0.94:
    print("Attention : le F1-score est inférieur à 94%. "
          "Ajustez vos modèles ou vos données.")

# Prédictions sur l'ensemble de test
y_test_pred = voting_clf.predict(X_test)

# Sauvegarder les prédictions dans un fichier
output_file = "Voting.txt"
try:
    with open(output_file, "w") as f:
        for pred in y_test_pred:
            f.write(pred + "\n")
    print(f"Prédictions sauvegardées dans {output_file}")
except Exception as e:
    print(f"Erreur lors de la sauvegarde des prédictions : {e}")

# Entraîner les modèles individuels pour la comparaison
knn_model.fit(X_train, y_train)
dt_model.fit(X_train, y_train)
lr_model.fit(X_train, y_train)

# Comparaison des performances des modèles
models = ['Decision Tree', 'KNN', 'Logistic Regression', 'Voting Classifier']
f1_scores = [
    f1_score(y_val, dt_model.predict(X_val), pos_label="Jedi"),
    f1_score(y_val, knn_model.predict(X_val), pos_label="Jedi"),
    f1_score(y_val, lr_model.predict(X_val), pos_label="Jedi"),
    f1_score(y_val, voting_clf.predict(X_val), pos_label="Jedi")
]

# Visualisation des résultats
plt.figure(figsize=(8, 6))
plt.bar(models, f1_scores, color=['blue', 'green', 'orange', 'red'])
plt.ylim(0.8, 1.0)
plt.ylabel("F1-Score")
plt.title("Comparaison des F1-Scores des modèles")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("voting_classifier_comparison.png")
plt.show()
