# Exercice 02 : Variances

## Objectif de l'exercice

L'objectif de cet exercice est d'analyser les données et de déterminer combien de composantes principales sont nécessaires pour expliquer au moins 90% de la variance totale des données. Cela permet de réduire la dimensionnalité tout en conservant un maximum d'information pertinente.

## Étapes réalisées

1. **Chargement des données**  
   Les données de la table `train_knight` ont été chargées depuis une base de données PostgreSQL.

2. **Prétraitement des données**  
   - Les colonnes non numériques (`id`, `knight`) ont été supprimées.  
   - Une standardisation des données a été effectuée pour centrer et réduire chaque colonne à une moyenne de 0 et un écart-type de 1. Cela garantit que toutes les caractéristiques sont sur la même échelle et évite que certaines dominent en raison de leur amplitude.

3. **Analyse en Composantes Principales (PCA)**  
   Une PCA a été appliquée sur les données standardisées pour :
   - Calculer les variances expliquées par chaque composante.
   - Cumulativement additionner ces variances pour déterminer combien de composantes principales sont nécessaires pour expliquer 90% de la variance totale.

4. **Visualisation des résultats**  
   - Un graphique a été généré pour illustrer la variance cumulée en fonction du nombre de composantes principales. Ce type de graphique est souvent appelé "scree plot".
   - Cela permet de visualiser le point où l'ajout de nouvelles composantes devient moins significatif.

## Résultats obtenus

- La variance expliquée par chaque composante a été calculée.
- La variance cumulée a été additionnée pour chaque composante, et il a été déterminé qu'environ **24 composantes principales** sont nécessaires pour expliquer **90% de la variance totale** des données.

## Visualisation

Un graphique a été généré pour montrer la variance cumulée. Il présente une courbe où chaque point correspond à une composante principale, et la montée progressive indique l'ajout de nouvelles informations. Ce graphique permet d'identifier le point optimal pour la réduction de dimensionnalité.
