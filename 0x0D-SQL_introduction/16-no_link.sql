-- this is a script to create a database if missing
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
