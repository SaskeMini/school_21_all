-- SESSION 1

BEGIN transaction isolation level repeatable read;

SELECT SUM(rating) FROM pizzeria;

SELECT SUM(rating) FROM pizzeria;

COMMIT;

SELECT SUM(rating) FROM pizzeria;

--SESSION 2

BEGIN transaction isolation level repeatable read;

INSERT INTO pizzeria (id, name, rating)
VALUES (11, 'Kazan Pizza 2', 4);

COMMIT;

SELECT SUM(rating) FROM pizzeria;