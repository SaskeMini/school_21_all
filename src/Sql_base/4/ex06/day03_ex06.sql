SELECT menu1.pizza_name AS pizza_name, p1.name AS pizzeria_name1, p2.name AS pizzeria_name2, menu1.price AS price FROM pizzeria AS p1
INNER JOIN pizzeria AS p2 ON p1.id > p2.id
INNER JOIN menu AS menu1 ON p1.id = menu1.pizzeria_id
INNER JOIN menu AS menu2 ON p2.id = menu2.pizzeria_id AND menu2.price = menu1.price AND menu2.pizza_name = menu1.pizza_name
ORDER BY pizza_name