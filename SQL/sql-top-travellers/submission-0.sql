-- Write your query below




SELECT u.name,
CASE 
WHEN SUM(r.distance) IS NULL THEN 0
ELSE SUM(r.distance)
END

as travelled_distance
FROM users as u LEFT JOIN rides as r
ON u.id=r.user_id GROUP BY  u.name ORDER BY travelled_distance DESC,name ASC;


