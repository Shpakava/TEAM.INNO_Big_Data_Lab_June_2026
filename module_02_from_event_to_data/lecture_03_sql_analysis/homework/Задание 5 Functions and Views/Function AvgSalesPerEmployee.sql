Функция: Создать функцию AvgSalesPerEmployee (PL/pgSQL), для вычисления средней суммы продаж для сотрудника.

CREATE FUNCTION AvgSalesPerEmployee(emp_id INT)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    avg_revenue DECIMAL(10, 2);
BEGIN
    SELECT COALESCE(AVG(total_price), 0.00)
    INTO avg_revenue
    FROM sales
    WHERE employee_id = emp_id;

    RETURN ROUND(avg_revenue, 2);
END;
$$ LANGUAGE plpgsql;