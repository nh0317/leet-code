# Write your MySQL query statement below

select id,
case 
    when id % 2 = 0 then Lag(student) over (order by id) 
    else Lead(student, 1, student) over (order by id) 
end as student
from Seat
order by id asc
