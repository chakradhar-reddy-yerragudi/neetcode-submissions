-- Write your query below

SELECT  name as customer_name,customer_id,order_id,order_date
FROM (
    SELECT c.name,c.customer_id,o.order_id,o.order_date,
    ROW_NUMBER() OVER(PARTITION BY c.customer_id ORDER BY o.order_date DESC)
    as rn
    FROM customers as c JOIN orders as o ON c.customer_id=o.customer_id
) WHERE rn<=3 ORDER BY customer_name ASC, customer_id ASC,order_date DESC
