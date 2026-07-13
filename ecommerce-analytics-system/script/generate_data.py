# ============================================================
# E-COMMERCE ANALYTICS SYSTEM
# File: generate_data.py (PART 1)
# ============================================================

import pandas as pd
import random
import os
from faker import Faker
from datetime import datetime, timedelta

# ------------------------------------------------------------
# INITIAL SETUP
# ------------------------------------------------------------

fake = Faker()

random.seed(42)
Faker.seed(42)

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)

print("=" * 60)
print("Generating Ecommerce Dataset...")
print("=" * 60)

# ------------------------------------------------------------
# DATA SIZE
# ------------------------------------------------------------

NUM_CUSTOMERS = 500
NUM_PRODUCTS = 100
NUM_ORDERS = 3000
NUM_ORDER_ITEMS = 8000

# ------------------------------------------------------------
# PRODUCT INFORMATION
# ------------------------------------------------------------

product_catalog = {
    "Electronics": [
        "Laptop",
        "Smartphone",
        "Keyboard",
        "Mouse",
        "Headphones",
        "Monitor",
        "Tablet",
        "Smart Watch",
        "Camera",
        "Speaker"
    ],

    "Fashion": [
        "T-Shirt",
        "Jeans",
        "Jacket",
        "Shoes",
        "Sneakers",
        "Watch",
        "Handbag",
        "Cap",
        "Dress",
        "Sweater"
    ],

    "Home": [
        "Chair",
        "Table",
        "Sofa",
        "Lamp",
        "Curtains",
        "Mattress",
        "Fan",
        "Cup Set",
        "Bottle",
        "Storage Box"
    ],

    "Books": [
        "Python Book",
        "SQL Guide",
        "Data Science",
        "Machine Learning",
        "Algorithms",
        "Java Programming",
        "Operating System",
        "Networking",
        "DBMS",
        "AI Basics"
    ],

    "Sports": [
        "Football",
        "Cricket Bat",
        "Basketball",
        "Yoga Mat",
        "Dumbbell",
        "Badminton Racket",
        "Tennis Ball",
        "Helmet",
        "Gloves",
        "Skipping Rope"
    ]
}

cities = [
    "Delhi",
    "Mumbai",
    "Pune",
    "Chennai",
    "Jaipur",
    "Lucknow",
    "Kolkata",
    "Hyderabad",
    "Bangalore",
    "Ahmedabad"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash on Delivery",
    "Net Banking"
]

order_status = [
    "Delivered",
    "Pending",
    "Cancelled",
    "Returned"
]

# ============================================================
# GENERATE CUSTOMERS
# ============================================================

print("Generating Customers...")

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    customer = {

        "customer_id": customer_id,

        "name": fake.name(),

        "email": fake.email(),

        "city": random.choice(cities),

        "signup_date": fake.date_between(
            start_date="-2y",
            end_date="-30d"
        )

    }

    customers.append(customer)

customers_df = pd.DataFrame(customers)

print("Customers Generated :", len(customers_df))

# ============================================================
# GENERATE PRODUCTS
# ============================================================

print("Generating Products...")

products = []

product_id = 1

for category in product_catalog:

    for product in product_catalog[category]:

        price = random.randint(200, 50000)

        products.append({

            "product_id": product_id,

            "product_name": product,

            "category": category,

            "price": price

        })

        product_id += 1

# Generate remaining products

while len(products) < NUM_PRODUCTS:

    category = random.choice(list(product_catalog.keys()))

    product = random.choice(product_catalog[category]) + " " + str(random.randint(1,100))

    products.append({

        "product_id": product_id,

        "product_name": product,

        "category": category,

        "price": random.randint(200,50000)

    })

    product_id += 1

products_df = pd.DataFrame(products)

print("Products Generated :", len(products_df))

# ============================================================
# GENERATE ORDERS
# ============================================================

print("Generating Orders...")

orders = []

