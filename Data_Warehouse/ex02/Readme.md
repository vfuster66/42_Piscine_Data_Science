# Ex02 : Remove Duplicates

## Objectif
Le but de ce fichier SQL est de supprimer les doublons dans la table `customers`. Cela garantit que chaque ligne est unique, en éliminant les doublons qui pourraient exister.

## Fonctionnement
Le script suit les étapes suivantes pour supprimer les doublons :

1. **Création d'une table temporaire** :
   - Une table temporaire `temp_customers` est créée pour stocker uniquement les lignes uniques de la table `customers`.
   - Les doublons sont éliminés grâce à la clause `SELECT DISTINCT ON` qui sélectionne la première occurrence pour chaque combinaison unique de `event_time`, `event_type`, et `product_id`.

2. **Vidage de la table originale** :
   - La table `customers` est vidée en utilisant la commande `TRUNCATE`, ce qui supprime toutes les lignes sans journaliser chaque suppression individuellement.

3. **Réinsertion des données uniques** :
   - Les données uniques depuis la table temporaire `temp_customers` sont réinsérées dans la table `customers`.

4. **Suppression de la table temporaire** :
   - La table temporaire `temp_customers` est supprimée après usage.

## Implémentation

Lancer le script
```python
python remove_duplicates.py
```

Résultat attendu :
- Connecté à PostgreSQL !
- Création de la table temporaire...
- Table temporaire créée avec succès.
- Vidage de la table originale...
- Réinsertion des données uniques...
- Suppression de la table temporaire...
- Tous les doublons ont été supprimés avec succès.
- Connexion PostgreSQL fermée.

## Prérequis
- Une base de données PostgreSQL active avec une table `customers` existante.
- L'utilisateur doit avoir les permissions nécessaires pour effectuer les opérations suivantes :
  - Création de tables temporaires.
  - Troncature (`TRUNCATE`).
  - Insertion dans la table `customers`.

## Notes
- **Performance** : Le script est optimisé pour fonctionner rapidement même avec de grandes tables, grâce à l'utilisation de `TRUNCATE` et de `SELECT DISTINCT ON`.
- **Impact sur les données** : Toutes les données de la table `customers` sont supprimées temporairement avant d'être réinsérées. Assurez-vous de disposer d'une sauvegarde si nécessaire.

## Résultats Attendus
- La table `customers` ne contiendra plus de doublons.
- Toutes les lignes dans `customers` seront uniques.
