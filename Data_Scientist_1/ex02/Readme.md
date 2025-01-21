# Exercice 02 : It’s Raining Cats No Points!

## Objectif de l'exercice

L'objectif de cet exercice est de visualiser les relations entre deux colonnes significatives des jeux de données `Train_knight` et `Test_knight` à travers quatre graphiques spécifiques. Ces graphiques permettent d'analyser visuellement la répartition des données et les clusters existants.

## Description des étapes

1. **Chargement des données :**
   - Les fichiers `Train_knight` et `Test_knight` ont été importés depuis une base de données PostgreSQL.
   - Les données de la colonne `knight` (indiquant Sith ou Jedi) ont été encodées pour faciliter la manipulation et l'affichage.

2. **Création des clusters :**
   - Dans `Train_knight`, les clusters sont basés sur la colonne `knight`, séparant Sith et Jedi.
   - Pour `Test_knight`, où la colonne `knight` n'est pas présente, des clusters fictifs ont été créés pour simuler la répartition.

3. **Sélection des colonnes :**
   - Deux colonnes significatives, `mass` et `midi_chlorian`, ont été choisies pour l'affichage des relations.

4. **Génération des graphiques :**
   - **Graphique 1 :** Données de `Train_knight` avec des clusters visuellement séparés, montrant Sith et Jedi différenciés par des couleurs.
   - **Graphique 2 :** Données de `Train_knight` avec tous les points mélangés, sans distinction de clusters.
   - **Graphique 3 :** Données de `Test_knight` avec des clusters visuellement séparés (basés sur des valeurs fictives si nécessaire).
   - **Graphique 4 :** Données de `Test_knight` avec tous les points mélangés.

5. **Affichage combiné :**
   - Les quatre graphiques ont été affichés dans une grille 2x2 sur une seule page pour faciliter la comparaison.

## Résultat

Les graphiques permettent d'observer visuellement les relations entre les deux colonnes choisies (`mass` et `midi_chlorian`) et les clusters de données :
- Les graphiques avec clusters séparés (1 et 3) mettent en évidence les distinctions entre Sith et Jedi ou des clusters fictifs pour `Test_knight`.
- Les graphiques avec clusters mélangés (2 et 4) montrent la distribution générale des données sans distinction de clusters.

Ces visualisations offrent une meilleure compréhension de la structure et de la distribution des données dans les fichiers `Train_knight` et `Test_knight`.
