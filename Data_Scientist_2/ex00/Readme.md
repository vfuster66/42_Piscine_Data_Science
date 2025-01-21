# Confusion Matrix - Exercice 00

## Objectif de l'exercice

Cet exercice consiste à implémenter une matrice de confusion pour analyser les performances d'un modèle de classification. La matrice de confusion est un outil essentiel pour évaluer la qualité des prédictions d'un modèle, en comparant les classes prédites avec les classes réelles.

L'exercice a pour but de :
- Comprendre comment calculer une matrice de confusion manuellement.
- Générer des métriques d'évaluation à partir de cette matrice, notamment la précision, le rappel, le F1-score et l'exactitude.
- Afficher les résultats sous forme d'une matrice graphique, facilitant l'interprétation.

**Important** : Cette matrice de confusion sera réutilisée dans les exercices suivants. Il est crucial de maîtriser son calcul et son interprétation.

## Démarche suivie

1. **Lecture des fichiers d'entrée** : Les fichiers `truth.txt` et `predictions.txt` contiennent respectivement les labels réels et les prédictions du modèle. Ils sont lus ligne par ligne pour être comparés.
2. **Calcul de la matrice de confusion** : Chaque combinaison de classe réelle et prédite est comptabilisée dans une matrice carrée, où chaque cellule représente une catégorie spécifique (par exemple, `True Positive`, `False Positive`, etc.).
3. **Calcul des métriques** :
   - **Précision** : Proportion de prédictions correctes parmi les exemples classés positivement par le modèle.
   - **Rappel** : Proportion des exemples positifs correctement identifiés par le modèle.
   - **F1-score** : Moyenne harmonique entre précision et rappel, utile pour des classes déséquilibrées.
   - **Exactitude** : Pourcentage global de prédictions correctes.
4. **Visualisation des résultats** :
   - Affichage de la matrice de confusion sous forme de tableau.
   - Création d'une heatmap colorée pour illustrer graphiquement les résultats.

## Résultat attendu

- Une matrice de confusion avec les valeurs calculées, par exemple :
```
[[25, 24], [30, 21]]
```

- Les métriques associées, par exemple :

```
Jedi : précision = 0.45, rappel = 0.51, F1-score = 0.48 Sith : précision = 0.47, rappel = 0.41, F1-score = 0.44 Exactitude globale = 0.46
```

- Une heatmap graphique montrant visuellement les résultats.

## Importance

La matrice de confusion permet de comprendre où un modèle fait des erreurs et dans quelles classes spécifiques. Elle est essentielle pour diagnostiquer les problèmes d'un modèle de classification et optimiser ses performances.

Cet exercice constitue la base pour les prochaines étapes de ce module et doit être réalisé avec soin.
