-- SESSION 1

BEGIN transaction isolation level repeatable read;

UPDATE pizzeria
set rating = 4
WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

--SESSION 2

BEGIN transaction isolation level repeatable read;

UPDATE pizzeria
set rating = 3.6
WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';