import sqlalchemy as db
import pandas as pd

# Database credentials
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_name = 'big_data'

def get_data(query):
    connection_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    engine = db.create_engine(connection_url)
    conn = engine.connect()
    result = pd.read_sql(query, conn)
    conn.close()
    engine.dispose()
    return result


def fetch_all_data():
    query = "SELECT * FROM df_order"
    return get_data(query)

# Get top 10 selling products
def get_top_selling_products():
    query = """
    SELECT `product_id`, SUM(sale_price) AS sales FROM `df_order`
    GROUP BY `product_id`
    ORDER BY sales DESC
    LIMIT 10;
    """
    return get_data(query)