SELECT COALESCE(person.name, '-') AS person_name, person_visits.visit_date AS visit_date, COALESCE(pizzeria.name, '-') AS pizzeria_name FROM person
LEFT JOIN person_visits ON (person_visits.person_id = person.id 
AND (person_visits.visit_date = '2022-01-01' OR person_visits.visit_date = '2022-01-02' OR person_visits.visit_date = '2022-01-03'))
FULL OUTER JOIN pizzeria ON person_visits.pizzeria_id = pizzeria.id
ORDER BY person_name, visit_date, pizzeria_name