# Exercise 02 : First Table

## Objectif
Créer une table PostgreSQL à partir des données d'un fichier CSV du dossier 'customer' et y importer les données.

## Fichiers
- `table.py` : Script Python pour créer la table
- `table.sql` : Script SQL définissant la structure de la table

## Prérequis
- PostgreSQL installé et configuré (Exercise 00)
- Python 3.x
- Module psycopg2 pour Python
- Base de données piscineds créée et accessible

## Structure de la table
La table est créée avec les colonnes suivantes :

- `event_time` (TIMESTAMP WITH TIME ZONE) : Date et heure de l'événement avec fuseau horaire
- `event_type` (VARCHAR(50)) : Type de l'événement
- `product_id` (INTEGER) : Identifiant du produit
- `price` (DECIMAL(10,2)) : Prix avec 2 décimales
- `user_id` (BIGINT) : Identifiant de l'utilisateur
- `user_session` (UUID) : Identifiant unique de session

## Utilisation

```
python3 table.py
```

Le script Python :

1. Se connecte à la base de données PostgreSQL
2. Crée la table si elle n'existe pas
3. Affiche un message de confirmation
4. Ferme la connexion

## Vérification
1. Connexion à la base de données :
```
psql -U vfuster -d piscineds -h localhost -W
```

2. Vérifier que la table est créée :
```
\dt
```
Vous devriez voir data_2022_oct dans la liste des tables.

3. Examiner la structure de la table :
```
\d data_2022_oct
```

4. Vérifier les données importées :
```
-- Compter le nombre total de lignes
SELECT COUNT(*) FROM data_2022_oct;

-- Voir les 5 premières lignes
SELECT * FROM data_2022_oct LIMIT 5;
```

