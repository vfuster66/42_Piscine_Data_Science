import psycopg2
import matplotlib.pyplot as plt

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

    # Requête 1 : Fréquence des commandes par client
    query1 = """
    SELECT user_id, COUNT(*) AS frequency
    FROM customers
    WHERE event_type = 'purchase'
    GROUP BY user_id;
    """
    cursor.execute(query1)
    print("Query 1 executed successfully!")
    data_frequency = cursor.fetchall()

    # Requête 2 : Dépenses totales en Altairian Dollars par client
    query2 = """
    SELECT user_id, SUM(price) AS total_spent
    FROM customers
    WHERE event_type = 'purchase'
    GROUP BY user_id
    HAVING SUM(price) < 225;
    """
    cursor.execute(query2)
    print("Query 2 executed successfully!")
    data_monetary = cursor.fetchall()

    # Fermeture de la connexion
    conn.commit()
    cursor.close()
    conn.close()

    # Extraction des données pour les graphiques
    frequency = [row[1] for row in data_frequency if row[1] <= 40]
    monetary = [row[1] for row in data_monetary]

    # Création des graphiques
    fig, axs = plt.subplots(1, 2, figsize=(15, 6))

    # Graphique 1 : Fréquence des commandes
    axs[0].grid(True, zorder=-1)
    axs[0].hist(frequency, bins=5, edgecolor='k', color='lightblue', alpha=0.8)
    axs[0].set_ylabel('customers')
    axs[0].set_xlabel('frequency')
    axs[0].set_xticks(range(0, 41, 10))
    axs[0].set_ylim(0, 70000)
    axs[0].set_title(
        'Frequency distribution of the number of orders per customer'
    )

    # Graphique 2 : Dépenses totales en Altairian Dollars
    axs[1].grid(True, zorder=-1)
    axs[1].hist(monetary, bins=5, edgecolor='k', color='lightblue', alpha=0.8)
    axs[1].set_ylabel('customers')
    axs[1].set_xlabel('monetary value in A$')
    axs[1].set_title(
        'Frequency distribution of the purchase prices per customer'
    )

    # Personnalisation générale des graphiques
    for ax in axs:
        ax.yaxis.grid(True, linestyle='-', alpha=0.7)
        ax.set_axisbelow(True)

    # Ajustement de l'espacement et affichage des graphiques
    plt.tight_layout()
    plt.savefig("distribution_charts.png")
    plt.show()

except Exception as e:
    print(f"Error: {e}")
