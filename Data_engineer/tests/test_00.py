"""
tests/test_ex00.py

Tests unitaires pour ex00.
"""

import psycopg2
import pytest


def test_user_connection():
    """Test si la connexion avec vfuster fonctionne."""
    try:
        conn = psycopg2.connect(
            dbname='piscineds',
            user='vfuster',
            password='Bonjour42',
            host='db'
        )
        assert conn is not None
        conn.close()
    except Exception as e:
        pytest.fail(f"Connexion échouée : {e}")
