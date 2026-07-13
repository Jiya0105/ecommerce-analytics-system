-- ============================================
-- CUSTOMER RETENTION
-- ============================================

WITH FirstPurchase AS (

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

------------------------------------------------

-- Repeat Customers

SELECT

customer_id,

COUNT(order_id)

AS Orders

FROM orders

GROUP BY customer_id

HAVING COUNT(order_id)>1

ORDER BY Orders DESC;