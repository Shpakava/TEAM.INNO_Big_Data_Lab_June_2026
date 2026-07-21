Для каждого магазина рассчитать агрегаты продаж и аналитические показатели в разрезе страны.
Для каждого магазина посчитать:
количество продаж (COUNT(sales_id))
общую сумму продаж (SUM(total_price))
Оставить только магазины, у которых не менее 2 продаж.
Для каждого такого магазина рассчитать:
долю оборота магазина от общего оборота страны
ранг магазина по сумме продаж внутри своей страны
накопительный оборот по стране,
отсортированный по убыванию оборота магазина
Отсортировать результат:
по стране
по рангу магазина

WITH filtered_shops AS (
    -- Агрегация продаж по магазинам и только те, где >= 2 продаж
    SELECT 
        co.country_name AS country,
        co.country_id, 
        sh.shop_id,
        sh.address AS shop_address,
        COUNT(s.sales_id) AS total_sales_count,
        SUM(s.total_price) AS total_sales_amount
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN shops sh ON e.shop_id = sh.shop_id
    JOIN cities ci ON sh.city_id = ci.city_id
    JOIN countries co ON ci.country_id = co.country_id
    GROUP BY 
        co.country_name,
        co.country_id,
        sh.shop_id,
        sh.address
    HAVING COUNT(s.sales_id) >= 2
),
raw_analytics AS (
    -- Оконные функции
    SELECT 
        country,
        shop_id,
        shop_address,
        total_sales_count,
        total_sales_amount,
        SUM(total_sales_amount) OVER (PARTITION BY country_id) AS country_total_raw,
        DENSE_RANK() OVER (PARTITION BY country_id ORDER BY total_sales_amount DESC) AS rang,
        SUM(total_sales_amount) OVER (PARTITION BY country_id ORDER BY total_sales_amount DESC) AS country_running_total_raw
    FROM 
        filtered_shops
)
-- Финальные расчеты
SELECT 
    country,
    shop_id,
    shop_address,
    total_sales_count,
    ROUND(total_sales_amount, 2) AS total_sales_amount,
    ROUND(country_total_raw, 2) AS country_total,
    ROUND((total_sales_amount / country_total_raw) * 100, 2) AS country_sales_share,
    rang,
    ROUND(country_running_total_raw, 2) AS country_running_total
FROM raw_analytics
ORDER BY country, rang
LIMIT 22;