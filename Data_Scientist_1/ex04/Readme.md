# Exercice 04 : Normalization

## Objectifs

L'objectif principal de cet exercice est de normaliser les données issues des fichiers `Train_knight.csv` et `Test_knight.csv`. La normalisation consiste à transformer les données afin que toutes les valeurs soient ramenées à une échelle comprise entre 0 et 1. Cela permet d’éliminer les biais dus aux différences d’échelles entre les colonnes. 

Par ailleurs, des graphiques similaires à ceux de l’exercice 02 doivent être générés, mais avec les données normalisées.

---

## Étapes réalisées

1. **Chargement des données** : Les données des fichiers `Train_knight.csv` et `Test_knight.csv` ont été importées depuis la base PostgreSQL.

2. **Préparation des données** :
   - La colonne `id`, qui n'a pas d'importance analytique, a été exclue.
   - La colonne `knight` a été encodée pour représenter les classes Sith et Jedi de manière numérique.

3. **Normalisation** :
   - Les données ont été normalisées en utilisant une méthode de mise à l’échelle Min-Max, ramenant toutes les valeurs à une plage entre 0 et 1.
   - Cette opération a été réalisée séparément pour les données de chaque fichier.

4. **Visualisation des données normalisées** :
   - Deux types de graphiques ont été générés :
     - Un graphique montrant les clusters distincts pour les Jedi et les Sith.
     - Un graphique montrant les données mélangées sans distinction de classe.

---

## Résultats obtenus

1. **Données normalisées** :
   - Toutes les caractéristiques des données ont été mises à l’échelle entre 0 et 1, assurant une comparaison équitable.

2. **Graphiques** :
   - Les graphiques permettent d’observer les relations entre deux caractéristiques sélectionnées dans les données normalisées.
   - Pour `Train_knight.csv`, les graphiques montrent les clusters séparés et mélangés.
   - Pour `Test_knight.csv`, les graphiques montrent les données sans distinction de classe, car ce fichier ne contient pas la colonne indiquant les classes.

---

## Points importants

1. **Importance de la normalisation** :
   - Elle met toutes les caractéristiques sur une échelle commune, évitant que certaines caractéristiques aient plus de poids en raison de leur amplitude.
   - Elle facilite l’analyse comparative et améliore les performances des algorithmes d’apprentissage machine.

2. **Différence entre les fichiers** :
   - `Train_knight.csv` inclut les informations de classe (Jedi ou Sith), ce qui permet de générer des graphiques différenciés par clusters.
   - `Test_knight.csv` ne contient pas cette information, limitant les graphiques à des visualisations sans distinction de classe.

3. **Visualisation** :
   - Les graphiques obtenus montrent l’efficacité de la normalisation et permettent d’observer des patterns entre les caractéristiques.

---

## Conclusion

Cet exercice met en lumière l'importance de la normalisation dans l'analyse de données multi-dimensionnelles. En ramenant toutes les caractéristiques à une échelle commune, il devient plus facile de visualiser et d'interpréter les relations entre les données, tout en minimisant les biais introduits par des écarts d'échelle.
