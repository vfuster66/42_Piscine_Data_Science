# Exercice 01 : Heatmap - It is warm

## Objectif de l'exercice

L'objectif de cet exercice est de visualiser les coefficients de corrélation entre les différentes caractéristiques de la table `train_knight` sous forme de Heatmap. Une heatmap permet d'identifier les relations entre les variables et de mieux comprendre les interactions potentielles dans les données.

---

## Ce qui a été fait

1. **Chargement des données** :
   - Connexion à une base de données PostgreSQL pour extraire les données de la table `train_knight`.
   - Suppression des colonnes non numériques ou non pertinentes (`id` et `knight`).

2. **Calcul des corrélations** :
   - Utilisation de la méthode `.corr()` de pandas pour calculer la matrice de corrélation entre les colonnes restantes.

3. **Visualisation avec une Heatmap** :
   - Une Heatmap a été créée à l'aide de la bibliothèque Seaborn.
   - La palette de couleurs utilisée est `rocket`, qui fournit un dégradé moderne et visuellement attrayant.
   - Les coefficients de corrélation sont représentés par des variations de couleur, permettant une analyse rapide et intuitive des relations entre les colonnes.

4. **Résultat final** :
   - La Heatmap montre les coefficients de corrélation sous forme graphique.
   - Une sauvegarde de l'image générée sous le nom `heatmap_correlation_rocket.png`.

---

## Utilité de l'exercice

Cet exercice permet de :
- Identifier les colonnes fortement corrélées (positivement ou négativement) pour une meilleure interprétation des données.
- Détecter les relations entre les variables qui pourraient être exploitées dans des modèles de machine learning.
- Fournir une vue d'ensemble visuelle pour guider les étapes suivantes, telles que la sélection de caractéristiques ou l'analyse de données multivariées.

Une compréhension claire des relations entre les caractéristiques est essentielle pour optimiser les analyses et construire des modèles prédictifs performants.

---

## Résultat attendu

La Heatmap montre des variations de corrélation entre -1 et 1 :
- Une corrélation proche de **1** indique une relation positive forte entre les variables.
- Une corrélation proche de **-1** indique une relation négative forte.
- Une corrélation proche de **0** indique peu ou pas de relation entre les variables.
