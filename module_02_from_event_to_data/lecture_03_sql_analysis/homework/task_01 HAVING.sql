Задача 1: Вывести по каждому продукту сумму продаж и средний чек, где сумма продаж выше 400,000.00 . Также отсортируйте вывод по сумме продаж по убыванию.

SELECT p.product_name, ROUND(SUM(s.total_price), 2) AS total_revenue, ROUND(AVG(s.total_price), 2) AS avg_sale
FROM products p
JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING SUM(s.total_price) > 400000.00
ORDER BY total_revenue DESC
LIMIT 10;