for order_id in range(1, NUM_ORDERS + 1):

    customer = random.randint(1, NUM_CUSTOMERS)

    order_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    orders.append({

        "order_id": order_id,

        "customer_id": customer,

        "order_date": order_date,

        "payment_method": random.choice(payment_methods),

        "status": random.choice(order_status)

    })

orders_df = pd.DataFrame(orders)

print("Orders Generated :", len(orders_df))

# ============================================================
# GENERATE ORDER ITEMS
# ============================================================

print("Generating Order Items...")

order_items = []

for item_id in range(1, NUM_ORDER_ITEMS + 1):

    order_items.append({

        "item_id": item_id,

        "order_id": random.randint(1, NUM_ORDERS),

        "product_id": random.randint(1, NUM_PRODUCTS),

        "quantity": random.randint(1,5)

    })

order_items_df = pd.DataFrame(order_items)

print("Order Items Generated :", len(order_items_df))

# ============================================================
# INTRODUCE DATA INCONSISTENCIES
# ============================================================

print("Introducing Data Inconsistencies...")

# Missing emails
customers_df.loc[random.sample(range(NUM_CUSTOMERS),20),"email"] = None

# Empty customer names
customers_df.loc[random.sample(range(NUM_CUSTOMERS),10),"name"] = ""

# Duplicate customer records
customers_df = pd.concat(
    [
        customers_df,
        customers_df.sample(5,random_state=42)
    ],
    ignore_index=True
)

# Negative prices
products_df.loc[random.sample(range(NUM_PRODUCTS),5),"price"] *= -1

# Invalid customer IDs
orders_df.loc[random.sample(range(NUM_ORDERS),10),"customer_id"] = 9999
# Invalid Product IDs
order_items_df.loc[random.sample(range(NUM_ORDER_ITEMS), 15), "product_id"] = 9999

# Negative Quantities
order_items_df.loc[random.sample(range(NUM_ORDER_ITEMS), 20), "quantity"] = -2

# Duplicate Orders
orders_df = pd.concat(
    [
        orders_df,
        orders_df.sample(10, random_state=42)
    ],
    ignore_index=True
)

# Future Order Dates
future_date = datetime.now() + timedelta(days=365)

orders_df.loc[
    random.sample(range(len(orders_df)), 10),
    "order_date"
] = future_date.date()

# Invalid Order IDs in Order Items
order_items_df.loc[
    random.sample(range(NUM_ORDER_ITEMS), 10),
    "order_id"
] = 99999

print("Data inconsistencies added successfully.")

# ============================================================
# SAVE CSV FILES
# ============================================================

print("\nSaving CSV Files...")

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

order_items_df.to_csv(
    "data/raw/order_items.csv",
    index=False
)

# ============================================================
# DISPLAY SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("DATA GENERATION SUMMARY")
print("=" * 60)

print(f"Customers     : {len(customers_df)}")
print(f"Products      : {len(products_df)}")
print(f"Orders        : {len(orders_df)}")
print(f"Order Items   : {len(order_items_df)}")

print("\nIntentional Inconsistencies Added:")
print("----------------------------------")
print("✔ Missing Emails")
print("✔ Empty Customer Names")
print("✔ Duplicate Customer Records")
print("✔ Duplicate Orders")
print("✔ Negative Product Prices")
print("✔ Negative Quantities")
print("✔ Invalid Customer IDs")
print("✔ Invalid Product IDs")
print("✔ Invalid Order IDs")
print("✔ Future Order Dates")

print("\nFiles Saved Successfully!")

print("data/raw/customers.csv")
print("data/raw/products.csv")
print("data/raw/orders.csv")
print("data/raw/order_items.csv")

print("=" * 60)
print("DATA GENERATION COMPLETED SUCCESSFULLY")
print("=" * 60)

# ============================================================
# DISPLAY SAMPLE DATA
# ============================================================

print("\nSample Customers")
print(customers_df.head())

print("\nSample Products")
print(products_df.head())

print("\nSample Orders")
print(orders_df.head())

print("\nSample Order Items")
print(order_items_df.head())