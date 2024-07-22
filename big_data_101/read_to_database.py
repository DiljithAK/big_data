import kaggle
import pandas as pd
from sqlalchemy import create_engine

# !!! Getting Data and cleaning Data !!!
# ======================================

df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
# print(df.head(20)) # Get list first 20 datas
# print(df['Ship Mode'].unique()) # Get unique values in a column
# print(df.columns) # Get all column headings

df.columns = df.columns.str.lower() # Convert headings to lower case
df.columns = df.columns.str.replace(' ', '_') # Replace space with under score

"""In our csv file, we have cost_price, list_price and discount_percent. We need to create a new column called discount_price in the data frame by calculating the list price and discount_percent"""

# Create new columns in the data frame
df['discount_price'] = df['list_price'] * df['discount_percent'] * 0.01
df['sale_price'] = df['list_price'] - df['discount_price']
df['profit'] = df['sale_price'] - df['cost_price']

# Convert order_date object to date
df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")

# Drop columns which we don't need any more. eg: cost_price
df.drop(columns=['cost_price', 'list_price', 'discount_percent'], inplace=True) # If inplace=True didn't provided these drop change won't show in the df.

# !!! Store Data into SQL Server !!!
# ==================================

# Database credentials
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_name = 'big_data'

# Connection URL
connection_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

# Create engine and connect to db
engine = create_engine(connection_url)
conn = engine.connect()

df.to_sql('df_order', con=conn, index=False, if_exists='append') # replace
