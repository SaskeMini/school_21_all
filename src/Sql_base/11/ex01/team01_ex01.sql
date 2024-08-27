insert into currency values (100, 'EUR', 0.85, '2022-01-01 13:29'); 
insert into currency values (100, 'EUR', 0.79, '2022-01-08 13:29');

SELECT temp.name,
    temp.lastname,
    currency_name,
    money * rate_to_usd as currency_in_usd
FROM (
SELECT coalesce(u.name,'not defined') as name,
    coalesce(u.lastname,'not defined') as lastname,
    c.name as currency_name,
    money,
    coalesce((SELECT rate_to_usd 
        FROM currency c 
        WHERE b.currency_id = c.id and c.updated < b.updated ORDER BY  c.updated DESC limit 1),
        (SELECT rate_to_usd 
        FROM currency c 
        WHERE b.currency_id = c.id and c.updated > b.updated 
        ORDER BY  c.updated ASC limit 1)) as rate_to_usd
FROM balance b INNER JOIN
    (SELECT c.id, c.name FROM currency c group by c.id,c.name) as c 
    ON c.id = b.currency_id
    LEFT JOIN "user" u on u.id = b.user_id) as temp
ORDER BY 1 DESC,2,3;