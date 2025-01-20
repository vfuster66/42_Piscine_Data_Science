# Exercice 04 : Elbow Method - Détermination du Nombre Optimal de Clusters

## Objectif de l'exercice

L'objectif de cet exercice est d'identifier le nombre optimal de clusters pour segmenter les clients en groupes distincts. Cette segmentation permettra de cibler chaque groupe avec des offres commerciales personnalisées, envoyées par e-mail. La méthode utilisée pour déterminer ce nombre est la **méthode du coude (Elbow Method)**.

---

## Ce qui a été fait

### 1. Connexion à la base de données
Une connexion à une base PostgreSQL a été établie pour extraire les données des clients. Ces données incluent :
- **Fréquence des achats** (nombre de commandes par client).
- **Dépenses totales** (somme des montants dépensés par chaque client).

Les données ont été agrégées par utilisateur afin de fournir des informations essentielles pour le clustering.

---

### 2. Préparation des données
Les colonnes contenant la fréquence et les dépenses totales ont été :
- **Standardisées** pour éviter que les grandes valeurs (comme les dépenses) dominent les petites (comme la fréquence).
- Préparées sous une forme prête à être utilisées pour l'algorithme de clustering.

---

### 3. Application de la méthode Elbow
La méthode du coude a été appliquée comme suit :
1. Le clustering K-means a été exécuté pour un nombre de clusters variant de 1 à 10.
2. Le **WCSS (Within-Cluster Sum of Squares)** a été calculé pour chaque nombre de clusters.
3. Un graphique a été tracé pour visualiser la relation entre le WCSS et le nombre de clusters.

---

### 4. Interprétation et Résultats
- Le graphique produit (intitulé `The Elbow Method`) montre une décroissance du WCSS à mesure que le nombre de clusters augmente.
- Le "coude" du graphique correspond au point où la diminution du WCSS devient significativement plus lente. Ce point représente le nombre optimal de clusters à utiliser.

---

## Résultat attendu

- Un graphique est généré et sauvegardé sous le nom `elbow_method_updated.png`.
- L'axe des ordonnées (WCSS) monte au-delà de 250,000 pour refléter les grandes variations initiales.
- L'axe des abscisses (nombre de clusters) affiche uniquement les chiffres pairs pour une meilleure lisibilité.

---
