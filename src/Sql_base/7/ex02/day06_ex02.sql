SELECT person.name AS name, menu.pizza_name AS pizza_name, menu.price AS price,
(menu.price - (person_discounts.discount / 100) * menu.price) AS discount_price, pizzeria.name AS pizzeria_name FROM menu
INNER JOIN person_order ON person_order.menu_id = menu.id
INNER JOIN person ON person.id = person_order.person_id
INNER JOIN pizzeria ON pizzeria.id = menu.pizzeria_id
INNER JOIN person_discounts ON person_discounts.person_id = person.id AND person_discounts.pizzeria_id = pizzeria.id
ORDER BY name, pizza_name;