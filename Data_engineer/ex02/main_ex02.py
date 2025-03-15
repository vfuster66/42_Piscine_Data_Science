import psycopg2
import pandas as pd
from printer import Printer

printer = Printer()

def create_table(cursor, table_name, df):
    columns = []
    for col in df.columns:
        if 'date' in col.lower() or 'time' in col.lower():
            columns.append(f'"{col}" TIMESTAMP')
        elif df[col].dtype == 'int64':
            columns.append(f'"{col}" INTEGER')
        elif df[col].dtype == 'float64':
            columns.append(f'"{col}" FLOAT')
        else:
            columns.append(f'"{col}" TEXT')

    query = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({", ".join(columns)});'
    printer.info(f"Création de la table avec la requête :\n{query}")
    cursor.execute(query)
    printer.success(f"Table {table_name} créée ou déjà existante.")

def import_csv_to_db_with_copy(file_path, table_name):
    try:
        conn = psycopg2.connect(
            dbname='piscineds',
            user='vfuster',
            password='Bonjour42',
            host='db'
        )
        cursor = conn.cursor()

        printer.title(f"Import de {file_path} dans {table_name} via COPY")

        # Lecture pour la création de la table
        printer.section("Lecture du fichier CSV pour création de la table...")
        df = pd.read_csv(file_path, nrows=1)
        create_table(cursor, table_name, df)
        conn.commit()

        # Import via COPY
        printer.section("Import via COPY...")
        with open(file_path, 'r') as f:
            next(f)  # skip header
            cursor.copy_expert(f'COPY "{table_name}" FROM STDIN WITH CSV', f)

        conn.commit()
        printer.success(f"Import via COPY terminé pour {table_name} ✅")

    except Exception as e:
        printer.error(f"Erreur durant l'import COPY : {e}")

    finally:
        cursor.close()
        conn.close()
        printer.info("Connexion PostgreSQL fermée.")

def main():
    file_path = 'customer/data_2022_oct.csv'
    table_name = 'data_2022_oct'
    import_csv_to_db_with_copy(file_path, table_name)

if __name__ == "__main__":
    main()
