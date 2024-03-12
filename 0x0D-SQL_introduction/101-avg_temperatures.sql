-- script that displays the average temperature
-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(`value`) as `avg_temp` from temperatures ORDER BY `avg_temp` DESC;
