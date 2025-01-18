# Piscine Data Science - Module 0 : Création d'une Base de Données

## Description
Ce projet fait partie de la piscine data science et se concentre sur la création et la gestion d'une base de données PostgreSQL. L'objectif est de manipuler des données de ventes sur une période de 4 mois.

## Structure du Projet

### Exercice 00 : Création de la Base de Données PostgreSQL
- Création d'une base de données nommée "piscineds"
- Configuration d'un utilisateur avec le login étudiant
- Mot de passe défini : "Bonjour42"
- Connexion possible via : `psql -U votre_login -d piscineds -h localhost -W`

### Exercice 01 : Visualisation de la Base de Données
- Utilisation de pgAdmin pour visualiser et gérer la base de données
- Interface permettant de :
  - Visualiser la structure des tables
  - Manipuler les données
  - Exécuter des requêtes SQL

### Exercice 02 : Création de la Première Table
- Création de tables basées sur les fichiers CSV du dossier 'customer'
- Structure des tables :
  - event_time (TIMESTAMP)
  - event_type (VARCHAR(50))
  - product_id (INTEGER)
  - price (DECIMAL(10,2))
  - user_id (BIGINT)
  - user_session (UUID)

### Exercice 03 : Tables Automatiques
- Script Python pour automatiser la création des tables
- Traitement automatique des fichiers CSV du dossier 'customer'
- Création des tables :
  - data_2022_oct
  - data_2022_nov
  - data_2022_dec
  - data_2023_jan

### Exercice 04 : Table Items
- Création d'une table "items" basée sur items.csv
- Structure :
  - product_id (INTEGER PRIMARY KEY)
  - category_id (BIGINT)
  - category_code (VARCHAR(100))
  - brand (VARCHAR(100))

## Configuration Technique

### Prérequis
- PostgreSQL installé
- Python 3.x
- Environnement virtuel Python
- pgAdmin installé

### Installation
1. Créer l'environnement virtuel :
```bash
. ./setup.sh
```

### Fichiers Principaux

- ex00/ : Configuration de la base de données - Vide
- ex01/ : Configuration de pgAdmin - Vide
- ex02/ : Scripts de création des tables
- ex03/ : Script Python d'automatisation
- ex04/ : Configuration de la table items