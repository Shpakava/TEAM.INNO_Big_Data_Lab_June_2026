def calculate_purchase(product_name, weight, price):
    """ 
    Функция для расчета стоимости партии товара и индекса распределения.
    :param product_name: Название товара
    :param weight: Вес партии в кг
    :param price: Цена за 1 кг
    """
    try:
        numeric_weight = float(weight)
        total_cost = numeric_weight * price
        technical_index = 100 / numeric_weight
        print(f"Товар: {product_name}. Итоговая стоимость: {total_cost}$")

    except TypeError as e: 
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
    
    except ValueError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
    
    except ZeroDivisionError as e:
        print(f"Тип ошибки: {type(e)}")
        print(f"Сообщение: {e}")
    
    finally:
        print(f"--- Проверка партии завершена ---")


# Корректный случай
calculate_purchase("Томаты", 100, 2.5)

# Ошибка ValueError
calculate_purchase("Огурцы", "пятьдесят", 1.8)

# Ошибка ZeroDivisionError
calculate_purchase("Перец", 0, 4)

# Ошибка TypeError
calculate_purchase("Зелень", [10], 5)
