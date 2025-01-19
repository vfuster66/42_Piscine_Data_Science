# Exercise 00 : Create postgres DB

## Objectif
L'objectif de cet exercice est de créer une base de données PostgreSQL avec des paramètres spécifiques qui sera utilisée tout au long du module pour stocker et manipuler les données de vente.

## Configuration requise
- PostgreSQL installé sur la machine
- Accès aux droits administrateur pour la création de la base de données

## Paramètres de la base de données
- Nom de la base de données : `piscineds`
- Nom d'utilisateur : `vfuster`
- Mot de passe : `Bonjour42`

## Configuration initiale

1. Se connecter en tant que postgres :
```
psql -U postgres
```

2. Créer la base de données et l'utilisateur : 
- Supprimer l'ancienne base si elle existe (et ses connexions)
```
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'piscineds'
AND pid <> pg_backend_pid();

DROP DATABASE IF EXISTS piscineds;
```

- Créer la nouvelle base
```
CREATE DATABASE piscineds;
```

3. Configuration des droits : 
- Donner tous les droits à l'utilisateur
```
GRANT ALL PRIVILEGES ON DATABASE piscineds TO vfuster;
```

- Se connecter à la base piscineds
```
\c piscineds
```

- Donner les droits sur le schema public
```
GRANT ALL ON SCHEMA public TO vfuster;
```

- Configurer les droits par défaut
```
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO vfuster;
```

## Vérification
Pour vérifier que la base de données est correctement configurée, exécutez la commande suivante :
```bash
psql -U vfuster -d piscineds -h localhost -W
```

Si la connexion s'établit après avoir saisi le mot de passe `Bonjour42`, cela signifie que :

La base de données existe
L'utilisateur est correctement configuré
Les permissions sont correctement attribuées

Le prompt PostgreSQL devrait apparaître ainsi :
```
piscineds=#
```
