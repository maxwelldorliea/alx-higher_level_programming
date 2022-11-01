-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
USE test;
SET AUTOCOMMIT=0; 
SOURCE ./temperatures.sql;
COMMIT;
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
