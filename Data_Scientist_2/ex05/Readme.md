# K-Nearest Neighbors (KNN) - Optimisation et Prédictions

## Objectif de l'exercice

L'objectif principal de cet exercice est d'implémenter un modèle de **K-Nearest Neighbors (KNN)** pour classer les données entre deux classes (`Jedi` et `Sith`). Cet exercice vise à :
1. Identifier la meilleure valeur de `k` pour le modèle KNN en mesurant l'**accuracy** sur un ensemble de validation.
2. Entraîner un modèle KNN final avec la meilleure valeur de `k` trouvée.
3. Effectuer des prédictions sur un ensemble de test (`Test_knight.csv`) et les sauvegarder dans un fichier.

## Ce qui a été fait

### Étapes principales :

1. **Chargement des données** :
   - Lecture des fichiers `Train_knight.csv` et `Test_knight.csv`.
   - Vérification de la présence et de la cohérence des colonnes entre les ensembles d'entraînement et de test.

2. **Préparation des données** :
   - Séparation des caractéristiques (`X`) et de la variable cible (`y`) dans les données d'entraînement.
   - Division des données d'entraînement en deux ensembles : **entraînement** et **validation** (80% - 20%).
   - Normalisation des données pour assurer une performance optimale du modèle KNN.

3. **Optimisation de la valeur de `k`** :
   - Test de différentes valeurs de `k` (de 1 à 30).
   - Calcul de l'**accuracy** pour chaque valeur de `k` en utilisant l'ensemble de validation.
   - Identification de la meilleure valeur de `k` en maximisant l'accuracy.

4. **Entraînement final** :
   - Entraînement du modèle KNN avec la meilleure valeur de `k` sur l'ensemble d'entraînement.

5. **Prédictions sur l'ensemble de test** :
   - Prédiction des classes (`Jedi` ou `Sith`) pour les données de test.
   - Sauvegarde des prédictions dans un fichier texte nommé `KNN.txt`.

6. **Visualisation des résultats** :
   - Génération d'un graphique montrant l'évolution de l'accuracy en fonction de la valeur de `k`.
   - Le graphique est sauvegardé dans un fichier `knn_optimization.png`.

## Résultats obtenus

- **Meilleure valeur de `k`** : La valeur optimale de `k` est déterminée en fonction de l'accuracy maximale sur l'ensemble de validation.
- **Accuracy obtenue** : Le modèle atteint une accuracy minimale de 92% sur l'ensemble de validation.
- **Fichier de prédictions** : Les prédictions sont sauvegardées dans `KNN.txt`.
- **Graphique généré** : Le fichier `knn_optimization.png` montre l'accuracy pour chaque valeur de `k`.

## Fichiers générés

1. **`KNN.txt`** :
   - Contient les prédictions pour les données de test, une classe par ligne (`Jedi` ou `Sith`).

2. **`knn_optimization.png`** :
   - Affiche un graphique de l'accuracy en fonction de la valeur de `k`.

## Usage

Pour exécuter le programme, utilisez la commande suivante :
```bash
python KNN.py Train_knight.csv Test_knight.csv
```
