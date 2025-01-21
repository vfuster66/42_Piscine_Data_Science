from sklearn.preprocessing import StandardScaler
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

    # Charger les données depuis les tables
    query_train = "SELECT * FROM train_knight;"
    query_test = "SELECT * FROM test_knight;"

    df_train = pd.read_sql_query(query_train, conn)
    df_test = pd.read_sql_query(query_test, conn)

    # Exclure la colonne cible 'knight' pour standardisation
    target_train = df_train['knight']
    target_test = df_test.get('knight', None)  # Vérifie si "knight" existe

    features_train = df_train.drop(columns=['id', 'knight'])
    features_test = df_test.drop(columns=['id', 'knight'], errors='ignore')

    # Standardisation des données
    scaler = StandardScaler()
    standardized_train = scaler.fit_transform(features_train)
    standardized_test = scaler.transform(features_test)

    # Créer de nouveaux DataFrames standardisés
    standardized_train_df = pd.DataFrame(
        standardized_train, columns=features_train.columns)
    standardized_test_df = pd.DataFrame(
        standardized_test, columns=features_test.columns)

    # Ajouter la colonne 'knight' pour la visualisation
    standardized_train_df['knight'] = target_train
    if target_test is not None:
        standardized_test_df['knight'] = target_test

    # Graphique basé sur les données standardisées
    x_col = 'mass'
    y_col = 'midi_chlorian'

    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=standardized_train_df,
        x=x_col,
        y=y_col,
        hue='knight',
        palette='coolwarm',
        alpha=0.7
    )
    plt.title('Données standardisées - Train_knight')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()
    plt.savefig("standardized_graph.png")
    plt.show()

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
