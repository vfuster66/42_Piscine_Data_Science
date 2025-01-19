import psycopg2
import pandas as pd
from psycopg2 import Error
from io import StringIO


def create_and_populate_items_table():
    connection = None
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

        # Supprimer la table si elle existe
        drop_table_query = '''
        DROP TABLE IF EXISTS items;
        '''
        cursor.execute(drop_table_query)
        print("Table items supprimée si elle existait")

        # Créer la table avec 3 types de données différents
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS items (
            product_id INTEGER,
            category_id NUMERIC(20),
            category_code TEXT,
            brand VARCHAR(50)
        );
        '''

        cursor.execute(create_table_query)
        print("Table items créée avec succès")

        try:
            # Lire le fichier CSV avec pandas
            df = pd.read_csv('./item/item.csv')

            # Convertir category_id en format numérique approprié
            df['category_id'] = pd.to_numeric(
                df['category_id'], errors='coerce')

            print(f"Nombre de lignes lues depuis le CSV : {len(df)}")

            # Préparer les données pour l'insertion
            output = StringIO()
            df.to_csv(output, sep='\t', header=False, index=False)
            output.seek(0)

            # Copier les données
            cursor.copy_from(
                output,
                'items',
                null='',
                columns=('product_id', 'category_id', 'category_code', 'brand')
            )

            connection.commit()
            print("Données importées avec succès dans la table items")

        except Exception as e:
            print(f"Erreur lors de l'importation des données : {e}")
            connection.rollback()

    except (Exception, Error) as error:
        print(f"Erreur PostgreSQL : {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connexion PostgreSQL fermée")


if __name__ == "__main__":
    create_and_populate_items_table()
