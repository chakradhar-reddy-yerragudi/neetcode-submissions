-- Write your query below
/*SELECT c.name FROM customers AS c
WHERE NOT EXISTS(SELECT 1 FROM orders AS o where o.customer_id = c.id)
*/
SELECT c.name FROM customers AS c
WHERE c.id NOT IN(SELECT customer_id FROM orders )
