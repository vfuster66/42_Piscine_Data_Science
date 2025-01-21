import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

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

    # Charger les données depuis les tables
    query_train = "SELECT * FROM train_knight;"
    query_test = "SELECT * FROM test_knight;"
    df_train = pd.read_sql_query(query_train, conn)
    df_test = pd.read_sql_query(query_test, conn)

    # Exclure la colonne "id"
    df_train = df_train.drop(columns=["id"])
    if "id" in df_test.columns:
        df_test = df_test.drop(columns=["id"])

    # Vérifier si "knight" existe dans train_knight
    if "knight" in df_train.columns:
        # Sauvegarder la colonne "knight" et l'exclure temporairement
        train_knight_labels = df_train.pop("knight")
        df_train["knight"] = train_knight_labels.map({"Sith": 0, "Jedi": 1})

    # Normalisation des données avec Min-Max Scaling
    scaler = MinMaxScaler()
    df_train_normalized = pd.DataFrame(
        scaler.fit_transform(df_train.iloc[:, :-1]),
        columns=df_train.columns[:-1]
    )
    df_train_normalized["knight"] = df_train["knight"]

    df_test_normalized = pd.DataFrame(
        scaler.transform(df_test), columns=df_test.columns
    )

    # Colonnes pour les graphiques
    x_col = "sensitivity"
    y_col = "strength"

    # Graphiques pour Train_knight
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.scatterplot(
        data=df_train_normalized,
        x=x_col,
        y=y_col,
        hue="knight",
        palette="coolwarm",
        alpha=0.7
    )
    plt.title("Train_knight Normalized - Clusters séparés")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.subplot(1, 2, 2)
    sns.scatterplot(
        data=df_train_normalized,
        x=x_col,
        y=y_col,
        color="green",
        alpha=0.7
    )
    plt.title("Train_knight Normalized - Clusters mélangés")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.tight_layout()
    plt.savefig("train_knight_normalized_graphs.png")
    plt.show()

    # Graphiques pour Test_knight uniquement si les colonnes nécessaires
    # existent
    if (x_col in df_test_normalized.columns and
            y_col in df_test_normalized.columns):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(
            data=df_test_normalized,
            x=x_col,
            y=y_col,
            color="blue",
            alpha=0.7
        )
        plt.title("Test_knight Normalized - Graphique mélangé")
        plt.xlabel(x_col)
        plt.ylabel(y_col)

        plt.tight_layout()
        plt.savefig("test_knight_normalized_graphs.png")
        plt.show()

    # Afficher les données normalisées
    print("Train_knight Normalized Data:")
    print(df_train_normalized.head())
    print("Test_knight Normalized Data:")
    print(df_test_normalized.head())

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
