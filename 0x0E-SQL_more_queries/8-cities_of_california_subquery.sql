-- Script to list all cities of California using subquery
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
