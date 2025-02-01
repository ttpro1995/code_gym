-- Create the schema if it does not exist
CREATE SCHEMA IF NOT EXISTS leet_601;

-- Create the Stadium table within the leet_601 schema
CREATE TABLE leet_601.Stadium (
    id INT,
    visit_date DATE,
    people INT
);

-- Insert the example data into the Stadium table within the leet_601 schema
INSERT INTO leet_601.Stadium (id, visit_date, people) VALUES
(1, '2017-01-01', 10),
(2, '2017-01-02', 109),
(3, '2017-01-03', 150),
(4, '2017-01-04', 99),
(5, '2017-01-05', 145),
(6, '2017-01-06', 1455),
(7, '2017-01-07', 199),
(8, '2017-01-09', 188);


-- more example
-- Insert additional data into the Stadium table within the leet_601 schema
INSERT INTO leet_601.Stadium (id, visit_date, people) VALUES
(31, '2017-02-01', 50),
(32, '2017-02-05', 150),
(33, '2017-02-03', 75),
(34, '2017-02-08', 100),
(35, '2017-02-02', 25),
(36, '2017-02-07', 175),
(37, '2017-02-04', 125),
(38, '2017-02-06', 180),
(39, '2017-02-10', 30),
(40, '2017-02-09', 90),
(41, '2017-02-12', 60),
(42, '2017-02-11', 110),
(43, '2017-02-15', 40),
(44, '2017-02-14', 140),
(45, '2017-02-13', 80),
(46, '2017-02-17', 160),
(47, '2017-02-16', 130),
(48, '2017-02-19', 190),
(49, '2017-02-18', 10),
(50, '2017-02-20', 200);


INSERT INTO leet_601.Stadium (id, visit_date, people) VALUES
(90, '2017-05-01', 50),
(95, '2017-05-05', 150),
(91, '2017-05-03', 75);


INSERT INTO leet_601.Stadium (id, visit_date, people) VALUES
(85, '2017-06-01', 150),
(88, '2017-06-05', 150),
(97, '2017-06-03', 175);

----
-- let make a example table to evaluate row_number over partition 
CREATE TABLE leet_601.StadiumWithClass (
    id INT,
    visit_date DATE,
    people INT,
    zlass varchar(10)
);

-- Insert the example data into the Stadium table within the leet_601 schema
INSERT INTO leet_601.StadiumWithClass (id, visit_date, people, zlass) VALUES
(1, '2017-01-01', 10, 'A'),
(2, '2017-01-02', 109, 'A'),
(3, '2017-01-03', 150, 'A'),
(4, '2017-01-04', 99, 'B'),
(5, '2017-01-05', 145, 'B'),
(6, '2017-01-06', 1455, 'C'),
(7, '2017-01-07', 199, 'C'),
(8, '2017-01-09', 188, 'C');

SELECT
    id,
    visit_date,
    people,
    row_number() over (order by id) as row_num 
FROM
    StadiumWithClass
    
    
SELECT
    id,
    visit_date,
    people,
    zlass,
    row_number() over (partition by zlass order by id) as row_num 
FROM
    StadiumWithClass

    
    
 SELECT
    id,
    visit_date,
    people,
    zlass,
    id - row_number() over (partition by zlass order by id) as row_num 
FROM
    StadiumWithClass

------------------------------------------------------------------------------------
-- anwser 

--Table: Stadium
--
--+---------------+---------+
--| Column Name   | Type    |
--+---------------+---------+
--| id            | int     |
--| visit_date    | date    |
--| people        | int     |
--+---------------+---------+
--visit_date is the column with unique values for this table.
--Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
--As the id increases, the date increases as well.
--
-- 
--
--Write a solution to display the records with three or more rows with consecutive id's, and the number of people is greater than or equal to 100 for each.
--
--Return the result table ordered by visit_date in ascending order.
--
--The result format is in the following example.



select * 
from stadium s ;


select id, visit_date , people 
from stadium s 
where people > 100 
order by visit_date ;



SELECT
    id,
    visit_date,
    people,
    row_number() over (order by id) as row_num 
FROM
    stadium
WHERE
    people > 100
order by 
	visit_date;
   
   
with group_table as (
	SELECT
	    id,
	    visit_date,
	    people,
	    id - ROW_NUMBER() OVER (ORDER BY id) AS grp
	FROM
	    stadium
	WHERE
	    people > 100
) 
select * 
from group_table
    
        

WITH group_table AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM
        stadium
    WHERE
        people > 100
),
triple_group as (
	select 
        grp
	from 
		group_table
	group by grp 
	having count(*) > 2
)
select gt.id, gt.visit_date, gt.people, gt.grp
from group_table gt
where gt.grp in (select tg.grp from triple_group tg)

------

SELECT
    id,
    visit_date,
    people,
    id - ROW_NUMBER() OVER (ORDER BY visit_date) AS grp
FROM
    stadium
WHERE
    people > 100
        

    
    ---------------------
----------- answer 1 - 14/15 test case 
        
WITH group_table AS (
	SELECT
	    id,
	    visit_date,
	    people,
	    id - ROW_NUMBER() OVER (ORDER BY visit_date) AS grp
	FROM
	    stadium
	WHERE
	    people >= 100
),
triple_group as (
	select 
        grp
	from 
		group_table
	group by grp 
	having count(*) > 2
)
select gt.id, gt.visit_date, gt.people, gt.grp
from group_table gt
where gt.grp in (select tg.grp from triple_group tg)
        
        
-------------------------------
-- Optimize by mistral 
-- 21 % time
WITH group_table AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY visit_date) AS grp
    FROM
        stadium
    WHERE
        people >= 100
),
triple_group AS (
    SELECT
        grp
    FROM
        group_table
    GROUP BY
        grp
    HAVING
        COUNT(*) > 2
)
SELECT
    gt.id,
    gt.visit_date,
    gt.people,
    gt.grp
FROM
    group_table gt
JOIN
    triple_group tg
ON
    gt.grp = tg.grp;
---
   
WITH group_table AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY visit_date) AS grp
    FROM
        stadium
    WHERE
        people >= 100
),
triple_group AS (
    SELECT
        grp
    FROM
        group_table
    GROUP BY
        grp
    HAVING
        COUNT(*) >= 3  -- Changed to >=3 for clarity (matches "more than 2")
)
SELECT
    gt.id,
    gt.visit_date,
    gt.people
FROM
    group_table gt
JOIN
    triple_group tg
ON
    gt.grp = tg.grp
ORDER BY
    gt.visit_date;  -- Optional, for ordered results


