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

//query 3
-- Q3: Family name, accession and maximum DNA sequence length
-- Page 9 with 15 results per page (rows 121-135)

SELECT
    f.rfam_acc AS family_accession,
    f.rfam_id AS family_name,
    x.max_sequence_length
FROM family AS f
JOIN (
    SELECT
        fr.rfam_acc,
        MAX(r.length) AS max_sequence_length
    FROM full_region AS fr
    JOIN rfamseq AS r
        ON fr.rfamseq_acc = r.rfamseq_acc
    GROUP BY fr.rfam_acc
    HAVING MAX(r.length) > 1000000
) AS x
    ON f.rfam_acc = x.rfam_acc
ORDER BY x.max_sequence_length DESC
LIMIT 15 OFFSET 120;