"""
ex00/tester.py

Testeur pour ex00 : création DB & vérification connexion utilisateur.
"""

from main_ex00 import run
import psycopg2
from printer import Printer

printer = Printer()


def test_connection():
    printer.header("Vérification de la connexion avec vfuster")
    try:
        conn = psycopg2.connect(
            dbname='piscineds',
            user='vfuster',
            password='Bonjour42',
            host='db'
        )
        printer.success(
            "Connexion établie avec succès à piscineds via vfuster."
        )
        conn.close()
    except Exception as e:
        printer.error(f"Échec de la connexion : {e}")


def main():
    run()
    test_connection()


if __name__ == "__main__":
    main()
