# Exercice 01 : Customers Table

## Objectif
L'objectif de cet exercice est de fusionner plusieurs tables de données existantes dans une table unique nommée `customers`. Cette table consolidée permettra de simplifier les manipulations et analyses futures.

## Prérequis
- Une base de données PostgreSQL configurée (voir Exercice 00).
- Les tables à fusionner doivent être présentes dans la base de données.
- Un fichier `data_2023_feb.csv` doit être disponible dans le répertoire de travail.

## Implémentation

Lancer le script
```python
python customers_table.py
```

Résultat attendu :
- Table 'customers' supprimée si elle existait.
- Table 'customers' créée avec succès.
- Données des tables existantes insérées avec succès.
- Table temporaire pour 'data_2023_feb.csv' créée.
- Données du fichier CSV 'data_2023_feb.csv' chargées dans la table temporaire.
- Données du fichier 'data_2023_feb.csv' insérées dans 'customers'.
- Table temporaire supprimée.
- Nombre total de lignes dans 'customers' : 20692840
- Connexion PostgreSQL fermée.

## Résultats attendus
- Une table `customers` consolidée contenant les données des tables et du fichier CSV.
- Les anciennes tables sources supprimées.
- Une table propre et centralisée pour les analyses futures.
