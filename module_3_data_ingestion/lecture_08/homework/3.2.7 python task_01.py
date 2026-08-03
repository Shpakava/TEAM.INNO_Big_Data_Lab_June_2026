SMALL_BATCH_LIMIT = 500

def calculate_batch(weight, price, discount=0.0):
    """ 
	Функция для расчета стоимости партии товара и автоматического определения, превышен ли лимит мелких покупок.
	:param weight: Вес партии в кг
	:param price: Цена за 1 кг
    :param discounts: Сезонная скидка (по умолчанию равна 0.0)
	"""
    final_sum = weight * price * (1 - discount)
    is_limit_exceeded = False
    if final_sum > SMALL_BATCH_LIMIT:
        is_limit_exceeded = True
    return final_sum, is_limit_exceeded

sum_carrots, is_exceeded_carrots = calculate_batch(100, 4)
print(f"Партия 1 (Морковь): Сумма {sum_carrots}. Превышение лимита: {is_exceeded_carrots}")

sum_apples, is_exceeded_apples = calculate_batch(50, 20, 0.10)
print(f"Партия 2 (Яблоки): Сумма {sum_apples}. Превышение лимита: {is_exceeded_apples}")
