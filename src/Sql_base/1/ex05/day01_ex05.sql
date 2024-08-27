SELECT * FROM person AS per (person_id, person_name, age, gender, address), pizzeria AS pizz (pizzeria_id, pizzeria_name, rating)
ORDER BY
    person_id,
    pizzeria_id