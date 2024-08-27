SELECT coalesce(u.name, 'not defined') as name,
    coalesce(u.lastname, 'not defined') as lastname,
    temp.type,
    temp.volume,
    coalesce(c.name, 'not defined') as currency_name,
    coalesce((SELECT rate_to_usd 
            FROM currency c1 
            WHERE c1.id = c.id and c1.updated = c.last_updated), 1) 
            AS last_rate_to_usd,
    temp.volume::numeric * coalesce(
        (SELECT rate_to_usd 
        FROM currency c1 
        WHERE c1.id = c.id and c1.updated = c.last_updated),1) 
        AS total_volume_in_usd
FROM (
SELECT user_id, type, currency_id, sum(money) as volume
FROM  balance b
GROUP BY user_id,type, currency_id) as temp
FULL JOIN "user" u 
ON u.id = temp.user_id
FULL JOIN (SELECT id, name, max(updated) as last_updated 
    FROM currency c 
    GROUP BY id, name) as c 
ON c.id = temp.currency_id
ORDER BY 1 DESC, 2, 3;