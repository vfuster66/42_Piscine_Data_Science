# Exercise 03 : Automatic Table Creation

## Objectif
Créer et peupler automatiquement des tables PostgreSQL pour tous les fichiers CSV présents dans le dossier 'customer'.

## Prérequis
- PostgreSQL installé et configuré
- Python 3.x
- Modules Python requis :
    - psycopg2-binary
    - pandas

## Fonctionnement du script
Le script `automatic_table.py` réalise les opérations suivantes :

1. Scan du dossier 'customer' :

    - Détecte automatiquement tous les fichiers .csv
    - Crée un nom de table correspondant au nom du fichier (sans extension)


2. Pour chaque fichier CSV :

    - Vérifie si la table existe déjà et contient des données
    - Si oui : passe au fichier suivant
    - Si non : crée la table et importe les données


3. Structure des tables créées :

```sql
CREATE TABLE IF NOT EXISTS table_name (
    event_time TIMESTAMP WITH TIME ZONE,
    event_type VARCHAR(50),
    product_id INTEGER,
    price DECIMAL(10,2),
    user_id BIGINT,
    user_session UUID
);
```

## Utilisation

1. Placer les fichiers CSV dans le dossier 'customer'

2. Exécuter le script :
```bash
python automatic_table.py
```

2. Vérifier les résultats :
```sql
psql -U vfuster -d piscineds -h localhost

-- Lister toutes les tables créées
\dt

-- Vérifier le contenu d'une table spécifique
SELECT COUNT(*) FROM data_2022_oct;
SELECT * FROM data_2022_oct LIMIT 5;
```

## Messages attendus

- "Traitement de [nom_table]"
- "Table [nom_table] créée avec succès" (pour les nouvelles tables)
- "La table [nom_table] existe déjà et contient des données" (pour les tables existantes)
- "Nombre de lignes lues depuis [fichier]"
- "Données importées avec succès dans [nom_table]"

## Gestion des erreurs

- Vérifie l'existence des tables avant création
- Évite les imports en double
- Gestion des erreurs de connexion à la base de données
- Gestion des erreurs de lecture des fichiers CSV
- Fermeture propre des connexions

## Notes importantes

- Les tables existantes et contenant des données ne sont pas modifiées
- Le script peut être exécuté plusieurs fois en toute sécurité
- Les noms des tables sont dérivés directement des noms des fichiers CSV