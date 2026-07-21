Задача 1: Вывести все магазины, расположенные в 'Poland'. Необходимые колонки: shop_id, address, city_name, country_name.

SELECT sh.shop_id, sh.address, ci.city_name, co.country_name
FROM shops sh
JOIN cities ci ON sh.city_id = ci.city_id
JOIN countries co ON ci.country_id = co.country_id
WHERE co.country_name = 'Poland';
