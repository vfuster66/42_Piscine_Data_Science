import psycopg2
import numpy as np
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

    # --- Première requête : Événements 'purchase' et leurs prix ---
    query1 = """
    SELECT event_type, price
    FROM customers;
    """
    cursor.execute(query1)
    print("First SQL query executed successfully!")
    data1 = cursor.fetchall()

    # Filtrer les prix pour les achats uniquement et convertir en float
    prices = [
        float(price)
        for event_type, price in data1
        if event_type == 'purchase'
    ]

    # Calculer les statistiques
    count = len(prices)
    mean_price = np.mean(prices)
    std_price = np.std(prices)
    min_price = np.min(prices)
    quartiles = np.percentile(prices, [25, 50, 75])
    max_price = np.max(prices)

    # Afficher les statistiques
    print("Statistics for purchases:")
    print(f"Count: {count}")
    print(f"Mean: {mean_price:.6f}")
    print(f"Std Dev: {std_price:.6f}")
    print(f"Min: {min_price:.6f}")
    print(f"25%: {quartiles[0]:.6f}")
    print(f"50% (Median): {quartiles[1]:.6f}")
    print(f"75%: {quartiles[2]:.6f}")
    print(f"Max: {max_price:.6f}")

    # --- Deuxième requête : Moyennes des prix des paniers (26 à 43) ---
    query2 = """
    SELECT user_id, AVG(price) AS avg_cart_price
    FROM customers
    WHERE event_type = 'cart'
    GROUP BY user_id
    HAVING AVG(price) BETWEEN 26 AND 43;
    """
    cursor.execute(query2)
    print("Second SQL query executed successfully!")
    data2 = cursor.fetchall()

    # Convertir les moyennes des prix en float
    avg_cart_prices = [float(row[1]) for row in data2]

    # --- Génération des graphiques ---
    # Graphique 1 : Box plot complet pour les achats
    plt.figure(figsize=(8, 6))
    plt.boxplot(prices, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='lightgray', edgecolor='none'),
                flierprops=dict(
                    marker='D',
                    markersize=8,
                    markerfacecolor='lightgray',
                    markeredgecolor='none'
                ),
                patch_artist=True)
    plt.xlabel("Price")
    plt.title("Full Box Plot (Purchases)")
    plt.savefig("boxplot_purchases_full.png")  # Sauvegarder le graphique
    plt.show()

    # Graphique 2 : Intervalle interquartile (IQR) pour les achats
    plt.figure(figsize=(8, 6))
    boxprops = dict(facecolor='green', edgecolor='black')
    medianprops = dict(linestyle='-', linewidth=2, color='black')
    plt.boxplot(prices, vert=False, widths=0.5, notch=True,
                boxprops=boxprops, medianprops=medianprops, showfliers=False,
                patch_artist=True)
    plt.xlabel("Price")
    plt.title("Interquartile Range (Purchases)")
    plt.savefig("boxplot_purchases_iqr.png")  # Sauvegarder le graphique
    plt.show()

    # Graphique 3 : Box plot des moyennes des prix des paniers
    plt.figure(figsize=(8, 6))
    plt.boxplot(avg_cart_prices, vert=False, widths=0.5, notch=True,
                boxprops=dict(facecolor='lightblue', edgecolor='black'),
                flierprops=dict(
                    marker='D',
                    markersize=8,
                    markerfacecolor='lightgray',
                    markeredgecolor='none'
                ),
                patch_artist=True, whis=0.2)
    plt.xlabel("Average Cart Price")
    plt.title("Box Plot (Cart Average: 26-43)")
    plt.xticks(np.arange(
        int(min(avg_cart_prices)),
        int(max(avg_cart_prices)) + 1,
        step=2
    ))
    plt.xlim(min(avg_cart_prices) - 1, max(avg_cart_prices) + 1)
    plt.savefig("boxplot_cart_avg.png")  # Sauvegarder le graphique
    plt.show()

    # Fermeture de la connexion
    conn.commit()
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
