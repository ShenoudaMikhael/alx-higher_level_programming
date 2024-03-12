-- select same score i
-- cript that lists the number of records with the same score in the table second_table
SELECT DISTINCT `score`,count(id) as number FROM second_table GROUP BY score ORDER BY score DESC;
