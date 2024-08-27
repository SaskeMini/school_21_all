SELECT menu.pizza_name AS pizza_name, pizzeria.name AS pizzeria_name, menu.price AS price FROM menu
INNER JOIN pizzeria ON pizzeria.id = menu.pizzeria_id AND (pizza_name = 'mushroom pizza' OR pizza_name = 'pepperoni pizza')
ORDER BY pizza_name, pizzeria_name