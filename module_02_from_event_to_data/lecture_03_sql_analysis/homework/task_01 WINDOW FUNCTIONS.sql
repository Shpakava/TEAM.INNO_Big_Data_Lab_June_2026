Задача 1: Найти выручку всех магазинов в Германии по месяцам и разницу с предыдущим месяцем. Применить сортировку по месяцам по возрастанию.

WITH monthly_germany_revenue AS (
    -- Выручка по каждому месяцу для магазинов в Германии
    SELECT 
        TO_CHAR(s.sales_timestamp, 'YYYY-MM') AS sale_month,
        SUM(s.total_price) AS monthly_revenue
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN shops sh ON e.shop_id = sh.shop_id
    JOIN cities ci ON sh.city_id = ci.city_id
    JOIN countries co ON ci.country_id = co.country_id
    WHERE co.country_name = 'Germany' AND s.sales_timestamp IS NOT NULL
    GROUP BY 
        TO_CHAR(s.sales_timestamp, 'YYYY-MM')
)
-- Применение оконных функций к сгруппированным данным
SELECT 
    sale_month,
    ROUND(monthly_revenue, 2) AS monthly_revenue,
    COALESCE(ROUND(LAG(monthly_revenue) OVER (ORDER BY sale_month), 0), 0) AS previous_month_revenue,
    ROUND(monthly_revenue - COALESCE(LAG(monthly_revenue) OVER (ORDER BY sale_month), 0), 2) AS revenue_diff_vs_previous
FROM monthly_germany_revenue
ORDER BY sale_month
LIMIT 24;
