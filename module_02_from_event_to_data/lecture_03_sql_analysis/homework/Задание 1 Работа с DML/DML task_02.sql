Выбрать только Продукты (Products), у которых is_allergic и resistant = 'Yes'.

SELECT 
    product_id,
    product_name,
    is_allergic,
    resistant
FROM 
    products
WHERE 
    is_allergic = 'Yes' AND resistant = 'Yes';