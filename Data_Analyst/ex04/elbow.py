import psycopg2
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Informations de connexion à PostgreSQL
dbname = "piscineds"
user = "vfuster"
password = "Bonjour42"
host = "localhost"
port = "5432"

try:
    # Connexion à PostgreSQL
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to PostgreSQL!")
    cursor = conn.cursor()

    # Requête SQL : Dépenses totales et fréquence des achats par client
    query = """
    SELECT user_id, COUNT(*) AS frequency, SUM(price) AS total_spent
    FROM customers
    WHERE event_type = 'purchase'
    GROUP BY user_id;
    """
    cursor.execute(query)
    print("Query executed successfully!")
    data = cursor.fetchall()

    # Fermeture de la connexion
    conn.commit()
    cursor.close()
    conn.close()

    # Création du DataFrame
    df = pd.DataFrame(data, columns=['user_id', 'frequency', 'total_spent'])

    # Normalisation des données
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['frequency', 'total_spent']])

    # Calcul de WCSS pour différents nombres de clusters
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(df_scaled)
        wcss.append(kmeans.inertia_)

    # Tracer le graphique Elbow
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss, marker='o', linestyle='-', color='blue')
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')

    # Configurer les ticks
    plt.xticks([x for x in range(1, 11) if x % 2 == 0])
    plt.ylim(0, max(wcss) + 50000)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Sauvegarder et afficher le graphique
    plt.savefig("elbow_method_updated.png")
    plt.show()

except Exception as e:
    print(f"Error: {e}")
