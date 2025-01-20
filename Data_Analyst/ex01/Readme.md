# Exercice 01: Exploration Initiale des Données

## Objectif

L'objectif de cet exercice est de réaliser une exploration initiale des données présentes dans la table `customers`, en se concentrant uniquement sur les événements de type `purchase`. Ces événements correspondent aux achats effectués sur le site. Les données utilisées couvrent la période allant du **1er octobre 2022** au **31 janvier 2023**.

L'exercice consiste à créer trois graphiques :
1. **Les dépenses moyennes par client par jour.**
2. **Le total des ventes par mois.**
3. **Le nombre de clients uniques par jour.**

## Méthodologie

### Étapes
1. **Filtrage des données :**
   - Seuls les événements où `event_type = 'purchase'` sont utilisés.
   - Les données sont limitées à la période entre le **1er octobre 2022** et le **31 janvier 2023**.

2. **Génération des graphiques :**
   - Les données filtrées sont regroupées et analysées pour produire trois visualisations :
     - **Dépenses moyennes par client par jour :**
       - Les dépenses moyennes sont calculées en divisant la somme des prix des achats par le nombre de clients uniques chaque jour.
     - **Total des ventes par mois :**
       - Le total des ventes est calculé par mois en millions d'Altairian Dollars.
     - **Nombre de clients uniques par jour :**
       - Le nombre de clients uniques est calculé pour chaque jour.

3. **Affichage des résultats :**
   - Les graphiques sont générés avec `matplotlib` et enregistrés sous forme d'images.

### Graphiques Générés
1. **Dépenses Moyennes par Client par Jour :**
   - Type de graphique : Courbe de zone.
   - Axe Y : Dépenses moyennes en Altairian Dollars.
   - Axe X : Jours (octobre à janvier).
   - Ajustements : La grille est activée pour plus de lisibilité, et l'axe X est limité à la période analysée.

2. **Total des Ventes par Mois :**
   - Type de graphique : Histogramme.
   - Axe Y : Total des ventes en millions d’Altairian Dollars.
   - Axe X : Mois (octobre à janvier).
   - Ajustements : Les mois sont étiquetés avec des abréviations (Oct, Nov, Dec, Jan), et l'axe Y est limité pour inclure les totaux des ventes.

3. **Nombre de Clients Uniques par Jour :**
   - Type de graphique : Courbe.
   - Axe Y : Nombre de clients uniques.
   - Axe X : Jours (octobre à janvier).
   - Ajustements : Limitation des dates sur l'axe X et ajout d'une grille.

## Prérequis

### Logiciels et Bibliothèques
- **Python 3.x**
- **PostgreSQL**
- Bibliothèques Python nécessaires :
  - `psycopg2` : Pour la connexion à la base de données.
  - `pandas` : Pour la manipulation des données.
  - `matplotlib` : Pour la création des graphiques.

### Configuration
- La table `customers` doit être pré-remplie avec les données filtrées pour la période indiquée.
- Les colonnes nécessaires dans la table `customers` :
  - `event_time` : Date et heure de l'événement.
  - `event_type` : Type d'événement.
  - `price` : Montant de l'achat.
  - `user_id` : Identifiant unique de l'utilisateur.

## Utilisation

1. **Exécuter le script Python :**
```bash
    python chart.py
```

2. Résultats :
    - Les graphiques sont enregistrés sous les noms suivants :
        - average_spend_per_customer.png
        - total_sales_per_month.png
        - unique_customers_per_day.png
    - Les graphiques sont également affichés à l'écran.

## Résultats Attendus

1. Dépenses Moyennes par Client par Jour :
    - La courbe montre les fluctuations des dépenses moyennes par client jour après jour.

2. Total des Ventes par Mois :
    - Un histogramme qui met en évidence les totaux des ventes par mois, avec un pic attendu en novembre.

3. Nombre de Clients Uniques par Jour :
    - Une courbe qui suit les variations du nombre de clients uniques journaliers, reflétant les tendances de fréquentation.

## Remarques

- Les données sont en Altairian Dollars, la devise fictive utilisée pour cet exercice.
- Les graphiques couvrent uniquement la période spécifiée (octobre 2022 à janvier 2023).
- Le script gère les données manquantes ou incorrectes en les filtrant lors du chargement.