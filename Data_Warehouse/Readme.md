# Piscine Data Warehouse - README Général

## Objectif
Cette piscine a pour but de vous initier au processus ETL (Extract, Transform, Load) en combinant des données provenant de plusieurs sources dans un entrepôt de données cohérent et structuré. Vous apprendrez à manipuler des bases de données, à nettoyer et transformer des données, et à garantir leur intégrité tout au long du processus.

## Structure du Projet
Le projet est divisé en quatre exercices, chacun abordant une étape clé de la gestion des données dans un entrepôt de données.

### Exercice 00 : **Show me your DB**
**Objectif :** Trouver un outil pour explorer la base de données de manière efficace.
- Vous devez choisir un logiciel (par exemple : pgAdmin, Postico, DBeaver) qui permet de visualiser facilement la base de données.
- Ce logiciel doit permettre de rechercher facilement des informations comme des IDs.

### Exercice 01 : **Customers Table**
**Objectif :** Consolider les données dans une table unique.
- Fusionnez toutes les tables `data_202*_***` dans une table appelée `customers`.
- Vous devrez vous assurer que toutes les données sont intégrées correctement.

### Exercice 02 : **Remove Duplicates**
**Objectif :** Nettoyer la table `customers` en supprimant les doublons.
- Identifiez et supprimez les lignes dupliquées dans la table `customers`.
- Tenez compte des cas où des instructions identiques ont été envoyées avec un intervalle d'une seconde.

### Exercice 03 : **Fusion**
**Objectif :** Enrichir les données existantes.
- Combinez les informations de la table `items` avec la table `customers`.
- Assurez-vous de ne perdre aucune information dans le processus et vérifiez que tous les produits de `items` sont bien intégrés dans `customers`.

## Contraintes Techniques
- **Langage autorisé :** Vous pouvez utiliser toutes les fonctions disponibles pour chaque exercice.
- **Précision :** Le travail doit garantir l’intégrité des données à chaque étape.
- **Performance :** Les scripts doivent être optimisés pour traiter de grandes quantités de données.


