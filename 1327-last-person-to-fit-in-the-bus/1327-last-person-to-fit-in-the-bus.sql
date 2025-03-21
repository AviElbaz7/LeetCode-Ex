WITH bus as (
    SELECT person_name, turn, sum(weight) over(order by turn) as total_weight
    FROM Queue
)

select person_name
from bus
where total_weight <= 1000
order by total_weight desc
limit 1