import psycopg2
import pandas as pd
from psycopg2 import Error
from io import StringIO


def create_and_populate_table():
    try:
        # Établir la connexion
        connection = psycopg2.connect(
            database="piscineds",
            user="vfuster",
            password="Bonjour42",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        # Créer la table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS data_2022_nov (
            event_time TIMESTAMP WITH TIME ZONE,
            event_type VARCHAR(50),
            product_id INTEGER,
            price DECIMAL(10,2),
            user_id BIGINT,
            user_session UUID
        );
        '''
        cursor.execute(create_table_query)
        print("Table créée avec succès")

        # Lire le fichier CSV
        try:
            df = pd.read_csv('customer/data_2022_nov.csv')
            print(f"Nombre de lignes lues depuis le CSV : {len(df)}")

            # Préparer les données pour l'insertion
            output = StringIO()
            df.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)

            # Copier les données dans la table
            cursor.copy_from(
                output,
                'data_2022_nov',
                null='',
                columns=df.columns
            )

            connection.commit()
            print("Données importées avec succès")

        except Exception as e:
            print(f"Erreur lors de l'importation des données : {e}")
            connection.rollback()

    except (Exception, Error) as error:
        print("Erreur PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connexion PostgreSQL fermée")


if __name__ == "__main__":
    create_and_populate_table()
