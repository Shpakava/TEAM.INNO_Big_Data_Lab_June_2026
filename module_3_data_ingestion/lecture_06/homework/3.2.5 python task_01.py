# Входные данные
rows_range = range(1, 6)

# Работа со списками
rows = list(rows_range)
rows[2] = "Ремонт"
priority_rows = rows[:3]

# Результат
if 5 in rows:
    print(f"Ряд 5 доступен")
print(f"Список рядов: {rows}")
print(f"Приоритетные ряды: {priority_rows}")