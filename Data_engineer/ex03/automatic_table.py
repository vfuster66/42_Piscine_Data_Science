import os
import psycopg2
from psycopg2 import sql


def connect_to_db():
    conn = psycopg2.connect(
        dbname="piscineds",
        user="vfuster",
        password="Bonjour42",
        host="localhost"
    )
    return conn


def create_table_from_csv(csv_path, conn):
    # Obtenir le nom de la table depuis le nom du fichier (sans .csv)
    table_name = os.path.splitext(os.path.basename(csv_path))[0]

    # Créer la requête SQL pour la création de la table
    columns = [
        "event_time TIMESTAMP",
        "event_type VARCHAR(50)",
        "product_id INTEGER",
        "price DECIMAL(10,2)",
        "user_id BIGINT",
        "user_session UUID"
    ]

    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            {}
        )
    """).format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(map(sql.SQL, columns))
    )

    # Exécuter la requête
    with conn.cursor() as cur:
        cur.execute(create_table_query)

    conn.commit()


def main():
    # Se connecter à la base de données
    conn = connect_to_db()

    # Parcourir le dossier customer
    customer_dir = 'customer'
    for filename in os.listdir(customer_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(customer_dir, filename)
            print(f"Creating table for {filename}...")
            create_table_from_csv(csv_path, conn)

    conn.close()
    print("All tables created successfully!")


if __name__ == "__main__":
    main()
