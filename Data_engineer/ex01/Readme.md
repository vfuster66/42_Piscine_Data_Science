# Exercise 01 : Show me your DB

## Objectif
Installer et configurer un outil de visualisation graphique pour la base de données PostgreSQL afin de faciliter la manipulation et la visualisation des données.

## Prérequis
- Base de données PostgreSQL configurée (Exercise 00)
- Base de données `piscineds` créée et accessible
- DBeaver Community Edition ou tout autre outil de visualisation de BDD

## Installation de DBeaver

### Sur macOS :
```bash
# Avec Homebrew
brew install --cask dbeaver-community

# OU téléchargement manuel depuis
# https://dbeaver.io/download/
```


## Configuration de la connexion

1. Lancer DBeaver

2. Cliquer sur "New Database Connection" (icône prise + dans la barre d'outils)

3. Sélectionner "PostgreSQL"

4. Remplir les informations suivantes :

- Host: localhost
- Port: 5432
- Database: piscineds
- Username: vfuster
- Password: Bonjour42

5. Cliquer sur "Test Connection" pour vérifier la connexion

6. Sauvegarder la configuration

## Vérifications attendues

- La connexion à la base `piscineds` est opérationnelle
- Navigation dans l'arborescence des tables
- Visualisation de la structure des tables (colonnes, types)
- Exécution de requêtes SQL simples (SELECT)
- Visualisation des données dans un format tabulaire
- Identification des données via leur ID dans les interfaces

## Avantages de DBeaver

- Interface graphique intuitive
- Explorateur de base de données
- Éditeur SQL intégré
- Visualisation des données en temps réel
- Support multi-plateformes
- Gratuit et open source