import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2

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

    # Calcul des corrélations
    correlation_matrix = df_train.corr()

    # Création de la Heatmap avec la palette "rocket"
    plt.figure(figsize=(12, 10))
    sns.heatmap(
        correlation_matrix,
        annot=False,
        cmap=sns.color_palette("rocket", as_cmap=True),
        linewidths=0.5
    )
    plt.title("Heatmap des coefficients de corrélation")
    plt.tight_layout()

    # Sauvegarde et affichage
    plt.savefig("heatmap_correlation_rocket.png")
    plt.show()

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
