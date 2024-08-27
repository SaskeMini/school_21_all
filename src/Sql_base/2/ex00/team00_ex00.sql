CREATE TABLE IF NOT EXISTS paths (
    point1 varchar, point2 varchar, cost numeric
);

INSERT INTO paths VALUES
('a', 'b', 10),
('a', 'c', 15),
('a', 'd', 20),

('b', 'a', 10),
('b', 'c', 35),
('b', 'd', 25),

('c', 'a', 15),
('c', 'b', 35),
('c', 'd', 30),

('d', 'a', 20),
('d', 'b', 25),
('d', 'c', 30);

WITH all_in AS (
    WITH recursive recur AS
    (SELECT point1, point2, cost, 1 AS level, array[point1] AS road, FALSE AS checks, array[cost] AS costs
    FROM paths
    WHERE point1 = 'a'

    UNION ALL

    SELECT paths.point1, paths.point2, paths.cost + recur.cost AS cost, recur.level + 1 AS level, recur.road || paths.point1 AS road,
     paths.point1 = ANY (recur.road) AS checks, recur.costs || paths.cost AS costs
    FROM paths INNER JOIN recur ON recur.point2 = paths.point1 AND NOT checks
    )
    SELECT
        cost - costs[5] AS total_cost,
        road
    FROM recur
    WHERE level = 5 AND 'a' = ANY(road) AND 'b' = ANY(road) AND 'c' = ANY(road) AND 'd' = ANY(road) AND road[1] = road[5]
    ORDER BY cost, road)

SELECT distinct * FROM all_in
WHERE total_cost = (SELECT MIN(total_cost) FROM all_in)
ORDER BY 1,2