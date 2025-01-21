import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Charger les fichiers CSV
train_file = "Train_knight.csv"  # Remplacez par votre fichier
test_file = "Test_knight.csv"    # Remplacez par votre fichier

# Charger les données
df_train = pd.read_csv(train_file)
df_test = pd.read_csv(test_file)

# Afficher les colonnes disponibles pour debug
print("Colonnes dans Train_knight.csv:", df_train.columns)
print("Colonnes dans Test_knight.csv:", df_test.columns)

# Vérifier et supprimer les colonnes si elles existent
columns_to_drop = [col for col in ['id', 'knight'] if col in df_train.columns]
X_train = df_train.drop(columns=columns_to_drop)
y_train = (df_train['knight'].map({'Jedi': 1, 'Sith': 0})
           if 'knight' in df_train.columns else None)

X_test = df_test.drop(columns=['id']) if 'id' in df_test.columns else df_test

# Vérifier si la cible est présente
if y_train is None:
    raise ValueError(
        "La colonne 'knight' est absente de Train_knight.csv. "
        "Impossible de continuer."
    )

# Créer un modèle de classification
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Évaluer le modèle
y_pred_train = model.predict(X_train)
print(classification_report(
    y_train, y_pred_train, target_names=["Sith", "Jedi"]
))

# Visualiser l'arbre
plt.figure(figsize=(20, 10))
plot_tree(
    model,
    feature_names=X_train.columns,
    class_names=["Sith", "Jedi"],
    filled=True
)
plt.title("Decision Tree trained on all Knights features")
plt.savefig("tree_visualization.png")
plt.show()

# Prédictions sur le fichier Test
y_pred_test = model.predict(X_test)
y_pred_labels = ["Jedi" if pred == 1 else "Sith" for pred in y_pred_test]

# Sauvegarder les prédictions dans Tree.txt
with open("Tree.txt", "w") as f:
    f.write("\n".join(y_pred_labels))

print("Predictions saved to Tree.txt")
