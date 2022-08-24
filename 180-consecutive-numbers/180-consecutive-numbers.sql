# Write your MySQL query statement below
select distinct a.num as ConsecutiveNums 
from Logs a  join Logs b on a.id = b.id+1  join Logs c on a.id = c.id-1
where a.num = b.num and a.num = c.num
