Определение внешних ключей (FK)
1. cities:
• FK: country_id (ссылается на countries.country_id)
2. customers:
• FK: city_id (ссылается на cities.city_id)
3. employees:
• FK: city_id (ссылается на cities.city_id)
• FK: shop_id (ссылается на shops.shop_id)
4. products:
• FK: category_id (ссылается на categories.category_id)
5. sales:
• FK: employee_id (ссылается на employees.employee_id)
• FK: customer_id (ссылается на customers.customer_id)
• FK: product_id (ссылается на products.product_id)
6. shops:
• FK: city_id (ссылается на cities.city_id)