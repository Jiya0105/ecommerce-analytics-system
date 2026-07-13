-- ============================================
-- TOTAL REVENUE
-- ============================================

SELECT
SUM(p.price * oi.quantity) AS Total_Revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id;

------------------------------------------------

-- Revenue by Category

SELECT
p.category,
SUM(p.price * oi.quantity) AS Revenue
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY Revenue DESC;

------------------------------------------------

-- Top 10 Customers

SELECT

c.customer_id,
c.name,

SUM(
p.price * oi.quantity
) AS Total_Spent

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

ORDER BY Total_Spent DESC

LIMIT 10;

------------------------------------------------

-- Top Products

SELECT

p.product_name,

SUM(oi.quantity) AS Quantity_Sold,

SUM(p.price*oi.quantity) AS Revenue

FROM products p

JOIN order_items oi

ON p.product_id=oi.product_id

GROUP BY p.product_name

ORDER BY Revenue DESC;