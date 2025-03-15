import pytest
import psycopg2

DB_PARAMS = {
    'dbname': 'piscineds',
    'user': 'vfuster',
    'password': 'Bonjour42',
    'host': 'db'
}

TABLES = [
    'data_2022_oct',
    'data_2022_nov',
    'data_2022_dec'
    # Tu ajoutes ici les autres tables que tu attends
]


def test_connection():
    """Teste la connexion à la base."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.close()
    except Exception as e:
        pytest.fail(f"Connexion échouée : {e}")


@pytest.mark.parametrize("table_name", TABLES)
def test_table_exists(table_name):
    """Teste si la table existe."""
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
        pytest.fail(f"Erreur vérification table {table_name} : {e}")


@pytest.mark.parametrize("table_name", TABLES)
def test_row_count(table_name):
    """Teste si la table contient des données."""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()

        cursor.execute(f'SELECT COUNT(*) FROM "{table_name}";')
        count = cursor.fetchone()[0]
        conn.close()

        assert count > 0, f"La table {table_name} est vide"
    except Exception as e:
        pytest.fail(f"Erreur vérification des données dans {table_name} : {e}")
