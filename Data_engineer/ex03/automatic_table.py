import os
import psycopg2
import pandas as pd
from printer import Printer

printer = Printer()

DB_PARAMS = {
    'dbname': 'piscineds',
    'user': 'vfuster',
    'password': 'Bonjour42',
    'host': 'db'
}

CUSTOMER_DIR = 'customer/'


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

    query = (
        f'CREATE TABLE IF NOT EXISTS "{table_name}" '
        f'({", ".join(columns)});'
    )
    printer.info(f"Création de la table : {table_name}")
    printer.info(f"Requête SQL : {query}")
    cursor.execute(query)


def import_csv_with_copy(cursor, table_name, file_path):
    printer.section(f"Import de {file_path} via COPY dans {table_name}")
    with open(file_path, 'r') as f:
        next(f)  # skip header
        cursor.copy_expert(f'COPY "{table_name}" FROM STDIN WITH CSV', f)
    printer.success(f"Import terminé pour {table_name}")


def import_all_csv():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        printer.title("Import automatique des CSV du dossier 'customer/'")

        files = [f for f in os.listdir(CUSTOMER_DIR) if f.endswith('.csv')]

        if not files:
            printer.warning(
                "Aucun fichier CSV trouvé dans le dossier customer/"
            )
            return

        for file_name in files:
            table_name = os.path.splitext(file_name)[0]
            file_path = os.path.join(CUSTOMER_DIR, file_name)

            printer.section(f"Traitement du fichier {file_name}")

            # Lire les colonnes pour créer la table
            df = pd.read_csv(file_path, nrows=1)
            create_table(cursor, table_name, df)
            conn.commit()

            # Importer le CSV complet
            import_csv_with_copy(cursor, table_name, file_path)
            conn.commit()

        printer.success(
            "✅ Tous les fichiers CSV ont été importés avec succès."
        )

    except Exception as e:
        printer.error(f"Erreur durant l'import automatique : {e}")

    finally:
        cursor.close()
        conn.close()
        printer.info("Connexion PostgreSQL fermée.")


def main():
    import_all_csv()


if __name__ == "__main__":
    main()
