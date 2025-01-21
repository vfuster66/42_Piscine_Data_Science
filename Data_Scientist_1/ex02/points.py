import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Encoder la colonne "knight" (Sith = 0, Jedi = 1) si elle existe
    if 'knight' in df_train.columns:
        df_train['knight'] = df_train['knight'].map({'Sith': 0, 'Jedi': 1})
    else:
        print("La colonne 'knight' est absente dans train_knight.")

    # Ajouter des clusters fictifs pour test_knight (si besoin)
    if 'knight' not in df_test.columns:
        df_test['knight'] = (df_test.index % 2)  # Clusters fictifs

    # Colonnes à utiliser pour les graphiques
    x_col = 'mass'
    y_col = 'midi_chlorian'

    # Créer une figure 2x2 pour afficher les 4 graphiques
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle(
        "Graphiques des clusters pour Train_knight et Test_knight",
        fontsize=16
    )

    # Graphique 1 : Train_knight avec clusters séparés
    sns.scatterplot(
        data=df_train, x=x_col, y=y_col, hue='knight',
        palette='coolwarm', alpha=0.7, ax=axes[0, 0]
    )
    axes[0, 0].set_title("Train_knight - Clusters séparés")
    axes[0, 0].set_xlabel(x_col)
    axes[0, 0].set_ylabel(y_col)

    # Graphique 2 : Train_knight avec clusters mélangés
    sns.scatterplot(
        data=df_train, x=x_col, y=y_col, color='green',
        alpha=0.7, ax=axes[0, 1]
    )
    axes[0, 1].set_title("Train_knight - Clusters mélangés")
    axes[0, 1].set_xlabel(x_col)
    axes[0, 1].set_ylabel(y_col)

    # Graphique 3 : Test_knight avec clusters séparés
    sns.scatterplot(
        data=df_test, x=x_col, y=y_col, hue='knight',
        palette='coolwarm', alpha=0.7, ax=axes[1, 0]
    )
    axes[1, 0].set_title("Test_knight - Clusters séparés")
    axes[1, 0].set_xlabel(x_col)
    axes[1, 0].set_ylabel(y_col)

    # Graphique 4 : Test_knight avec clusters mélangés
    sns.scatterplot(
        data=df_test, x=x_col, y=y_col, color='purple',
        alpha=0.7, ax=axes[1, 1]
    )
    axes[1, 1].set_title("Test_knight - Clusters mélangés")
    axes[1, 1].set_xlabel(x_col)
    axes[1, 1].set_ylabel(y_col)

    # Ajuster les espacements et enregistrer
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig("combined_graphs.png")
    plt.show()

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
