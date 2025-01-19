import psycopg2


def remove_duplicates_with_temp_table():
    """
    Supprime les doublons dans la table 'customers' en utilisant une table
    temporaire.
    """
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
        print("Connecté à PostgreSQL !")
        cursor = conn.cursor()

        # Étape 1 : Créer une table temporaire
        print("Création de la table temporaire...")
        cursor.execute("""
        CREATE TABLE temp_customers AS
        SELECT DISTINCT ON (event_time, event_type, product_id) *
        FROM customers
        ORDER BY event_time;
        """)
        conn.commit()
        print("Table temporaire créée avec succès.")

        # Étape 2 : Vider la table originale
        print("Vidage de la table originale...")
        cursor.execute("TRUNCATE customers;")
        conn.commit()

        # Étape 3 : Réinsérer les données uniques
        print("Réinsertion des données uniques...")
        cursor.execute("""
        INSERT INTO customers
        SELECT * FROM temp_customers;
        """)
        conn.commit()

        # Étape 4 : Supprimer la table temporaire
        print("Suppression de la table temporaire...")
        cursor.execute("DROP TABLE temp_customers;")
        conn.commit()

        print("Tous les doublons ont été supprimés avec succès.")

    except psycopg2.Error as error:
        print(f"Erreur PostgreSQL : {error}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Connexion PostgreSQL fermée.")


if __name__ == "__main__":
    remove_duplicates_with_temp_table()
