# Write your MySQL query statement below
select u.name, 
    (case
        when r.distance is null then 0
        else sum(r.distance)
    end
 )as travelled_distance 
from Users u left join Rides r on u.id = r.user_id
group by u.id
order by travelled_distance desc, name asc
# (
#     case
#         when count(distance) >= 2 then name
#         else distance
#     end
# )