SELECT DISTINCT person_order.order_date AS action_date, person.name AS person_name 
FROM person_order
LEFT JOIN person_visits ON person_order.order_date = person_visits.visit_date
LEFT JOIN person ON person_visits.person_id = person.id
ORDER BY
    action_date ASC,
    person_name DESC;
