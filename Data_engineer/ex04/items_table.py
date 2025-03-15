import psycopg2
import pandas as pd
from psycopg2 import Error
from io import StringIO
from printer import Printer

printer = Printer()


def create_and_populate_items_table():
    connection = None
    try:
        # Connexion PostgreSQL
        connection = psycopg2.connect(
            database="piscineds",
            user="vfuster",
            password="Bonjour42",
            host="db"
        )
        cursor = connection.cursor()

        # Suppression de l'ancienne table si existante
        drop_table_query = 'DROP TABLE IF EXISTS items;'
        cursor.execute(drop_table_query)
        printer.info("Table items supprimée si elle existait.")

        # Création de la nouvelle table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS items (
            product_id INTEGER,
            category_id NUMERIC(20),
            category_code TEXT,
            brand VARCHAR(50)
        );
        '''
        cursor.execute(create_table_query)
        printer.success("Table items créée avec succès.")

        # Lecture du CSV avec pandas
        try:
            file_path = './item/item.csv'
            df = pd.read_csv(file_path)

            df['category_id'] = pd.to_numeric(
                df['category_id'], errors='coerce')

            printer.section(
                f"Nombre de lignes lues depuis {file_path} : {len(df)}"
            )

            # Conversion en CSV mémoire pour COPY
            output = StringIO()
            df.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)

            # Import avec COPY
            cursor.copy_from(
                output,
                'items',
                null='',
                columns=('product_id', 'category_id', 'category_code', 'brand')
            )
            connection.commit()

            printer.success(
                "Données importées avec succès dans la table items ✅"
            )

        except Exception as e:
            printer.error(f"Erreur lors de l'importation des données : {e}")
            connection.rollback()

    except (Exception, Error) as error:
        printer.error(f"Erreur PostgreSQL : {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            printer.info("Connexion PostgreSQL fermée.")
