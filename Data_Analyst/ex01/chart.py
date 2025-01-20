import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def create_charts():
    """
    Génère trois graphiques basés sur les données filtrées de 'customers'.
    """
    dbname = "piscineds"
    user = "vfuster"
    password = "Bonjour42"
    host = "localhost"
    port = "5432"

    try:
        # Connexion à PostgreSQL
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connecté à PostgreSQL !")

        # Charger les données filtrées dans un DataFrame Pandas
        query = """
        SELECT event_time, price, user_id
        FROM customers
        WHERE event_type = 'purchase'
          AND event_time >= '2022-10-01'
          AND event_time < '2023-02-01';
        """
        df = pd.read_sql(query, conn, parse_dates=['event_time'])

        # Ajouter une colonne 'day' et 'month'
        df['day'] = df['event_time'].dt.date
        df['month'] = df['event_time'].dt.to_period('M')

        # Graphique 1 : Dépenses moyennes par client par jour
        avg_spend_per_customer = df.groupby('day').apply(
            lambda x: x['price'].sum() / x['user_id'].nunique()
        )
        plt.figure(figsize=(5, 6))
        avg_spend_per_customer.plot(kind='area', alpha=0.5)
        plt.title('Dépenses moyennes par client par jour', pad=20)
        plt.ylabel('Dépenses moyennes par client (Altairian Dollars)')
        plt.ylim(0, None)
        plt.xlim(pd.Timestamp('2022-10-01'), pd.Timestamp('2023-01-31'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=5))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
        plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)
        plt.savefig('average_spend_per_customer.png')
        plt.show()

        # Graphique 2 : Total des ventes par mois
        total_sales_per_month = df.groupby('month')['price'].sum() / 1_000_000
        plt.figure(figsize=(10, 6))
        total_sales_per_month.plot(kind='bar', alpha=0.7)
        plt.title('Total des ventes par mois', pad=20)
        plt.ylabel('Ventes totales (en millions d’Altairian Dollars)')
        plt.ylim(0, 1.6)
        plt.xticks(range(len(total_sales_per_month.index)),
                   [
                       month.strftime('%b')
                       for month in total_sales_per_month.index
                           ])
        plt.grid(visible=True, which='major', linestyle='--', linewidth=0.5)
        plt.savefig('total_sales_per_month.png')
        plt.show()

        # Graphique 3 : Nombre de clients par jour
        unique_customers_per_day = df.groupby('day')['user_id'].nunique()
        plt.figure(figsize=(10, 6))
        unique_customers_per_day.plot()
        plt.title('Nombre de clients uniques par jour', pad=20)
        plt.ylabel('Nombre de clients')
        plt.xlim(pd.Timestamp('2022-10-01'), pd.Timestamp('2023-01-31'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.gca().xaxis.set_minor_locator(mdates.DayLocator(interval=5))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
        plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)
        plt.savefig('unique_customers_per_day.png')
        plt.show()

        print("Graphiques générés avec succès !")

    except psycopg2.Error as error:
        print(f"Erreur PostgreSQL : {error}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
        print("Connexion PostgreSQL fermée.")


if __name__ == "__main__":
    create_charts()
