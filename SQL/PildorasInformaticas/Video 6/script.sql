-- This gonna show the name, section, the price of the product and the price with the IVA.
SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO, PRECIO+(PRECIO*1.21) AS precio_con_IVA FROM productos;


-- This gonna show the name, section, the price of the product and the price with the IVA,
-- but rounded, with two decimals.
SELECT NOMBREARTÍCULO, SECCIÓN, PRECIO, ROUND(PRECIO+(PRECIO*1.21), 2) AS precio_con_IVA FROM productos