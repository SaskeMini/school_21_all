SELECT person_order.order_date AS order_date, person.name || ' (age:' || person.age || ')' AS person_information
FROM person_order AS person_order (xz_id, id, menu_id, order_date)
NATURAL JOIN person
ORDER BY order_date, person_information ASC;