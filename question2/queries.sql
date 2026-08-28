//query 1
SELECT COUNT(DISTINCT species) as Types_of_Acacia_Plants
FROM taxonomy
WHERE species LIKE 'Acacia%';

