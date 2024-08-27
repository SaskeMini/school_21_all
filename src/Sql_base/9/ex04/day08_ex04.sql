-- SESSION 1

BEGIN transaction isolation level serializable;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';

--SESSION 2

BEGIN transaction isolation level serializable;

UPDATE pizzeria
set rating = 3.0
WHERE name = 'Pizza Hut';

COMMIT;

SELECT * FROM pizzeria WHERE name = 'Pizza Hut';