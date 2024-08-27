SELECT menu.pizza_name AS pizza_name, menu.price AS price, pizzeria.name AS pizzeria_name FROM pizzeria
INNER JOIN menu ON pizzeria.id = menu.pizzeria_id
WHERE NOT EXISTS (
    SELECT menu_id FROM person_order
    WHERE person_order.menu_id = menu.id
)
ORDER BY pizza_name, price