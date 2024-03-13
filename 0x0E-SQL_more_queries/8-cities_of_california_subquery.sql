-- cript that lists all the cities
-- a script that lists all the cities of California that can be found in the database 
SELECT * from cities where state_id = (SELECT id from states where name = 'California');
