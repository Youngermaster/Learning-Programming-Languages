-- This will return the sum of the price on each section column
SELECT SECCIÓN, SUM(PRECIO) FROM PRODUCTOS 
    GROUP BY SECCIÓN;


-- This will return the sum of the price on each section column in order.
SELECT SECCIÓN, SUM(PRECIO) AS sum_prices FROM PRODUCTOS 
    GROUP BY SECCIÓN
    ORDER BY sum_prices;