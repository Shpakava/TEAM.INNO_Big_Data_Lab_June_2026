# Входные данные
raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "

# Преобразование строк
order_id = raw_log.split("|")[0]
product_code = raw_log.split("|")[1]
raw_phone = raw_log.split("|")[2]
raw_city = raw_log.split("|")[3]
category = product_code[:3]
region = product_code[-2:]
position_first = product_code.find("-")
clean_phone = ""
for num in raw_phone:
	if num.isdigit():
		clean_phone += num
city = raw_city.strip().lower().title()

# Итоговый отчет
print(f"Позиция первого дефиса в коде товара: {position_first}")
if product_code.startswith("FRT"): 
	print("Код товара начинается с 'FRT'")
else:
	print("Код товара не начинается с 'FRT'")
print(f"Длина номера телефона: {len(clean_phone)}")
print(f"Заказ: {order_id} \nКатегория: {category} | Регион: {region} \nТелефон: {clean_phone} \nГород: {city}")