# Exercice 03 : Standardization

## Objectif

L'objectif de cet exercice est de standardiser les données issues des fichiers `Train_knight.csv` et `Test_knight.csv` pour faciliter leur utilisation dans des analyses ultérieures. La standardisation permet de normaliser les variables en leur donnant une moyenne de 0 et un écart-type de 1. Cela est particulièrement utile pour les algorithmes qui sont sensibles à l'échelle des données.

## Ce qui a été fait

1. **Chargement des données** :
   - Les données ont été récupérées depuis une base PostgreSQL contenant les tables `train_knight` et `test_knight`.

2. **Préparation des données** :
   - Les colonnes non pertinentes (`id` et `knight`) ont été exclues pour ne pas influencer la standardisation.
   - La colonne cible `knight` a été temporairement isolée pour être réintégrée uniquement lors de la visualisation.

3. **Standardisation** :
   - Les colonnes restantes ont été standardisées à l'aide de `StandardScaler` de la bibliothèque scikit-learn.
   - Chaque colonne a été transformée pour avoir une moyenne de 0 et un écart-type de 1.

4. **Visualisation** :
   - Un des graphiques de l'exercice précédent a été reproduit, mais avec les données standardisées.
   - La séparation des clusters (Jedi et Sith) a été affichée pour le jeu de données `Train_knight`.

## Résultats obtenus

- Les données standardisées facilitent la comparaison des variables sur une même échelle, en éliminant les biais liés à leurs unités respectives.
- Un graphique de dispersion basé sur les colonnes `mass` et `midi_chlorian` a été généré à partir des données standardisées, permettant de visualiser la distinction entre Jedi et Sith.

## Graphique généré

- Le graphique final montre une séparation claire des clusters dans l'espace des données standardisées, tout en mettant en évidence les similarités et les différences entre les classes `knight`.

## Remarques

- La méthode de standardisation utilisée garantit que les résultats sont adaptés à l'analyse multivariée ou à l'application d'algorithmes d'apprentissage automatique.
