--Query 2A.
--Write an SQL query to determine how many types of Acacia plants are present in the taxonomy table.
--Return the result as a clearly named column.

SELECT COUNT(DISTINCT species) AS acacia_type_count
FROM taxonomy
WHERE species LIKE 'Acacia%';



--Query 2B
--Write an SQL query to determine which type of wheat has the longest DNA sequence.
--Use the appropriate information from the rfamseq and taxonomy tables.
--Return the relevant wheat type and its DNA sequence length.

SELECT
    t.species as wheat_type,
    r.length as dna_sequence_length
FROM taxonomy AS t
JOIN rfamseq AS r
    ON t.ncbi_id = r.ncbi_id
WHERE t.species LIKE '%wheat%'
ORDER BY r.length DESC
LIMIT 1;



-- Query 2C: 
--Family name, accession and maximum DNA sequence length
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