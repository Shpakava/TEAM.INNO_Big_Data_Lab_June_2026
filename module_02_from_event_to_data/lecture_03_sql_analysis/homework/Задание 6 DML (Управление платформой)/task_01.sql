Найти сотрудников с продажами > 1000.

SELECT DISTINCT
    e.employee_id,
    e.first_name,
    e.last_name
FROM 
    employees e
JOIN 
    sales s ON e.employee_id = s.employee_id
WHERE 
    s.total_price > 1000
ORDER BY 
    e.employee_id;