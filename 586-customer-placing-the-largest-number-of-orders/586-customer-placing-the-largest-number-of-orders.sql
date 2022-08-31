# Write your MySQL query statement below
select customer_number
from Orders
group by customer_number
having count(customer_number) = (
    select max(cnt)
    from (select count(*) as cnt from Orders group by customer_number) t
)