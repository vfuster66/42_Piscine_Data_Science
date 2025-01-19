# Ex03 : Integration des Données

## Objectif

L'objectif de cet exercice est d'intégrer les données de la table items dans la table customers tout en respectant les contraintes suivantes :

- Enrichir les données existantes : Associer les colonnes category_id, category_code et brand de la table items aux lignes correspondantes dans la table customers via la clé commune product_id.
- Ajouter les produits manquants : Insérer dans la table customers toutes les lignes de la table items qui ne contiennent pas encore de product_id correspondant dans customers.
- Éviter les doublons : Assurer l'unicité des données et éviter les lignes redondantes après l'intégration.

## Fonctionnement

### Étape 1 : Ajouter des colonnes dans la table customers

    - Si elles n'existent pas déjà, les colonnes category_id, category_code et brand sont ajoutées dans la table customers pour accueillir les informations provenant de items.

### Étape 2 : Mise à jour des lignes existantes

    - Les lignes dans customers sont enrichies avec les valeurs des colonnes category_id, category_code et brand provenant de la table items via une mise à jour (UPDATE) basée sur le champ commun product_id.

### Étape 3 : Ajout des lignes manquantes

    - Les product_id présents dans items mais absents dans customers sont insérés comme nouvelles lignes dans la table customers avec les informations disponibles (category_id, category_code, et brand).

## Instructions pour exécuter le script
### Pré-requis

- Une base de données PostgreSQL contenant les tables customers et items.
- Les permissions nécessaires pour exécuter des commandes ALTER TABLE, UPDATE, et INSERT.

### Commandes à exécuter

- Placez le script integrate_items_into_customers.py dans votre environnement de travail.

- Assurez-vous que les identifiants de connexion à la base de données (nom de la base, utilisateur, mot de passe, hôte et port) dans le script sont corrects.

- Exécutez le script en utilisant la commande suivante :
```
python integrate_items_into_customers.py
```

### Vérifications après l'exécution

- Vérification du nombre total de lignes :
    - Comparez le nombre total de lignes dans customers avant et après l'intégration.

```
SELECT COUNT(*) AS total_rows FROM customers;
```

- Produits ajoutés :

    - Vérifiez si tous les product_id de la table items ont été ajoutés dans customers :

```
SELECT COUNT(*) AS missing_products
FROM items
WHERE product_id NOT IN (
    SELECT DISTINCT product_id FROM customers
);
```

- Données enrichies :

    - Assurez-vous que toutes les lignes ont été enrichies correctement :

```
    SELECT COUNT(*) AS products_not_enriched
    FROM customers
    WHERE category_id IS NULL
       AND category_code IS NULL
       AND brand IS NULL;
```

## Résultats attendus

- La table customers contient toutes les informations de la table items.
- Tous les produits de items sont présents dans customers.
- Les lignes existantes dans customers sont enrichies avec les données pertinentes de items.

## Notes

- Le script est conçu pour minimiser les opérations inutiles et maximiser la performance sur de grandes tables.
- En cas d'erreur, les connexions sont fermées proprement pour éviter les verrous dans la base de données.