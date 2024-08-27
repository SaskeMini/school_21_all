CREATE materialized VIEW mv_dmitriy_visits_and_eats AS (
SELECT pizzeria.name AS name FROM pizzeria
INNER JOIN person_visits ON pizzeria.id = person_visits.pizzeria_id AND person_visits.visit_date = '2022-01-08'
INNER JOIN menu ON menu.pizzeria_id = pizzeria.id AND (menu.price < 800)
INNER JOIN person ON person.id = person_visits.person_id AND person.name = 'Dmitriy'
)