import sqlite3
import pandas as pd

print("=" * 60)
print("LOADING DATA INTO SQLITE DATABASE")
print("=" * 60)

# Connect to SQLite Database
conn = sqlite3.connect("ecommerce.db")

print("Database Created Successfully")

# Read cleaned CSV files
customers = pd.read_csv("data/cleaned/customers_clean.csv")
products = pd.read_csv("data/cleaned/products_clean.csv")
orders = pd.read_csv("data/cleaned/orders_clean.csv")
order_items = pd.read_csv("data/cleaned/order_items_clean.csv")

print("Cleaned CSV Files Loaded")

# Load into SQLite Tables
customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

order_items.to_sql(
    "order_items",
    conn,
    if_exists="replace",
    index=False
)

print("Tables Created Successfully")

# Verify Row Counts
cursor = conn.cursor()

tables = [
    "customers",
    "products",
    "orders",
    "order_items"
]

print("\nRow Counts")

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

conn.commit()
conn.close()

print("\nDatabase Loading Completed Successfully")