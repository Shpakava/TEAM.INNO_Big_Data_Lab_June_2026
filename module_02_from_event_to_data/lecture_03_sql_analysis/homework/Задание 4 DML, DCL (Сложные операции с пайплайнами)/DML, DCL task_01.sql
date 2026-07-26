Увеличить цену всех продуктов категории 'Fruits' на 10%.

UPDATE products p
SET price = p.price * 1.10
FROM categories c
WHERE p.category_id = c.category_id AND c.category_name = 'Fruits';