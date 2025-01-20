# Exercice 05 : Clustering

## Objectif
L'objectif de cet exercice est de segmenter les clients en groupes distincts en fonction de leur comportement d'achat. Ces segments permettront d'adapter des campagnes marketing ciblées, telles que :
- Des offres de bienvenue pour les nouveaux clients.
- Des coupons pour ramener les clients inactifs.
- Des statuts fidélité (or, argent, platine) pour les clients réguliers.

## Approche
1. **Préparation des données** : 
   - Extraction des données depuis une base PostgreSQL, incluant :
     - **Recency** : Temps écoulé depuis la dernière commande (en mois).
     - **Frequency** : Nombre total de commandes.
     - **Monetary** : Montant total dépensé.
   - Normalisation des données pour une meilleure application des algorithmes de clustering.

2. **Clustering avec KMeans** :
   - Application de l'algorithme KMeans pour regrouper les clients en 4 segments.
   - Les clusters sont déterminés à partir des variables normalisées.

3. **Visualisation des résultats** :
   - Création de **4 graphiques variés** pour représenter et analyser les clusters.

## Graphiques Utilisés

### 1. **Scatter Plot (Nuage de points)**  
Ce graphique montre la relation entre la récence (`recency`) et la fréquence (`frequency`) des clients, colorée selon leur appartenance à un cluster. Cela permet de visualiser les groupes et leur séparation.

### 2. **Heatmap (Carte thermique)**  
Une carte thermique affiche les moyennes des caractéristiques (`recency`, `frequency`, `monetary`) pour chaque cluster. Elle aide à interpréter les comportements typiques de chaque groupe.

### 3. **Pair Plot (Matrice de relations)**  
Ce graphique met en évidence les relations entre toutes les variables disponibles (`recency`, `frequency`, `monetary`) pour chaque cluster. Il est utile pour identifier les tendances globales et explorer les données en profondeur.

### 4. **Pie Chart (Diagramme circulaire)**  
Ce diagramme représente la distribution proportionnelle des clients dans chaque cluster. Il fournit un aperçu clair du poids relatif de chaque segment.

## Résultats
- Chaque graphique apporte une perspective unique sur les groupes de clients :
  - **Scatter Plot** : Visualisation claire des clusters dans un espace 2D.
  - **Heatmap** : Analyse des moyennes pour comprendre les comportements typiques des clusters.
  - **Pair Plot** : Exploration des relations multidimensionnelles entre les caractéristiques.
  - **Pie Chart** : Distribution proportionnelle des groupes.
