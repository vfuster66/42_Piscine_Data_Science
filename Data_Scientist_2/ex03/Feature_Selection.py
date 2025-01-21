import pandas as pd
import psycopg2
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from tabulate import tabulate

# Connexion à PostgreSQL
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

    # Supprimer les colonnes non pertinentes
    df_train = df_train.drop(columns=['id', 'knight'])

    # Standardisation des données
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(df_train)
    df_standardized = pd.DataFrame(standardized_data, columns=df_train.columns)

    # Calcul du VIF
    def calculate_vif(data):
        vif_data = pd.DataFrame()
        vif_data["Feature"] = data.columns
        vif_data["VIF"] = [
            variance_inflation_factor(data.values, i)
            for i in range(data.shape[1])
        ]
        vif_data["Tolerance"] = 1 / vif_data["VIF"]
        return vif_data

    # Initial VIF
    vif_results = calculate_vif(df_standardized)
    initial_vif = vif_results.copy()

    # Afficher le tableau des VIF initiaux
    print("\nInitial VIF Results:")
    print(tabulate(initial_vif, headers='keys', tablefmt='grid'))

    # Réduction des caractéristiques basées sur le VIF
    while vif_results['VIF'].max() > 5:
        feature_to_remove = vif_results.sort_values(
            by="VIF", ascending=False
        ).iloc[0]['Feature']
        print(f"\nRemoving feature: {feature_to_remove} "
              f"with VIF: {vif_results['VIF'].max()}")
        df_standardized = df_standardized.drop(columns=[feature_to_remove])
        vif_results = calculate_vif(df_standardized)

    # Final VIF
    final_vif = vif_results.copy()

    # Afficher le tableau des VIF finaux
    print("\nFinal VIF Results:")
    print(tabulate(final_vif, headers='keys', tablefmt='grid'))

    # Afficher les caractéristiques restantes
    print("\nFeatures retained:")
    print(tabulate(final_vif[['Feature']], headers='keys', tablefmt='grid'))

    # Fermeture de la connexion
    conn.close()

except Exception as e:
    print(f"Error: {e}")
