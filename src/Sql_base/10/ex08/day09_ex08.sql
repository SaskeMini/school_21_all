-- CREATE FUNCTION fnc_fibonacci(pstop integer default 10)
-- RETURNS TABLE(one bigint) AS $$
-- WITH RECURSIVE recur (one, two) AS
-- (SELECT 0 AS one, 1 AS two
-- UNION ALL
-- SELECT two, one + two FROM recur WHERE two < pstop)
-- SELECT one FROM recur;
-- $$ LANGUAGE SQL;

select * from fnc_fibonacci(100);
select * from fnc_fibonacci();
