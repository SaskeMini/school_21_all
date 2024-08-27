-- CREATE FUNCTION fnc_person_visits_and_eats_on_date(pperson varchar default 'Dmitriy', pprice numeric default 500, pdate date default '2022-01-08')
-- RETURNS TABLE(name varchar) AS $$
-- BEGIN
-- RETURN QUERY
--     SELECT pizzeria.name AS pizzeria_name FROM pizzeria
--         INNER JOIN person_visits ON person_visits.pizzeria_id = pizzeria.id
--         INNER JOIN person ON person.id = person_visits.person_id
--         INNER JOIN menu ON menu.pizzeria_id = pizzeria.id
--     WHERE menu.price < pprice and person.name = pperson and person_visits.visit_date = pdate;
-- END;
-- $$ LANGUAGE PLPGSQL;

select *
from fnc_person_visits_and_eats_on_date(pprice := 800);

select *
from fnc_person_visits_and_eats_on_date(pperson := 'Anna',pprice := 1300,pdate := '2022-01-01');