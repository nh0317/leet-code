# Write your MySQL query statement below
select distinct product_id, product_name
from Product
where product_id not in (
    select product_id
    from Sales
    where (timediff(sale_date, '2019-04-01') > 0 
            or timediff(sale_date, '2019-01-01') < 0)
) and product_id not in (
    select p.product_id
    from Product p left join Sales s on p.product_id = s.product_id
    where s.sale_date is null
)