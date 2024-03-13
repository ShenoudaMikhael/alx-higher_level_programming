-- script that displays the average temperature
-- Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS `avg_temp` FROM temperatures WHERE `month` >= 7 and `month` <= 8
GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;