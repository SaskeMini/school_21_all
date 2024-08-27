INSERT INTO person_visits (id, person_id, pizzeria_id, visit_date)
VALUES ((SELECT MAX(id) FROM person_visits) + 1, (SELECT id FROM person WHERE name = 'Dmitriy'), 
(SELECT pizzeria.id FROM pizzeria INNER JOIN menu ON menu.pizzeria_id = pizzeria.id WHERE menu.price < 800 AND name != 'Papa Johns' limit 1), '2022-01-08');

refresh materialized VIEW mv_dmitriy_visits_and_eats;
