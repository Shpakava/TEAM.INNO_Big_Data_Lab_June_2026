Представление (View): Создать представление FullStatShops для суммарной статистики по магазинам с колонками (shop_id, shop_address, country, total_sales_count, total_sales_amount).

CREATE VIEW FullStatShops AS
SELECT 
    sh.shop_id,
    sh.shop_address,
    co.country_name AS country,
    COALESCE(COUNT(s.sales_id), 0) AS total_sales_count,
    COALESCE(ROUND(SUM(s.total_price), 2), 0.00) AS total_sales_amount
FROM 
    shops sh
JOIN 
    cities ci ON sh.city_id = ci.city_id
JOIN 
    countries co ON ci.country_id = co.country_id
LEFT JOIN 
    employees e ON sh.shop_id = e.shop_id
LEFT JOIN 
    sales s ON e.employee_id = s.employee_id
GROUP BY 
    sh.shop_id,
    sh.shop_address,
    co.country_name;