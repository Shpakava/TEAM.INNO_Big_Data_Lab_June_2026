from typing import Optional, Union

def calculate_total_delivery_cost(product_name: str,
                                  weights: Union[list[Union[int, float]], tuple[Union[int, float]]],
                                  prices: Union[list[Union[int, float]], tuple[Union[int, float]]], 
                                  discount: Optional[float] = None, 
                                  currency_rate: Union[int, float] = 1, 
                                  *extra_costs: Union[int, float]) -> dict[str, float]:
    """ 
    Функция для расчета итоговой стоимости партии товара с учетом базовых цен, скидки и дополнительных расходов.
    :param product_name: Название товара
    :param weights: Коллекция с весами партий
    :param prices: Коллекция с ценами за 1 кг
    :param discount: Скидка, которой по умолчанию нет, но может быть передана в функцию
    :param currency_rate: Коэффициент пересчета валюты. По умолчанию всегда равен 1.
    :param *extra_costs: Дополнительные расходы (доставка, упаковка, хранение)
    """
    if len(weights) != len(prices):
        raise ValueError("Количество элементов в weights и prices должно совпадать.")

    # Локальные переменные с явной типизацией
    total_sum: int = 0
    for i in range(len(weights)):
        total_sum += weights[i] * prices[i]

    discount_sum: float = total_sum
    if discount is not None:
        discount_sum = total_sum * (1 - discount)

    extra_sum: float = float(sum(extra_costs))
    final_sum: float = (discount_sum + extra_sum) * currency_rate

    return {product_name: final_sum}


# 1. Овощная партия
veg_result: dict[str, float] = calculate_total_delivery_cost("Овощная партия", [100, 50], [4, 6], 0.1, 1, 20, 15)

for name, cost in veg_result.items():
    print(f"Товар: {name}, итоговая стоимость: {cost}")

# 2. Фруктовая партия
fruit_result: dict[str, float] = calculate_total_delivery_cost("Фруктовая партия", (30, 20, 10), (15, 12, 18), None, 1.2, 25)

for name, cost in fruit_result.items():
    print(f"Товар: {name}, итоговая стоимость: {cost}")
