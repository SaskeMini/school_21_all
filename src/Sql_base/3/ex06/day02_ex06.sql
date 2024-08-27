SELECT menu.pizza_name AS pizza_name, pizzeria.name AS pizzeria_name FROM menu
INNER JOIN person_order ON menu.id = person_order.menu_id
INNER JOIN pizzeria ON menu.pizzeria_id = pizzeria.id
INNER JOIN person ON person_order.person_id = person.id AND (person.name = 'Denis' OR person.name = 'Anna')
ORDER BY pizza_name, pizzeria_name