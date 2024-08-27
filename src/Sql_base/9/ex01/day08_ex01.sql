-- SESSION 1

SHOW transaction isolation level;

BEGIN transaction isolation level read committed;

UPDATE pizzeria
set rating = 4
WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

--SESSION 2

BEGIN transaction isolation level read committed;

UPDATE pizzeria
set rating = 3.6
WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';