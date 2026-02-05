/* Write your T-SQL query statement below */
SELECT Employee.name, bonus
from Employee
left join Bonus on Employee.empid =  Bonus.empid 
where bonus is NULL or bonus < 1000