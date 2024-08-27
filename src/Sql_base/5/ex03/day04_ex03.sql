SELECT generated_date AS missing_date FROM v_generated_dates
LEFT JOIN person_visits ON person_visits.visit_date = v_generated_dates.generated_date AND person_visits.visit_date >= '2022-01-01' AND person_visits.visit_date <= '2022-01-31'
WHERE person_visits.visit_date IS NULL