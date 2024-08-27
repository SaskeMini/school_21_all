-- SESSION 1

BEGIN;

UPDATE pizzeria
set rating = 5 where name = 'DinoPizza';

UPDATE pizzeria
set rating = 1 where name = 'Pizza Hut';

COMMIT;

-- SESSION 2

BEGIN;

UPDATE pizzeria
set rating = 2 where name = 'Pizza Hut';

UPDATE pizzeria
set rating = 4 where name = 'DinoPizza';

COMMIT;
