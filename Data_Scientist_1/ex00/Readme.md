# Exercice 00 : Histogram

## Objectif de l'exercice

L'objectif de cet exercice est de visualiser les données contenues dans deux ensembles distincts, `test_knight` et `train_knight`, à l'aide de courbes de densité (KDE - Kernel Density Estimation). Ces visualisations permettent d'analyser et de mieux comprendre les distributions des différentes caractéristiques des données ainsi que leurs interactions.

Les visualisations sont cruciales pour identifier les tendances, les différences et les éventuelles relations entre les classes présentes dans les données.

---

## Travail réalisé

### 1. Visualisation des données de `test_knight`
- Une série de courbes KDE a été créée pour représenter la distribution de chaque compétence des "Knights".
- Ces courbes permettent de comprendre les caractéristiques propres à cet ensemble de données.
- Chaque graphique montre une vue claire de la densité des valeurs pour chaque compétence, facilitant l'identification des tendances.

### 2. Visualisation des données de `train_knight`
- Des courbes KDE ont été générées pour chaque compétence en fonction de la classe (`knight`) : Jedi ou Sith.
- Ces graphiques permettent une comparaison directe entre les deux classes (Jedi et Sith), mettant en évidence les différences ou similitudes dans leurs distributions.
- Une palette de couleurs distincte a été utilisée pour différencier les deux classes, assurant une meilleure lisibilité.

---

## Résultat final

- **Courbes KDE pour `test_knight`** : Une représentation de la densité des compétences pour tous les "Knights" de cet ensemble de données.
- **Courbes KDE pour `train_knight`** : Une comparaison visuelle claire des compétences des Jedi et des Sith, aidant à analyser leurs points communs et leurs divergences.

Ces visualisations fournissent des outils essentiels pour explorer et mieux comprendre les données, tout en facilitant une éventuelle prise de décision basée sur ces analyses.
