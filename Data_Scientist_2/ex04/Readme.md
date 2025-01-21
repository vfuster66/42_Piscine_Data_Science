# Exercice 04 : Forest

## Objectif de l'exercice

L'objectif principal de cet exercice est de construire un modèle de classification basé sur un **Decision Tree Classifier** ou un **Random Forest Classifier** pour différencier les individus entre deux classes : **Jedi** et **Sith**. L'exercice vise également à obtenir une **précision minimale de 90% du F1-score** et à visualiser l'arbre de décision généré.

Les étapes clés incluent :
1. Charger les fichiers de données `Train_knight.csv` et `Test_knight.csv`.
2. Construire un modèle d'arbre de décision pour classifier les données.
3. Évaluer les performances du modèle.
4. Générer une visualisation de l'arbre.
5. Sauvegarder les prédictions dans un fichier `Tree.txt`.

---

## Ce qui a été fait

### 1. Chargement des données
- Les fichiers `Train_knight.csv` et `Test_knight.csv` ont été chargés.
- Les colonnes pertinentes ont été utilisées pour l'entraînement (exclusion de l'identifiant si nécessaire).

### 2. Préparation des données
- La colonne `knight` a été transformée en étiquettes numériques (`0` pour Sith et `1` pour Jedi) pour faciliter l'entraînement du modèle.

### 3. Construction du modèle
- Un **Decision Tree Classifier** a été utilisé pour entraîner le modèle sur les données de `Train_knight.csv`.
- Une visualisation de l'arbre a été générée, montrant les décisions prises à chaque nœud en fonction des valeurs des caractéristiques.

### 4. Évaluation du modèle
- Le modèle a été évalué sur le fichier `Test_knight.csv`.
- Les métriques obtenues incluent la précision, le rappel, le F1-score et l'exactitude globale. Voici un résumé des résultats :

  | Classe   | Précision | Rappel | F1-score | Support |
  |----------|-----------|--------|----------|---------|
  | Sith     | 0.99      | 1.00   | 1.00     | 246     |
  | Jedi     | 1.00      | 0.99   | 0.99     | 152     |
  | **Global** | **1.00**  | **0.99** | **0.99**  | 398     |

### 5. Génération des prédictions
- Les prédictions ont été sauvegardées dans le fichier `Tree.txt` avec le format attendu (une prédiction par ligne, soit **Jedi** ou **Sith**).

---

## Résultats obtenus

### Visualisation de l'arbre
Une visualisation claire et lisible de l'arbre a été générée, mettant en évidence :
- Les seuils de décision à chaque nœud.
- Le **Gini index** pour mesurer la pureté des nœuds.
- Le nombre d'échantillons dans chaque feuille.
- La répartition des classes (`value = [Sith, Jedi]`) dans chaque nœud.

![Visualisation de l'arbre](tree_visualization.png)

### Prédictions
Le fichier `Tree.txt` contient les prédictions du modèle sur l'ensemble de test. Les résultats sont conformes aux attentes et respectent la contrainte d'un **F1-score ≥ 90%**.

---

## Importance de cet exercice

Cet exercice illustre l'utilisation pratique des arbres de décision en tant que modèle de classification :
- **Interprétabilité** : L'arbre est facilement visualisable, permettant de comprendre comment les décisions sont prises.
- **Efficacité** : Avec un F1-score de 99%, le modèle montre une performance robuste sur ce jeu de données.
- **Praticité** : En sauvegardant les prédictions dans un fichier, les résultats peuvent être facilement exploités pour d'autres analyses ou validations.
