INSERT INTO person_order (id, person_id, menu_id, order_date) 
SELECT
        (generate_series(
                (SELECT MAX(id) + 1 FROM person_order),
                (SELECT MAX(id) + (SELECT COUNT(*) FROM person) FROM person_order)
        )),
        (generate_series(
                (SELECT MIN(id) FROM person),
                (SELECT MIN(id) + (SELECT COUNT(*) FROM person) - 1 FROM person)
        )),
        (SELECT id FROM menu WHERE pizza_name = 'greek pizza'),
        '2022-02-25'