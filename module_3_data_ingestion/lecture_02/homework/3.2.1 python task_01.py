category_a = "Vegetables"
category_b = "Fruits"
price_per_unit_a = 150
quantity_a = 40
vat_rate = 0.2

# Реализация обмена значений переменных без временной переменной
category_a, category_b = category_b, category_a
print("Текушая категория А:", category_a)
print("Текущая категория В:", category_b)

# Расчет стоимости партии с НДС
total_value = (price_per_unit_a * quantity_a) + (price_per_unit_a * quantity_a * vat_rate)
print("Общая стоимость партии с НДС:", total_value)
