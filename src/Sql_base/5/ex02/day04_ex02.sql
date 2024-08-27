CREATE VIEW v_generated_dates AS
SELECT dd.day::date AS generated_date
FROM generate_series(timestamp '2022-01-01', timestamp '2022-01-31', interval '1 day') AS dd(day)
ORDER BY generated_date;