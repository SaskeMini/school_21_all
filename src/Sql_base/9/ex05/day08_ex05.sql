-- SESSION 1

BEGIN transaction isolation level read committed;

SELECT SUM(rating) FROM pizzeria;

SELECT SUM(rating) FROM pizzeria;

COMMIT;

SELECT SUM(rating) FROM pizzeria;

--SESSION 2

BEGIN transaction isolation level read committed;

INSERT INTO pizzeria (id, name, rating)
VALUES (10, 'Kazan Pizza', 5);

COMMIT;

SELECT SUM(rating) FROM pizzeria;