import os
from db_connection import *
from plot import *

# data = fetch_all_data()
data = get_top_selling_products()
os.makedirs('big_data_101/plot', exist_ok=True)
plot_top_selling_products(data)
# print(data)
