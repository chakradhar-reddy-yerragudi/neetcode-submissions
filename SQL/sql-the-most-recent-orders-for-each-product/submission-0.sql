-- Write your query below

WITH wind as (
    SELECT product_name,o.product_id,order_id,order_date,
    RANK() OVER(PARTITION BY o.product_id ORDER BY order_date DESC) as r
    FROM orders as o JOIN customers as c
    ON o.customer_id=c.customer_id JOIN
    products as p
    ON o.product_id=p.product_id
)

select product_name,product_id,order_id,order_date FROM wind 
WHERE r=1 ORDER BY product_name,product_id,order_id;
