# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e left join Department d on e.departmentId = d.id
WHERE(departmentId, salary) IN
(SELECT departmentId,MAX(salary) FROM Employee GROUP BY departmentId) ;