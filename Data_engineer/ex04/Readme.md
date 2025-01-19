# Exercise 04 : Items Table

## Objectif
Créer une table "items" basée sur le fichier items.csv en utilisant au moins 3 types de données différents.

## Types de données utilisés

1. `INTEGER` : pour product_id
2. `NUMERIC(20)` : pour category_id (pour gérer les grands nombres)
3. `TEXT` : pour category_code
4. `VARCHAR(50)` : pour brand

## Implémentation

```bash
# S'assurer que les dépendances sont installées
pip install psycopg2-binary pandas

# Exécuter le script Python
python items_table.py
```

## Vérification de l'importation
```sql
-- Se connecter à PostgreSQL
psql -U vfuster -d piscineds -h localhost

-- Voir le nombre total de lignes
SELECT COUNT(*) FROM items;

-- Voir les premières lignes
SELECT * FROM items LIMIT 5;

-- Vérifier la structure
\d items
```

## Résultats attendus

- "Table items supprimée si elle existait"
- "Table items créée avec succès"
- "Nombre de lignes lues depuis le CSV : 109579"
- "Données importées avec succès dans la table items"
- "Connexion PostgreSQL fermée"

## Notes importantes

- Le script supprime la table existante avant de la recréer
- Le script gère correctement les grands nombres dans category_id
- Les données peuvent contenir des valeurs NULL
- L'import utilise le séparateur de tabulation pour éviter les problèmes avec les virgules