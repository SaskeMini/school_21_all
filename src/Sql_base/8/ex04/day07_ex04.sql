SELECT person.name AS name, COUNT(person_visits.person_id) AS count_of_visits FROM person_visits
INNER JOIN person ON person.id = person_visits.person_id
GROUP BY name, person_visits.person_id
HAVING COUNT(*) > 3