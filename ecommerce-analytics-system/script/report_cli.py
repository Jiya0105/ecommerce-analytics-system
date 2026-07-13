import sqlite3
import pandas as pd
import os

print("="*60)
print("E-COMMERCE ANALYTICS REPORT")
print("="*60)

# Create output folder
os.makedirs("output", exist_ok=True)

# Connect Database
conn = sqlite3.connect("ecommerce.db")

print("Connected to ecommerce.db")

# ---------------------------------------------------
# 1. Total Revenue
# ---------------------------------------------------

query1 = """
SELECT
SUM(p.price * oi.quantity) AS Total_Revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id;
"""

df1 = pd.read_sql_query(query1, conn)

print("\nTOTAL REVENUE")
print(df1)

df1.to_csv("output/total_revenue.csv", index=False)

# ---------------------------------------------------
# 2. Revenue By Category
# ---------------------------------------------------

query2 = """
SELECT

p.category,

SUM(p.price*oi.quantity) AS Revenue

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

GROUP BY p.category

ORDER BY Revenue DESC;
"""

df2 = pd.read_sql_query(query2, conn)

print("\nREVENUE BY CATEGORY")
print(df2)

df2.to_csv("output/revenue_by_category.csv", index=False)

# ---------------------------------------------------
# 3. Top Customers
# ---------------------------------------------------

query3 = """
SELECT

c.customer_id,
c.name,

SUM(p.price*oi.quantity)
AS TotalSpent

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN order_items oi

ON o.order_id=oi.order_id

JOIN products p

ON oi.product_id=p.product_id

GROUP BY

c.customer_id,
c.name

ORDER BY TotalSpent DESC

LIMIT 10;
"""

df3 = pd.read_sql_query(query3, conn)

print("\nTOP 10 CUSTOMERS")
print(df3)

df3.to_csv("output/top_customers.csv", index=False)

# ---------------------------------------------------
# 4. Top Products
# ---------------------------------------------------

query4 = """
SELECT

p.product_name,

SUM(oi.quantity) AS QuantitySold,

SUM(p.price*oi.quantity) AS Revenue

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

GROUP BY p.product_name

ORDER BY Revenue DESC

LIMIT 10;
"""

df4 = pd.read_sql_query(query4, conn)

print("\nTOP PRODUCTS")
print(df4)

df4.to_csv("output/top_products.csv", index=False)

# ---------------------------------------------------
# 5. Customer Ranking (Window Function)
# ---------------------------------------------------

query5 = """
SELECT

c.customer_id,
c.name,

SUM(p.price*oi.quantity) AS TotalSpent,

RANK() OVER(
ORDER BY SUM(p.price*oi.quantity) DESC
) AS CustomerRank

FROM customers c

JOIN orders o

ON c.customer_id=o.customer_id

JOIN order_items oi

ON o.order_id=oi.order_id

JOIN products p

ON oi.product_id=p.product_id

GROUP BY
c.customer_id,
c.name;
"""

df5 = pd.read_sql_query(query5, conn)

print("\nCUSTOMER RANKING")
print(df5.head(10))

df5.to_csv("output/customer_ranking.csv", index=False)

# ---------------------------------------------------
# 6. Running Revenue
# ---------------------------------------------------

query6 = """
SELECT

o.order_date,

SUM(p.price*oi.quantity) AS DailyRevenue,

SUM(
SUM(p.price*oi.quantity)
)

OVER(

ORDER BY o.order_date

)

AS RunningRevenue

FROM orders o

JOIN order_items oi

ON o.order_id=oi.order_id

JOIN products p

ON oi.product_id=p.product_id

GROUP BY o.order_date;
"""

df6 = pd.read_sql_query(query6, conn)

print("\nRUNNING REVENUE")
print(df6.head())

df6.to_csv("output/running_revenue.csv", index=False)

# ---------------------------------------------------
# 7. Cohort Analysis
# ---------------------------------------------------

query7 = """
WITH FirstPurchase AS(

SELECT

customer_id,

MIN(order_date)

AS first_purchase

FROM orders

GROUP BY customer_id

)

SELECT

strftime('%Y-%m',first_purchase)

AS Cohort,

COUNT(customer_id)

AS Customers

FROM FirstPurchase

GROUP BY Cohort

ORDER BY Cohort;
"""

df7 = pd.read_sql_query(query7, conn)

print("\nCOHORT ANALYSIS")
print(df7)

df7.to_csv("output/cohort_analysis.csv", index=False)

# ---------------------------------------------------
# 8. Repeat Customers
# ---------------------------------------------------

query8 = """
SELECT

customer_id,

COUNT(order_id)

AS Orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)>1

ORDER BY Orders DESC;
"""

df8 = pd.read_sql_query(query8, conn)

print("\nREPEAT CUSTOMERS")
print(df8.head(20))

df8.to_csv("output/repeat_customers.csv", index=False)

conn.close()

print("\n")
print("="*60)
print("ALL REPORTS GENERATED SUCCESSFULLY")
print("="*60)

print("\nReports Saved Inside OUTPUT Folder")