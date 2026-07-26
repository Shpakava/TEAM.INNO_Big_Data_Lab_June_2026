Удалить всех сотрудников без продаж.

DELETE FROM employees
WHERE employee_id NOT IN (SELECT DISTINCT employee_id FROM sales);