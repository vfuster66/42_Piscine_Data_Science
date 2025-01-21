# README

## Objectif de l'exercice

L'objectif principal de cet exercice est d'explorer les relations entre les différentes caractéristiques (features) et la colonne cible `knight`, qui indique le type de chevalier (Sith ou Jedi). L'exercice vise à identifier les caractéristiques les plus corrélées avec la cible et à représenter ces corrélations sous forme graphique pour une meilleure compréhension des données.

## Ce qui a été fait

1. **Chargement des données** :
   - Les données ont été extraites depuis une table PostgreSQL appelée `train_knight`.
   - La colonne `id`, utilisée uniquement comme identifiant, a été exclue des analyses.

2. **Préparation des données** :
   - La colonne `knight` a été encodée en valeurs numériques (`Sith` = 0, `Jedi` = 1) pour permettre le calcul des corrélations.
   - Seules les colonnes numériques ont été prises en compte pour l'analyse.

3. **Calcul des corrélations** :
   - Les coefficients de corrélation ont été calculés pour chaque caractéristique par rapport à la cible `knight`.
   - Les résultats ont été triés pour identifier les caractéristiques les plus influentes.

4. **Représentations graphiques** :
   - Un barplot a été généré pour visualiser les coefficients de corrélation de chaque caractéristique avec la cible.
   - Une heatmap a été produite pour afficher les corrélations entre toutes les colonnes numériques, offrant une vue d'ensemble des relations entre les caractéristiques.

## Pourquoi trouve-t-on des valeurs négatives ?

Les coefficients de corrélation indiquent la force et la direction de la relation entre deux variables :
- **Valeurs positives** : Une corrélation positive signifie que lorsque la valeur d'une caractéristique augmente, la probabilité d'appartenir à un certain type de chevalier (par exemple, Jedi) augmente également.
- **Valeurs négatives** : Une corrélation négative indique que l'augmentation d'une caractéristique diminue la probabilité d'appartenir à un certain type de chevalier. Cela peut refléter des relations inverses ou opposées entre les caractéristiques et la cible.

## Schémas générés

1. **Barplot des corrélations avec `knight`** :
   - Ce graphique montre les coefficients de corrélation pour chaque caractéristique avec la cible `knight`.
   - Il permet d'identifier rapidement les caractéristiques ayant les relations les plus fortes (positives ou négatives) avec la cible.

2. **Heatmap des corrélations** :
   - La heatmap représente les relations entre toutes les colonnes numériques sous forme de matrice colorée.
   - Elle fournit une vue d'ensemble des interactions entre les caractéristiques et permet de repérer les groupes de caractéristiques fortement corrélées.

Ces deux visualisations offrent des perspectives complémentaires sur les données, facilitant l'interprétation des résultats.
