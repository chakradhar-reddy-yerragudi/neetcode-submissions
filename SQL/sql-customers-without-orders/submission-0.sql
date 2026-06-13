-- Write your query below
SELECT c.name FROM customers AS c
WHERE NOT EXISTS(SELECT 1 FROM orders AS o where o.customer_id = c.id)