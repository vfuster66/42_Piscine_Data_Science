import psycopg2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Connexion à PostgreSQL
dbname = "piscineds"
user = "vfuster"
password = "Bonjour42"
host = "localhost"
port = "5432"

try:
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

    # Exclure explicitement la colonne 'id'
    if 'id' in df_train.columns:
        df_train = df_train.drop(columns=['id'])

    # Encoder la colonne "knight" (Sith = 0, Jedi = 1)
    df_train['knight'] = df_train['knight'].map({'Sith': 0, 'Jedi': 1})

    # Vérifier les colonnes numériques
    numeric_columns = df_train.select_dtypes(
        include=['float64', 'int64']
    ).columns

    # Calcul des corrélations
    correlations = df_train[numeric_columns].corr()

    # Trier les corrélations avec la colonne "knight"
    knight_corr = correlations['knight'].sort_values(ascending=False)
    print("Corrélations avec 'knight':")
    print(knight_corr)

    # Barplot des corrélations avec "knight"
    plt.figure(figsize=(12, 8))
    knight_corr.drop('knight').plot(kind='bar', color='skyblue')
    plt.title("Corrélations des caractéristiques avec 'knight'")
    plt.xlabel("Caractéristiques")
    plt.ylabel("Coefficient de corrélation")
    plt.tight_layout()
    plt.savefig("correlation_barplot.png")
    plt.show()

    # Heatmap des corrélations
    plt.figure(figsize=(16, 12))
    sns.heatmap(
        correlations, annot=False, cmap='coolwarm', fmt='.2f', cbar=True
    )
    plt.title("Heatmap des corrélations")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.show()

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
