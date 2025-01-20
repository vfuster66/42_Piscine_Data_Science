# Exercice 03 : Analyse des Commandes et Dépenses des Clients

## Objectif de l'exercice

Cet exercice a pour objectif d'explorer les données liées aux commandes et aux dépenses des clients dans une base de données PostgreSQL. L'analyse se concentre sur deux aspects principaux :
1. La **fréquence des commandes** effectuées par chaque client.
2. Les **dépenses totales en Altairian Dollars** réalisées par chaque client.

Ces données sont ensuite visualisées sous forme de graphiques pour offrir une vue synthétique et exploitable des comportements des clients.

---

## Ce qui a été fait

### 1. Connexion à la base de données
Une connexion à une base PostgreSQL a été établie afin d'extraire les données nécessaires pour l'analyse. Deux requêtes SQL ont été exécutées pour récupérer les informations pertinentes.

### 2. Extraction des données
Deux jeux de données ont été extraits :
- **Fréquence des commandes** : Nombre de commandes réalisées par chaque client pour des événements de type "achat".
- **Dépenses totales** : Montant total dépensé par chaque client, avec un filtrage sur les montants inférieurs à 225 Altairian Dollars.

### 3. Visualisation des données
Deux graphiques ont été générés :
1. **Graphique de la fréquence des commandes** :
   - Affiche la répartition du nombre de commandes passées par les clients.
   - Limite les fréquences à un maximum de 40 pour éviter les valeurs aberrantes.
   - Les intervalles de l'axe des abscisses sont réglés sur un pas de 10.

2. **Graphique des dépenses totales en Altairian Dollars** :
   - Affiche la répartition des montants dépensés par les clients.
   - Limite les montants à un maximum de 225 pour une meilleure lisibilité.
   - Les intervalles de l'axe des ordonnées sont réglés avec un pas de 5 000, allant de 0 à 45 000.

### 4. Sauvegarde des résultats
Les graphiques générés sont affichés à l'écran et sauvegardés dans un fichier PNG intitulé `distribution_charts.png` pour une consultation ultérieure.

---

## Résultat attendu

- **Graphique 1 : Fréquence des commandes** :
  - L'axe des abscisses (fréquence) est limité à 40 avec des intervalles de 10.
  - L'axe des ordonnées (nombre de clients) est limité à 70 000, sans afficher la valeur 70 000.

- **Graphique 2 : Dépenses totales** :
  - L'axe des abscisses (valeur en Altairian Dollars) est limité à 225 avec des intervalles de 25.
  - L'axe des ordonnées (nombre de clients) va de 0 à 45 000 avec un pas de 5 000, sans afficher la valeur 45 000.

---

