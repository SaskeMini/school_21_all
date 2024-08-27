-- CREATE UNIQUE INDEX idx_menu_unique ON menu (pizzeria_id, pizza_name);
SET enable_seqscan = off;
EXPLAIN ANALYZE
SELECT * FROM menu
WHERE pizza_name = 'pepperoni pizza' AND pizzeria_id = 6;