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
    query_test = "SELECT * FROM test_knight;"
    query_train = "SELECT * FROM train_knight;"

    test_knight = pd.read_sql_query(query_test, conn)
    train_knight = pd.read_sql_query(query_train, conn)

    # KDE 1 : Visualisation des données de Test_knight
    plt.figure(figsize=(20, 20))
    for idx, column in enumerate(test_knight.columns[1:]):
        plt.subplot(6, 6, idx + 1)
        sns.kdeplot(
            test_knight[column], fill=True, color='green', label="Knight"
        )
        plt.title(column)
        plt.legend()
        plt.tight_layout()
    plt.savefig("kde_test_knight.png")
    plt.show()

    # KDE 2 : Visualisation des interactions dans Train_knight
    plt.figure(figsize=(20, 20))
    for idx, column in enumerate(train_knight.columns[1:-1]):
        plt.subplot(6, 6, idx + 1)
        sns.kdeplot(
            data=train_knight,
            x=column,
            hue="knight",
            fill=True,
            palette="coolwarm"
        )
        plt.title(column)
        plt.legend(title="Knight")
        plt.tight_layout()
    plt.savefig("kde_train_knight.png")
    plt.show()

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
