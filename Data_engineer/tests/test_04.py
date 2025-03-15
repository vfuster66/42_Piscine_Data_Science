import pytest
import psycopg2

DB_PARAMS = {
    'dbname': 'piscineds',
    'user': 'vfuster',
    'password': 'Bonjour42',
    'host': 'db'
}


def test_connection():
    """Teste la connexion à la base de données."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.close()
    except Exception as e:
        pytest.fail(f"Connexion échouée : {e}")


def test_table_exists():
    """Teste si la table 'items' existe."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_schema = 'public' AND table_name = 'items'
            );
        """)
        exists = cursor.fetchone()[0]
        conn.close()
        assert exists, "La table 'items' n'existe pas"
    except Exception as e:
        pytest.fail(f"Erreur lors de la vérification de la table : {e}")


def test_row_count():
    """Teste si la table 'items' contient des données."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM items;")
        count = cursor.fetchone()[0]
        conn.close()
        assert count > 0, "La table 'items' est vide"
    except Exception as e:
        pytest.fail(f"Erreur lors de la vérification des données : {e}")
