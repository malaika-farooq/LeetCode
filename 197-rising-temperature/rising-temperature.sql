# Write your MySQL query statement below
SELECT curr.id
FROM Weather curr
join Weather tom
on curr.recordDate = DATE_ADD(tom.recordDate, Interval 1 DAY)
where curr.temperature > tom.temperature 