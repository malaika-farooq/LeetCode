/* Write your T-SQL query statement below */
SELECT A1.machine_id, ROUND(AVG(A2.timestamp - A1.timestamp), 3) as processing_time
-- A1.machine_id, A2.machine_id, A1.process_id, A2.process_id, A1.activity_type, A2.activity_type, A1.timestamp, A2.timestamp 
from Activity A1
Join Activity A2 on A1.process_id = A2.process_id and A1.machine_id = A2.machine_id and A1.activity_type  = 'start' and A2.activity_type = 'end'
GROUP BY A1.machine_id
