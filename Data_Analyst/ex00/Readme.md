# Exercice 00 : American Apple Pie

## Objectif
Le but de cet exercice est de créer un diagramme en camembert (pie chart) pour visualiser la répartition des types d'événements présents dans la table `customers` de votre Data Warehouse. Cela vous aide à mieux comprendre les interactions des utilisateurs sur le site.

## Fonctionnalité
Le script Python **`pie.py`** :
- Se connecte à une base de données PostgreSQL.
- Extrait les types d'événements (`event_type`) et leur fréquence à partir de la table `customers`.
- Crée un diagramme en camembert représentant la répartition des différents événements.
- Enregistre le graphique sous forme de fichier image **`event_distribution_pie_chart.png`**.

## Utilisation

### Prérequis
- Python 3 installé.
- Une base de données PostgreSQL active avec la table `customers` remplie.
- Les bibliothèques Python suivantes installées dans votre environnement virtuel :
  - `psycopg2`
  - `matplotlib`

Vous pouvez installer ces bibliothèques avec la commande suivante :
```bash
pip install psycopg2 matplotlib
```

### Commandes

1. Exécutez le script Python pour générer le diagramme :
```bash
    python pie.py
```

2. Vérifiez le terminal pour les messages de statut :
    - Confirmation de connexion à la base de données.
    - Message indiquant que le graphique a été sauvegardé.
    
3. Ouvrez le fichier event_distribution_pie_chart.png pour visualiser le résultat.

## Détails Techniques
### Étapes suivies par le script :

1. Connexion à la base de données PostgreSQL :
    - Le script utilise psycopg2 pour se connecter à la base de données définie.
    - Il exécute une requête SQL pour récupérer les types d'événements et leur fréquence.

2. Extraction et Transformation des Données :
    - Les résultats de la requête sont utilisés pour construire les étiquettes (labels) et les proportions (sizes) nécessaires pour le graphique.

3. Création du Diagramme en Camembert :
    - Le diagramme est créé avec la bibliothèque matplotlib.
    - Chaque section du camembert représente un type d'événement avec sa proportion.

4. Enregistrement et Affichage :
    - Le graphique est sauvegardé sous forme d'image PNG pour une utilisation ultérieure.
    - Il est également affiché dans une fenêtre interactive.

### Requête SQL utilisée

La requête SQL regroupe les événements et compte leur occurrence :
```sql
SELECT event_type, COUNT(*) AS event_count
FROM customers
GROUP BY event_type
ORDER BY event_count DESC;
```

## Résultats Attendus

- Un graphique en camembert montrant la répartition des types d'événements sur le site.
- Les types d'événements les plus fréquents apparaissent en priorité.