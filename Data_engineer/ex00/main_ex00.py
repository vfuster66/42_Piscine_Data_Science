"""
ex00/main_ex00.py

Script pour créer la base de données piscineds et configurer les droits.
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from printer import Printer

printer = Printer()


def create_database():
    printer.header("Création de la base piscineds")
    try:
        # Connexion à PostgreSQL en tant que superuser postgres
        conn = psycopg2.connect(
            dbname='postgres', user='postgres', password='Bonjour42', host='db'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Kill connexions existantes
        cursor.execute("""
            SELECT pg_terminate_backend(pg_stat_activity.pid)
            FROM pg_stat_activity
            WHERE pg_stat_activity.datname = 'piscineds'
            AND pid <> pg_backend_pid();
        """)

        # Supprimer base si existante
        cursor.execute("DROP DATABASE IF EXISTS piscineds;")
        printer.info("Ancienne base supprimée (si existante).")

        # Créer la base
        cursor.execute("CREATE DATABASE piscineds;")
        printer.success("Base piscineds créée.")

        cursor.close()
        conn.close()

    except Exception as e:
        printer.error(f"Erreur lors de la création de la base : {e}")


def grant_privileges():
    printer.header("Attribution des privilèges à l'utilisateur vfuster")
    try:
        conn = psycopg2.connect(
            dbname='piscineds',
            user='vfuster',
            password='Bonjour42',
            host='db'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Créer l'utilisateur si inexistant
        cursor.execute("""
            DO $$
            BEGIN
                IF NOT EXISTS (
                    SELECT FROM pg_catalog.pg_roles
                    WHERE rolname = 'vfuster'
                ) THEN
                    CREATE ROLE vfuster LOGIN PASSWORD 'Bonjour42';
                END IF;
            END
            $$;
        """)
        printer.info("Utilisateur vfuster vérifié/créé.")

        # Droits sur la DB
        cursor.execute(
            "GRANT ALL PRIVILEGES ON DATABASE piscineds TO vfuster;"
        )
        cursor.execute("GRANT ALL ON SCHEMA public TO vfuster;")
        cursor.execute("""
            ALTER DEFAULT PRIVILEGES IN SCHEMA public
            GRANT ALL ON TABLES TO vfuster;
        """)
        printer.success("Privilèges accordés à vfuster.")

        cursor.close()
        conn.close()

    except Exception as e:
        printer.error(f"Erreur lors de l'attribution des privilèges : {e}")


def run():
    create_database()
    grant_privileges()
    printer.footer("Ex00 terminé.")


if __name__ == "__main__":
    run()
