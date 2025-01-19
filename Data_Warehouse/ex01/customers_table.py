import psycopg2
from psycopg2 import sql


def create_customers_table():
    """
    Connecte à la base de données PostgreSQL, crée la table 'customers', insère
    les données provenant des tables existantes et ajoute les données
    depuis un fichier CSV.
    Supprime ensuite les tables source.
    """
    try:
        # Connexion à la base de données
        connection = psycopg2.connect(
            database="piscineds",
            user="vfuster",
            password="Bonjour42",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Supprimer la table 'customers' si elle existe déjà
        cursor.execute("DROP TABLE IF EXISTS customers;")
        print("Table 'customers' supprimée si elle existait.")

        # Créer la table 'customers'
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customers (
            event_time TIMESTAMP,
            event_type VARCHAR(50),
            product_id INTEGER,
            price DECIMAL(10, 2),
            user_id BIGINT,
            user_session UUID
        );
        """
        cursor.execute(create_table_query)
        print("Table 'customers' créée avec succès.")

        # Insérer les données des tables existantes
        insert_data_query = """
        INSERT INTO customers (event_time, event_type, product_id, price,
                               user_id, user_session)
        SELECT event_time, event_type, product_id, price, user_id, user_session
        FROM data_2022_oct
        UNION ALL
        SELECT event_time, event_type, product_id, price, user_id, user_session
        FROM data_2022_nov
        UNION ALL
        SELECT event_time, event_type, product_id, price, user_id, user_session
        FROM data_2022_dec
        UNION ALL
        SELECT event_time, event_type, product_id, price, user_id, user_session
        FROM data_2023_jan;
        """
        cursor.execute(insert_data_query)
        print("Données des tables existantes insérées avec succès.")

        # Charger les données du fichier CSV
        temp_table_query = """
        CREATE TEMP TABLE temp_data_2023_feb (
            event_time TIMESTAMP,
            event_type VARCHAR(50),
            product_id INTEGER,
            price DECIMAL(10, 2),
            user_id BIGINT,
            user_session UUID
        );
        """
        cursor.execute(temp_table_query)
        print("Table temporaire pour 'data_2023_feb.csv' créée.")

        # Chemin du fichier CSV
        csv_file_path = 'data_2023_feb.csv'
        with open(csv_file_path, 'r') as f:
            next(f)  # Sauter l'en-tête
            cursor.copy_expert(
                ("COPY temp_data_2023_feb FROM STDIN WITH CSV DELIMITER ',' "
                 "NULL ''"),
                f
            )
        print("Données du fichier CSV 'data_2023_feb.csv' chargées dans la "
              "table temporaire.")

        # Insérer les données de la table temporaire dans 'customers'
        cursor.execute("""
        INSERT INTO customers (event_time, event_type, product_id, price,
                               user_id, user_session)
        SELECT * FROM temp_data_2023_feb;
        """)
        print("Données du fichier 'data_2023_feb.csv' insérées dans "
              "'customers'.")

        # Supprimer la table temporaire
        cursor.execute("DROP TABLE temp_data_2023_feb;")
        print("Table temporaire supprimée.")

        # Supprimer les tables sources
        tables_to_drop = [
            'data_2022_oct', 'data_2022_nov',
            'data_2022_dec', 'data_2023_jan'
        ]
        for table in tables_to_drop:
            drop_table_query = sql.SQL("DROP TABLE IF EXISTS {};")
            drop_table_query = drop_table_query.format(sql.Identifier(table))
            cursor.execute(drop_table_query)
            print(f"Table '{table}' supprimée.")

        # Valider les changements
        connection.commit()

        # Vérification du nombre total de lignes
        cursor.execute("SELECT COUNT(*) FROM customers;")
        total_rows = cursor.fetchone()[0]
        print(f"Nombre total de lignes dans 'customers' : {total_rows}")

    except psycopg2.Error as error:
        print(f"Erreur PostgreSQL : {error}")
    finally:
        # Fermeture des connexions
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        print("Connexion PostgreSQL fermée.")


if __name__ == "__main__":
    create_customers_table()
