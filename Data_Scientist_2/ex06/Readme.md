# Democracy! - Voting Classifier

## Objectif de l'exercice

L'objectif principal de cet exercice est de créer un **Voting Classifier** en combinant trois modèles de machine learning : un **arbre de décision**, un **KNN (K-Nearest Neighbors)**, et un troisième modèle de notre choix (dans ce cas, une **régression logistique**). Le modèle final utilise un système de vote majoritaire pour effectuer des prédictions.

Le but est d'obtenir un modèle robuste, performant et capable d'atteindre un **F1-score minimum de 94%** sur l'ensemble de validation.

## Ce qui a été fait

1. **Chargement des données** :
   - Les fichiers `Train_knight.csv` et `Test_knight.csv` ont été chargés.
   - Les colonnes ont été vérifiées pour s'assurer de la correspondance entre l'entraînement et le test.

2. **Préparation des données** :
   - Séparation des données en ensembles de caractéristiques (`X`) et étiquettes (`y`).
   - Division de l'ensemble d'entraînement en sous-ensembles **entraînement** et **validation**.
   - Standardisation des données pour assurer une mise à l'échelle cohérente entre les caractéristiques.

3. **Création des modèles individuels** :
   - Un **arbre de décision**.
   - Un **KNN (K-Nearest Neighbors)**.
   - Une **régression logistique**.

4. **Construction du Voting Classifier** :
   - Les prédictions des trois modèles ont été combinées via un **système de vote majoritaire**.

5. **Évaluation du modèle** :
   - Le modèle a été testé sur l'ensemble de validation, et les métriques suivantes ont été calculées :
     - **F1-score**
     - **Précision**
     - **Rappel**
   - Le modèle a obtenu un **F1-score de 98%** sur l'ensemble de validation, dépassant ainsi l'objectif fixé de 94%.

6. **Prédictions finales** :
   - Le modèle a été utilisé pour prédire les étiquettes du fichier de test `Test_knight.csv`.
   - Les prédictions ont été sauvegardées dans le fichier `Voting.txt`.

## Résultats obtenus

### Rapport de classification sur l'ensemble de validation

| Classe | Précision | Rappel | F1-score | Support |
|--------|-----------|--------|----------|---------|
| Jedi   | 1.00      | 0.97   | 0.98     | 33      |
| Sith   | 0.98      | 1.00   | 0.99     | 47      |
| **Moyenne pondérée** | **0.99** | **0.99** | **0.99** | **80** |

### Précision globale :
- **99%**

### Prédictions finales :
Les prédictions pour le fichier de test ont été sauvegardées dans le fichier `Voting.txt`.

## Importance de cet exercice

Le Voting Classifier combine les forces de plusieurs algorithmes pour créer un modèle plus performant et robuste. Ce type de modèle est particulièrement utile lorsque les modèles individuels montrent des faiblesses spécifiques que le vote peut compenser.

Voici pourquoi cet exercice est important :
- **Robustesse** : En combinant plusieurs modèles, on obtient un meilleur équilibre entre biais et variance.
- **Performance** : Les votes majoritaires permettent de corriger les erreurs des modèles individuels.
- **Généralisabilité** : Le modèle final est souvent plus performant sur des données inédites.

## Conclusion

Le Voting Classifier implémenté dans cet exercice a démontré une excellente capacité de prédiction avec un **F1-score de 98%**, dépassant largement l'objectif fixé de 94%. Ce modèle est un excellent exemple d'ensemble learning, montrant comment combiner plusieurs algorithmes pour obtenir des résultats supérieurs.
