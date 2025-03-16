
# Exercise 00 : Create postgres DB

## Objectif
L'objectif de cet exercice est de créer une base de données PostgreSQL avec des paramètres spécifiques, qui sera utilisée tout au long du module pour stocker et manipuler les données de vente.

## Prérequis
- PostgreSQL 14 ou supérieur installé localement
- PostgreSQL accessible via `localhost` sur le port `5432`
- Accès administrateur à l'utilisateur `postgres`

## Paramètres de la base de données
- Nom de la base de données : `piscineds`
- Nom d'utilisateur : `vfuster`
- Mot de passe : `Bonjour42`

## Configuration initiale

### 1. Se connecter en tant que `postgres` :
```bash
psql -U postgres
```

### 2. Créer l'utilisateur `vfuster` (si besoin) :
```sql
DROP ROLE IF EXISTS vfuster;
CREATE ROLE vfuster WITH LOGIN PASSWORD 'Bonjour42';
ALTER ROLE vfuster CREATEDB;
```

### 3. Supprimer l'ancienne base si elle existe (et forcer la fermeture des connexions) :
```sql
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'piscineds'
AND pid <> pg_backend_pid();

DROP DATABASE IF EXISTS piscineds;
```

### 4. Créer la nouvelle base de données :
```sql
CREATE DATABASE piscineds OWNER vfuster;
```

### 5. Configuration des droits :

#### Se connecter à la base :
```sql
\c piscineds
```

#### Donner tous les droits sur le schéma public :
```sql
GRANT ALL ON SCHEMA public TO vfuster;
```

#### Configurer les droits par défaut :
```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO vfuster;
```

## Vérification

Pour vérifier que la base de données est correctement configurée, exécutez la commande suivante dans un terminal :
```bash
psql -U vfuster -d piscineds -h localhost -W
```

Mot de passe ➔ `Bonjour42`

Le prompt PostgreSQL devrait apparaître ainsi :
```sql
piscineds=#
```

---

## Remarques
La base `piscineds` servira de support tout au long des exercices du module **Data_Engineer** et des modules suivants comme **Data_Warehouse** et **Data_Analyst**.
