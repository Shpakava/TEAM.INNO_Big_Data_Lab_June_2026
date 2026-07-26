Обновить класс продуктов на 'A' для категорий с общей выручкой > 5000.

UPDATE products p
SET class = 'A'
FROM (
    SELECT 
        p.category_id, 
        SUM(s.total_price) as category_revenue
    FROM products p
    JOIN sales s ON p.product_id = s.product_id
    GROUP BY p.category_id
    HAVING SUM(s.total_price) > 5000
) AS cat_revenue
WHERE p.category_id = cat_revenue.category_id;