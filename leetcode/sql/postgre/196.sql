
CREATE TABLE leet_196.Person (
    id INT,
    email VARCHAR(256)
);


INSERT INTO leet_196.Person (id, email) VALUES
(1, 'aaaa'),
(2, 'bbbbb'),
(3, 'aaaaa'),
(4, 'acccc');



INSERT INTO leet_196.Person (id, email) VALUES
(1, 'john@example.com'),
(2, 'bob@example.com'),
(3, 'john@example.com');


----

select 
	p.id, 
	p.email
from person p;



with email_group as (
	select 
		p.id, 
		p.email,
		row_number() over (partition by email order by id) as id_count  
	from person p
) 
select g.id, g.email
from email_group g
where id_count > 1;


with email_group as (
	select 
		p.id, 
		p.email,
		row_number() over (partition by email order by id) as id_count  
	from person p
)
delete from Person 
using email_group g 
where person.id = g.id 
and id_count > 1;




with email_group as (
	select 
		p.id, 
		p.email,
		row_number() over (partition by email order by id) as id_count  
	from person p
)
delete from Person 
where Person.id = email_group.id 
and id_count > 1;

