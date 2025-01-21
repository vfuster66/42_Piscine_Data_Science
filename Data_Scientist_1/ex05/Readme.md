# README - Split Dataset

## Objectif de l'exercice

L'objectif de cet exercice est de diviser aléatoirement un fichier de données (`Train_knight.csv`) en deux ensembles distincts : 
- **Training_knight.csv** : utilisé pour entraîner un modèle.
- **Validation_knight.csv** : utilisé pour valider le modèle.

Cette division est essentielle pour évaluer les performances d'un modèle tout en évitant les problèmes d'adaptation excessive (overfitting). Elle permet de séparer les étapes d'apprentissage et d'évaluation intermédiaire.

---

## Pourquoi diviser les données ?

### 1. Ensemble d'entraînement
L'ensemble **Training** contient la majorité des données (80%). Il est utilisé pour ajuster les paramètres internes du modèle et lui apprendre les relations entre les caractéristiques (features) et la cible.

### 2. Ensemble de validation
L'ensemble **Validation** contient 20% des données. Il sert à évaluer le modèle pendant son développement, notamment pour ajuster les hyperparamètres. Cela permet d'éviter les problèmes de surapprentissage et d'assurer une meilleure généralisation.

---

## Méthodologie

1. **Fractionnement aléatoire**
   - Les lignes du fichier `Train_knight.csv` sont réparties de manière aléatoire pour éviter les biais.
   - **80%** des données sont attribuées à `Training_knight.csv`.
   - **20%** des données sont attribuées à `Validation_knight.csv`.

2. **Représentativité**
   - Le fractionnement aléatoire garantit que les deux ensembles restent représentatifs de la distribution globale des données.

3. **Fichiers générés**
   - `Training_knight.csv` contient l'ensemble d'entraînement (318 lignes).
   - `Validation_knight.csv` contient l'ensemble de validation (80 lignes).

---

## Importance dans un projet de Data Science

1. **Éviter les biais** :  
   La division aléatoire permet de garantir que les ensembles sont issus de la même distribution, ce qui est crucial pour évaluer les performances du modèle.

2. **Évaluation des performances** :  
   L'ensemble de validation est indispensable pour mesurer les performances intermédiaires du modèle et éviter le surapprentissage.

3. **Pipeline typique de Data Science** :  
   Cette étape s'intègre dans un workflow standard où les données sont :
   - Nettoyées et prétraitées.
   - Divisées en ensembles d'entraînement, de validation, et éventuellement de test.
   - Utilisées pour ajuster et évaluer le modèle.

---

## Conclusion

Le fractionnement des données est une étape cruciale pour garantir que le modèle peut être généralisé à de nouvelles données. Dans cet exercice, les fichiers générés (`Training_knight.csv` et `Validation_knight.csv`) permettent de séparer efficacement l'apprentissage et la validation. Cela constitue une base solide pour les étapes suivantes du développement du modèle.
