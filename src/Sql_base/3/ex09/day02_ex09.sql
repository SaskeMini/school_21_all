SELECT person.name AS name FROM person
INNER JOIN person_order ON person.id = person_order.person_id AND (person.gender = 'female')
INNER JOIN menu ON menu.id = person_order.menu_id AND menu.pizza_name = 'pepperoni pizza'
INTERSECT
SELECT person.name AS name FROM person
INNER JOIN person_order ON person.id = person_order.person_id AND (person.gender = 'female')
INNER JOIN menu ON menu.id = person_order.menu_id AND menu.pizza_name = 'cheese pizza'
ORDER BY name