import psycopg2
import matplotlib.pyplot as plt


def generate_pie_chart():
    """
    Génère un diagramme en camembert basé sur les types d'événements
    dans la table 'customers'.
    """
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
        print("Connecté à PostgreSQL !")
        cursor = conn.cursor()

        # Requête pour récupérer les types d'événements et leur fréquence
        cursor.execute("""
        SELECT event_type, COUNT(*) AS event_count
        FROM customers
        GROUP BY event_type
        ORDER BY event_count DESC;
        """)
        results = cursor.fetchall()

        # Préparer les données pour le graphique
        labels = [row[0] for row in results]
        sizes = [row[1] for row in results]

        # Création du diagramme en camembert
        plt.figure(figsize=(10, 7))
        plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=140,
            textprops={'fontsize': 12}
        )
        plt.title(
            "Répartition des types d'événements sur le site", fontsize=16,
            pad=50
        )
        plt.axis('equal')  # Assure que le camembert est bien circulaire

        # Enregistrement et affichage du graphique
        plt.savefig("event_distribution_pie_chart.png")
        print("Diagramme en camembert enregistré sous "
              "'event_distribution_pie_chart.png'.")
        plt.show()

    except psycopg2.Error as error:
        print(f"Erreur PostgreSQL : {error}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Connexion PostgreSQL fermée.")


if __name__ == "__main__":
    generate_pie_chart()
