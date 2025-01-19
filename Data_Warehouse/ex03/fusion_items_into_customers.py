import psycopg2


def integrate_items_into_customers():
    """
    Intègre les données de la table 'items' dans la table 'customers'.
    """
    dbname = "piscineds"
    user = "vfuster"
    password = "Bonjour42"
    host = "localhost"
    port = "5432"

    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connecté à PostgreSQL !")
        cursor = conn.cursor()

        # Étape 1 : Ajouter les colonnes nécessaires dans 'customers'
        print("Ajout des colonnes nécessaires dans 'customers'...")
        cursor.execute("""
        ALTER TABLE customers
        ADD COLUMN IF NOT EXISTS category_id NUMERIC(20),
        ADD COLUMN IF NOT EXISTS category_code TEXT,
        ADD COLUMN IF NOT EXISTS brand VARCHAR(50);
        """)
        conn.commit()

        # Étape 2 : Mise à jour des données existantes dans 'customers'
        print("Mise à jour des données existantes dans 'customers'...")
        cursor.execute("""
        UPDATE customers
        SET category_id = i.category_id,
            category_code = i.category_code,
            brand = i.brand
        FROM items i
        WHERE customers.product_id = i.product_id;
        """)
        conn.commit()

        # Étape 3 : Ajouter les produits manquants depuis 'items'
        print("Ajout des produits manquants depuis 'items'...")
        cursor.execute("""
        INSERT INTO customers (product_id, category_id, category_code, brand)
        SELECT i.product_id, i.category_id, i.category_code, i.brand
        FROM items i
        WHERE i.product_id NOT IN (SELECT DISTINCT product_id FROM customers);
        """)
        conn.commit()

        # Étape 4 : Vérification des résultats
        cursor.execute("SELECT COUNT(*) FROM customers;")
        total_rows = cursor.fetchone()[0]
        print("Nombre total de lignes dans 'customers' après intégration : "
              f"{total_rows}")

    except psycopg2.Error as error:
        print(f"Erreur PostgreSQL : {error}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
        print("Connexion PostgreSQL fermée.")


if __name__ == "__main__":
    integrate_items_into_customers()
