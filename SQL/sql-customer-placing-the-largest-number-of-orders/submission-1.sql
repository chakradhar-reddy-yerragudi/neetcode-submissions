-- Write your query below

SELECT  customer_number FROM ORDERS GROUP BY customer_number ORDER BY 
count(*) DESC LIMIT 1
