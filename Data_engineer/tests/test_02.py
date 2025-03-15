import psycopg2
import pytest

# Paramètres de connexion PostgreSQL
DB_PARAMS = {
    'dbname': 'piscineds',
    'user': 'vfuster',
    'password': 'Bonjour42',
    'host': 'db'
}


def test_connection():
    """Teste la connexion à la base 'piscineds'."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        assert conn is not None
        conn.close()
    except Exception as e:
        pytest.fail(f"Connexion échouée : {e}")


def test_table_exists():
    """Teste si la table 'data_2022_oct' existe."""
    table_name = 'data_2022_oct'
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_schema = 'public' AND table_name = %s
            );
        """, (table_name,))
        exists = cursor.fetchone()[0]
        conn.close()
        assert exists, f"La table {table_name} n'existe pas"
    except Exception as e:
        pytest.fail(f"Erreur lors de la vérification de la table : {e}")


def test_row_count():
    """Teste si la table contient des données (>= 1 ligne)."""
    table_name = 'data_2022_oct'
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        conn.close()
        assert count > 0, f"La table {table_name} est vide"
    except Exception as e:
        pytest.fail(f"Erreur lors de la vérification des données : {e}")
