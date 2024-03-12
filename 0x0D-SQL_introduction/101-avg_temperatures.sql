-- script that displays the average temperature
-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, avg(`value`) from temperatures ORDER BY `value` DESC;
