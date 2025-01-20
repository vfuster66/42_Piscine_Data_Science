import psycopg2
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Requête SQL pour récupérer les données
    query = """
    SELECT user_id,
           DATE_PART('month', AGE(NOW(), MAX(event_time))) AS recency,
           COUNT(*) AS frequency,
           SUM(price) AS monetary
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

    # Création d'un DataFrame
    df = pd.DataFrame(data,
                      columns=['user_id', 'recency', 'frequency', 'monetary'])

    # Nettoyage et conversion des données
    df[['recency', 'frequency', 'monetary']] = df[['recency', 'frequency',
                                                   'monetary']].apply(
        pd.to_numeric, errors='coerce'
    ).fillna(0)

    # Normalisation des données
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[['recency', 'frequency', 'monetary']])

    # Appliquer le clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    df['cluster'] = kmeans.fit_predict(df_scaled)

    # Visualisation 1 : Scatter plot avec les clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=df['recency'], y=df['frequency'],
        hue=df['cluster'], palette='tab10', s=50
    )
    plt.title("Scatter plot: Recency vs Frequency")
    plt.xlabel("Recency (months)")
    plt.ylabel("Frequency (number of purchases)")
    plt.legend(title="Cluster")
    plt.savefig("scatter_clusters.png")
    plt.show()

    # Visualisation 2 : Heatmap des moyennes des clusters
    cluster_means = df.groupby('cluster')[
        ['recency', 'frequency', 'monetary']
    ].mean()
    plt.figure(figsize=(10, 6))
    sns.heatmap(cluster_means,
                annot=True,
                fmt=".2f",
                cmap="YlGnBu",
                linewidths=.5)
    plt.title("Heatmap of Average Characteristics per Cluster")
    plt.xlabel("Features")
    plt.ylabel("Cluster")
    plt.savefig("heatmap_clusters.png")
    plt.show()

    # Visualisation 3 : Pair plot pour explorer les relations
    # entre les variables
    sns.pairplot(
        df[['recency', 'frequency', 'monetary', 'cluster']],
        hue='cluster',
        palette='Set2'
    )
    plt.suptitle("Pairplot of Clusters", y=1.02)
    plt.savefig("pairplot_clusters.png")
    plt.show()

    # Visualisation 4 : Pie chart de la distribution des clusters
    cluster_counts = df['cluster'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(cluster_counts,
            labels=[f"Cluster {i}" for i in cluster_counts.index],
            autopct='%1.1f%%',
            startangle=90,
            colors=sns.color_palette('pastel'))
    plt.title("Cluster Distribution")
    plt.savefig("pie_clusters.png")
    plt.show()

except Exception as e:
    print(f"Error: {e}")
