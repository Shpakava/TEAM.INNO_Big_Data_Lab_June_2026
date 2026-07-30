# Входные данные
prices = [100, -50, 300, 40, 800]

# Работа со списками
for num in prices:
    if num < 0:
        prices.remove(num)
prices.append(150)
prices.sort()
tax_prices = [price * 1.2 for price in prices]
tax_prices_new = []
for num in tax_prices:
    if num > 100:
        tax_prices_new.append(num)

# Результат
print(f"Базовый прайс (очищенный): {prices}")
print(f"Цены с НДС (>100): {tax_prices_new}")
print(f"Общая выручка: {sum(tax_prices_new)}")
print(f"Минимум: {min(tax_prices_new)}")
print(f"Максимум: {max(tax_prices_new)}")