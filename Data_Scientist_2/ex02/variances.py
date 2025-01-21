import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Connexion à la base de données
dbname = "piscineds"
user = "vfuster"
password = "Bonjour42"
host = "localhost"
port = "5432"

try:
    # Connexion PostgreSQL
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to PostgreSQL!")

    # Charger les données depuis la table train_knight
    query_train = "SELECT * FROM train_knight;"
    df_train = pd.read_sql_query(query_train, conn)

    # Supprimer les colonnes non numériques ou non pertinentes
    df_train = df_train.drop(columns=['id', 'knight'])

    # Standardisation des données
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(df_train)

    # Application de PCA
    pca = PCA()
    pca.fit(standardized_data)

    # Variances expliquées (en pourcentage)
    explained_variance_ratio = pca.explained_variance_ratio_ * 100
    cumulative_variance = explained_variance_ratio.cumsum()

    # Déterminer le nombre de composantes nécessaires pour 90% de variance
    num_components = (cumulative_variance < 90).sum() + 1

    print("Variances (Percentage):")
    print(explained_variance_ratio)
    print("\nCumulative Variances (Percentage):")
    print(cumulative_variance)
    print(f"\nNumber of components to reach 90%: {num_components}")

    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(
        range(1, len(cumulative_variance) + 1),
        cumulative_variance,
        marker='o',
        linestyle='-',
        color='b'
    )
    plt.axhline(y=90, color='r', linestyle='--', label='90% Variance')
    plt.axvline(
        x=num_components,
        color='g',
        linestyle='--',
        label=f'{num_components} Components'
    )
    plt.title("Cumulative Variance Explained")
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Variance (%)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("cumulative_variance.png")
    plt.show()

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
