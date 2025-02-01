-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/


--+----------------+---------+
--| Column Name    | Type    |
--+----------------+---------+
--| requester_id   | int     |
--| accepter_id    | int     |
--| accept_date    | date    |
--+----------------+---------+
--(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
--This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.


CREATE TABLE RequestAccepted(
	requester_id INT,
	accepter_id INT, 
	accept_date DATE
)



--Input: 
--RequestAccepted table:
--+--------------+-------------+-------------+
--| requester_id | accepter_id | accept_date |
--+--------------+-------------+-------------+
--| 1            | 2           | 2016/06/03  |
--| 1            | 3           | 2016/06/08  |
--| 2            | 3           | 2016/06/08  |
--| 3            | 4           | 2016/06/09  |
--+--------------+-------------+-------------+


insert into RequestAccepted (requester_id, accepter_id, accept_date) 
values 
(1,2,'2016/06/03'),
(1,3,'2016/06/08'),
(2,3,'2016/06/08'),
(3,4,'2016/06/09');



select * 
from requestaccepted r ;


select  
requester_id as id,
count(1) as req_count 
from requestaccepted r 
group by requester_id ;

select  
accepter_id as id,
count(1) as req_count 
from requestaccepted r 
group by accepter_id ;


with count_req as (
	select  
	requester_id as id,
	count(1) as req_count 
	from requestaccepted r 
	group by requester_id 
), 
count_accept as (
	select  
	accepter_id as id,
	count(1) as acc_count 
	from requestaccepted r 
	group by accepter_id 
)
select 
rq.id, 
rq.req_count, 
ac.acc_count,
(rq.req_count + ac.acc_count) as friend_count
from count_req rq
join count_accept as ac on ac.id = rq.id ;

----


with count_req as (
	select  
	requester_id as id,
	count(1) as req_count 
	from requestaccepted r 
	group by requester_id 
), 
count_accept as (
	select  
	accepter_id as id,
	count(1) as acc_count 
	from requestaccepted r 
	group by accepter_id 
), friend_count_table as (
	select 
	rq.id, 
	rq.req_count, 
	ac.acc_count,
	(rq.req_count + ac.acc_count) as friend_count
	from count_req rq
	join count_accept as ac on ac.id = rq.id 
) 
select id, friend_count as num
from friend_count_table fc
order by fc.friend_count DESC
limit 1;



with count_req as (
	select  
	requester_id as id,
	count(1) as req_count 
	from requestaccepted r 
	group by requester_id 
), 
count_accept as (
	select  
	accepter_id as id,
	count(1) as acc_count 
	from requestaccepted r 
	group by accepter_id 
), friend_count_table as (
	select 
	rq.id, 
	coalesce (rq.req_count,0) as req_count, 
	coalesce (ac.acc_count,0) as acc_count,
	(coalesce (rq.req_count,0) + coalesce (ac.acc_count,0)) as friend_count
	from count_req rq
	full outer join count_accept as ac on ac.id = rq.id 
) 
select id, friend_count as num
from friend_count_table fc
order by fc.friend_count DESC
limit 1;

----
--correct

with count_req as (
	select  
	requester_id as id,
	count(1) as req_count 
	from requestaccepted r 
	group by requester_id 
), 
count_accept as (
	select  
	accepter_id as id,
	count(1) as acc_count 
	from requestaccepted r 
	group by accepter_id 
), friend_count_table as (
	select 
	coalesce (rq.id, ac.id) as id, 
	coalesce (rq.req_count,0) as req_count, 
	coalesce (ac.acc_count,0) as acc_count,
	(coalesce (rq.req_count,0) + coalesce (ac.acc_count,0)) as friend_count
	from count_req rq
	full outer join count_accept as ac on ac.id = rq.id 
) 
select id, friend_count as num
from friend_count_table fc
order by fc.friend_count DESC
limit 1;


