import pandas as pd
import mysql.connector
from mysql.connector import Error

# Load data from CSV
csv_file_path = "/Users/ravitejanb/Documents/Fortes_retail/orders_table.csv"

df = pd.read_csv(csv_file_path)

# MySQL connection details
host = "localhost"
user = "root"
password = "havefun1783"
database = "fortinos_s1_retail"

# SQL create table query
create_table_query = """
CREATE TABLE IF NOT EXISTS orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATETIME,
    ShipDate DATETIME,
    OrderAmount DECIMAL(10, 2),
    OrderStatus VARCHAR(50),
    PaymentMethod VARCHAR(50),
    ShippingAddress TEXT,
    ProductID INT,
    Quantity INT
);
"""

# Function to insert data into the database
def insert_data_to_mysql(dataframe, connection):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO orders (OrderID, CustomerID, OrderDate, ShipDate, OrderAmount, OrderStatus, PaymentMethod, ShippingAddress, ProductID, Quantity)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for _, row in dataframe.iterrows():
        cursor.execute(insert_query, tuple(row))
    connection.commit()

# Connect to MySQL and execute operations
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute(create_table_query)  # Create table if it does not exist
        insert_data_to_mysql(df, connection)  # Insert data from CSV
        print("Data inserted successfully into MySQL database.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
