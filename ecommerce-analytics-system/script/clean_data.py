import pandas as pd
from datetime import datetime
import os

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

# Create cleaned folder
os.makedirs("data/cleaned", exist_ok=True)

# Load datasets
customers = pd.read_csv("data/raw/customers.csv")
products = pd.read_csv("data/raw/products.csv")
orders = pd.read_csv("data/raw/orders.csv")
order_items = pd.read_csv("data/raw/order_items.csv")

print("Datasets Loaded Successfully")

print("\nOriginal Rows")
print("----------------------")
print("Customers :", len(customers))
print("Products :", len(products))
print("Orders :", len(orders))
print("Order Items :", len(order_items))
print("\nRemoving Duplicate Records...")

customers = customers.drop_duplicates()

products = products.drop_duplicates()

orders = orders.drop_duplicates()

order_items = order_items.drop_duplicates()

print("Duplicate Removal Completed")
print("\nHandling Missing Values...")

customers["email"] = customers["email"].fillna("unknown@email.com")

customers["name"] = customers["name"].replace("", "Unknown")

print("Missing Values Handled")
print("\nRemoving Negative Prices...")

products = products[products["price"] > 0]

print("Remaining Products :", len(products))
print("\nRemoving Negative Quantities...")

order_items = order_items[order_items["quantity"] > 0]
orders["order_date"] = pd.to_datetime(orders["order_date"])

today = pd.Timestamp.today()

orders = orders[orders["order_date"] <= today]
valid_customers = customers["customer_id"]

orders = orders[
    orders["customer_id"].isin(valid_customers)
]
valid_orders = orders["order_id"]

order_items = order_items[
    order_items["order_id"].isin(valid_orders)
]
valid_products = products["product_id"]

order_items = order_items[
    order_items["product_id"].isin(valid_products)
]
customers.to_csv(
    "data/cleaned/customers_clean.csv",
    index=False
)

products.to_csv(
    "data/cleaned/products_clean.csv",
    index=False
)

orders.to_csv(
    "data/cleaned/orders_clean.csv",
    index=False
)

order_items.to_csv(
    "data/cleaned/order_items_clean.csv",
    index=False
)

print("\nCleaning Completed Successfully")

print("\nFinal Rows")
print("----------------------")
print("Customers :", len(customers))
print("Products :", len(products))
print("Orders :", len(orders))
print("Order Items :", len(order_items))