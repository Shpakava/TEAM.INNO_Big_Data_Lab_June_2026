# Входные данные
products = ["Яблоки", "Хлеб", "Молоко", "Печенье", "Сок", "Кефир"]

for product in range(0, len(products), 2):
    print(f"Индекс {product}: Проверен товар {products[product]} (Длина названия: {len(products[product])} символов)")
    if products[product] == "Бананы":
        print("Обнаружены Бананы. Проверка прервана")
        break
else:
    print("--- Выборочная проверка успешно завершена ---")
