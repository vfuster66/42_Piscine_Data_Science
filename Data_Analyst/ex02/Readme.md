# Exercice 02 : Analyse et Visualisation des Données avec PostgreSQL et Matplotlib

## Objectif de l'exercice

Cet exercice vise à explorer et visualiser des données extraites d'une base PostgreSQL pour analyser les comportements d'achat et les moyennes des prix des paniers. L'objectif est de mettre en œuvre des compétences en manipulation de données, calculs statistiques et création de visualisations graphiques.

---

## Étapes réalisées

### 1. Connexion à la base de données
- **Base de données utilisée :** PostgreSQL.
- Une connexion est établie à la base de données `piscineds` pour exécuter des requêtes SQL et extraire les données nécessaires.
- Les identifiants de connexion sont définis directement dans le script Python.

### 2. Extraction des données
Deux requêtes SQL ont été utilisées :
1. **Requête 1 : Événements d'achat (`purchase`)**
   - Extraction de la liste des prix associés aux événements d'achat dans la table `customers`.
   - Les prix sont filtrés et convertis pour être utilisés dans l'analyse.

2. **Requête 2 : Moyennes des prix des paniers (`cart`)**
   - Calcul des moyennes des prix des paniers pour chaque utilisateur.
   - Filtrage des moyennes pour ne conserver que celles comprises entre 26 et 43.

### 3. Calcul des statistiques descriptives
Pour les prix des événements d'achat, les statistiques suivantes sont calculées :
- **Nombre total d'achats (`count`)**
- **Moyenne des prix (`mean`)**
- **Écart-type des prix (`std`)**
- **Prix minimum (`min`)**
- **Prix maximum (`max`)**
- **Quartiles (`25%`, `50%` - médiane, `75%`)**

### 4. Visualisation des données
Trois graphiques sont créés pour représenter les données :

1. **Box plot complet des prix des achats** :
   - Affiche la distribution complète des prix des articles achetés.
   - Met en évidence les valeurs aberrantes.

2. **Box plot de l'intervalle interquartile (IQR)** :
   - Analyse concentrée sur l'intervalle interquartile (entre le 1er et le 3e quartile).
   - Supprime les valeurs aberrantes pour une meilleure lisibilité.

3. **Box plot des moyennes des prix des paniers filtrés** :
   - Représente la répartition des prix moyens des paniers pour les utilisateurs avec des moyennes comprises entre 26 et 43.

### 5. Sauvegarde des graphiques
Chaque graphique est sauvegardé sous forme de fichier PNG dans le répertoire courant :
- `boxplot_purchases_full.png` : Distribution complète des prix des achats.
- `boxplot_purchases_iqr.png` : Intervalle interquartile des prix des achats.
- `boxplot_cart_avg.png` : Moyennes des prix des paniers.

---

## Résultat attendu

### Statistiques calculées
Les statistiques descriptives pour les prix des achats sont affichées dans le terminal.

### Graphiques générés
Les trois graphiques sont :
1. Un box plot complet des prix des achats.
2. Un box plot mettant en évidence l'intervalle interquartile des prix.
3. Un box plot des moyennes des prix des paniers filtrés.

Les graphiques sont affichés dans des fenêtres interactives et sauvegardés dans des fichiers PNG.

---
