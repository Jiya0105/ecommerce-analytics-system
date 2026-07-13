-- =======================================
-- CUSTOMER RANKING
-- =======================================

SELECT

c.customer_id,
c.name,

SUM(
p.price*oi.quantity
) AS TotalSpent,

RANK() OVER(

ORDER BY

SUM(p.price*oi.quantity)

DESC

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

------------------------------------------------

-- Running Revenue

SELECT

o.order_date,

SUM(
p.price*oi.quantity
) AS DailyRevenue,

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