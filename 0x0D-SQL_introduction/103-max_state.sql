-- displays the max temperature of each state (ordered by State name)
USE hbtn_0c_0;
SET AUTOCOMMIT=0; 
SOURCE ./temperatures.sql;
COMMIT;
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
