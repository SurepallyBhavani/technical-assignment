//query 1
SELECT COUNT(DISTINCT species) as Types_of_Acacia_Plants
FROM taxonomy
WHERE species LIKE 'Acacia%';

//query 2
SELECT
    t.species as Wheat_Type,
    r.length as DNA_Sequence_Length
FROM taxonomy AS t
JOIN rfamseq AS r
    ON t.ncbi_id = r.ncbi_id
WHERE t.species LIKE '%wheat%'
ORDER BY r.length DESC
LIMIT 1;

