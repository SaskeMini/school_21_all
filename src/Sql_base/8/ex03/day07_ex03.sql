SELECT s1.name, COALESCE(s1.count, 0) + COALESCE(s2.count, 0) AS total_count
FROM
((SELECT pizzeria.name AS name, COUNT(*) AS count FROM person_order
INNER JOIN menu ON menu.id = person_order.menu_id
INNER JOIN pizzeria ON pizzeria.id = menu.pizzeria_id
GROUP BY name) AS s1
FULL JOIN
(SELECT pizzeria.name AS name, COUNT(*) AS count FROM person_visits
INNER JOIN pizzeria ON pizzeria.id = person_visits.pizzeria_id
GROUP BY name) AS s2 ON s1.name = s2.name)
ORDER BY total_count DESC, 1 ASC