BEGIN;

UPDATE pizzeria
set rating = 5
WHERE name = 'Pizza Hut';

SELECT * FROM pizzeria
WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria
WHERE name = 'Pizza Hut';