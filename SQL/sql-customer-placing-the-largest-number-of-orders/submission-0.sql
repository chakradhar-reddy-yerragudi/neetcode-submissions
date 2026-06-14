-- Write your query below
with cttable as (SELECT customer_number,count(customer_number)as sctnm from orders group by customer_number)

SELECT DISTINCT customer_number FROM ORDERS GROUP BY customer_number HAVING
COUNT(customer_number)=(SELECT MAX(sctnm) FROM cttable)