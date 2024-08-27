UPDATE menu
SET price = price - div(price, 10)
WHERE pizza_name = 'greek pizza'