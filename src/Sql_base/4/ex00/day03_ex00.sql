SELECT menu.pizza_name AS pizza_name, menu.price AS price, pizzeria.name AS pizzeria_name, person_visits.visit_date AS visit_date FROM person_visits
INNER JOIN person ON person_visits.person_id = person.id AND person.name = 'Kate'
INNER JOIN pizzeria ON pizzeria.id = person_visits.pizzeria_id
INNER JOIN menu ON pizzeria.id = menu.pizzeria_id AND price >= 800 AND price <= 1000
ORDER BY pizza_name, price, pizzeria_name 