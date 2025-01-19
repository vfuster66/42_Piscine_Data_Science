import os
import psycopg2
import pandas as pd
from psycopg2 import Error
from io import StringIO


def get_csv_files(directory):
    """Récupère tous les fichiers CSV du dossier 'customer'"""
    csv_files = []
    try:
        for file in os.listdir(directory):
            if file.endswith('.csv'):
                csv_files.append(os.path.join(directory, file))
        return csv_files
    except Exception as e:
        print(f"Erreur lors de la lecture du dossier : {e}")
        return []


def create_table_name(csv_path):
    """Crée le nom de la table à partir du nom du fichier CSV"""
    base_name = os.path.basename(csv_path)
    return os.path.splitext(base_name)[0]


def table_exists_and_has_data(cursor, table_name):
    """Vérifie si la table existe et contient des données"""
    # Vérifier si la table existe
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = %s
        );
    """, (table_name,))

    if not cursor.fetchone()[0]:
        return False

    # Vérifier si la table contient des données
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    return count > 0


def create_and_populate_tables():
    connection = None
    try:
        connection = psycopg2.connect(
            database="piscineds",
            user="vfuster",
            password="Bonjour42",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()
        csv_files = get_csv_files('./customer')

        for csv_file in csv_files:
            table_name = create_table_name(csv_file)
            print(f"\nTraitement de {table_name}")

            # Vérifier si la table existe et contient des données
            if table_exists_and_has_data(cursor, table_name):
                print(f"La table {table_name} existe déjà et contient des "
                      f"données. Passage à la suivante.")
                continue

            # Création de la table
            create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                event_time TIMESTAMP WITH TIME ZONE,
                event_type VARCHAR(50),
                product_id INTEGER,
                price DECIMAL(10,2),
                user_id BIGINT,
                user_session UUID
            );
            '''
            cursor.execute(create_table_query)
            print(f"Table {table_name} créée avec succès")

            try:
                df = pd.read_csv(csv_file)
                print(f"Nombre de lignes lues depuis {csv_file} : {len(df)}")

                output = StringIO()
                df.to_csv(output, sep='\t', header=False, index=False)
                output.seek(0)

                cursor.copy_from(
                    output,
                    table_name,
                    null='',
                    columns=df.columns
                )

                connection.commit()
                print(f"Données importées avec succès dans {table_name}")

            except Exception as e:
                print(f"Erreur lors de l'importation des données pour "
                      f"{table_name}: {e}")
                connection.rollback()

    except (Exception, Error) as error:
        print(f"Erreur PostgreSQL : {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("\nConnexion PostgreSQL fermée")


if __name__ == "__main__":
    create_and_populate_tables()
