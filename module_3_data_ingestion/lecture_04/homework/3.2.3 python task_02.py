# Входные данные. Список списков
daily_logs = [
    [500, 0, 1200],       # Касса 1 (Нормальная)
    [300, -999, 800],     # Касса 2 (Сломалась посередине, 800 не должно посчитаться)
    [1500, 200]           # Касса 3 (Нормальная)
]

total_revenue = 0
for index, daily_log in enumerate(daily_logs, start=1):
    print(f"--- Обработка Кассы {index} ---")
    for transaction in daily_log:
        if transaction == -999:
            print("Аварийная остановка кассы!")
            break
        elif transaction == 0:
            print("Сбой(0)")
            continue
        elif transaction > 0:
            total_revenue += transaction
            print(f"Добавлено: {transaction}")
print("=== ИТОГ ДНЯ ===")
print(f"Общая выручка магазина: {total_revenue}")