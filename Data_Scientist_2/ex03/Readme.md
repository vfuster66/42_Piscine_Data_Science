# Feature Selection avec VIF (Variance Inflation Factor)

## Objectif de l'exercice

L'objectif principal de cet exercice est d'identifier et de sélectionner les caractéristiques les plus importantes dans un dataset en réduisant les effets de la multicolinéarité entre les variables. La multicolinéarité peut fausser les résultats des modèles prédictifs et rendre l'interprétation des résultats difficile. Pour ce faire, nous avons utilisé le **Variance Inflation Factor (VIF)**, une méthode statistique qui quantifie combien la variance d'un coefficient de régression est augmentée à cause de la colinéarité.

## Ce qui a été fait

1. **Connexion à PostgreSQL** :
   - Le dataset a été chargé depuis la table `train_knight` de la base de données.

2. **Calcul du VIF initial** :
   - Le VIF a été calculé pour chaque variable. Un VIF élevé (> 5) indique une forte multicolinéarité.

3. **Suppression des variables problématiques** :
   - Les caractéristiques avec un VIF supérieur à 5 ont été supprimées itérativement, en commençant par celle avec le VIF le plus grand. Ce processus a été répété jusqu'à ce que toutes les variables restantes aient un VIF inférieur ou égal à 5.

4. **Affichage des résultats** :
   - Une liste des variables conservées a été affichée, ainsi que leurs VIF finaux, sous forme de tableau pour plus de clarté.

5. **Représentation des résultats** :
   - Un tableau a été utilisé pour présenter les VIF initiaux et finaux des caractéristiques, facilitant l'analyse et l'interprétation des résultats.

## Résultats obtenus

### VIF initial :
Certaines variables, comme `strength`, `recovery`, et `sensitivity`, présentaient des VIF extrêmement élevés, indiquant une forte multicolinéarité.

### VIF final :
Après avoir éliminé les variables problématiques, les caractéristiques suivantes ont été conservées :

- `hability`
- `agility`
- `reactivity`
- `midi_chlorian`
- `push`
- `lightsaber`
- `survival`
- `repulse`
- `friendship`
- `blocking`
- `deflection`
- `mass`
- `burst`

Toutes ces variables ont un **VIF inférieur ou égal à 5**, ce qui garantit que les effets de la multicolinéarité ont été minimisés.

## Importance de cet exercice

La réduction de la multicolinéarité est essentielle dans les modèles linéaires et régressifs, car :
- Elle améliore la stabilité et la fiabilité des coefficients estimés.
- Elle facilite l'interprétation des relations entre les caractéristiques et la variable cible.
- Elle évite les problèmes de sur-ajustement et améliore la généralisation du modèle.

En utilisant le VIF, cet exercice permet de conserver uniquement les caractéristiques les plus pertinentes tout en réduisant l'impact des corrélations excessives entre elles.
