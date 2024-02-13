-- Count records for each score and list in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
