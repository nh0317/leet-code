# Write your MySQL query statement below
select salesperson.name from salesperson 
where salesperson.sales_id not in 
(select orders.sales_id 
 from orders inner join company 
on company.com_id=orders.com_id 
 where company.name='red');