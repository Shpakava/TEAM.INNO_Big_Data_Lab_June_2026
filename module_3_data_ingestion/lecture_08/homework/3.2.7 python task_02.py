# Входные данные
branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000}
]

def audit_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[AUDIT] Запуск анализа...")
        print(f"[AUDIT] Анализ завершен.")
        result = func(*args, **kwargs)
        return result
    return wrapper

@audit_logger
def get_sorted_report():
    sorted_branches = sorted(branches, key=lambda x: x["revenue"], reverse=True)
    print("Топ филиалов:")
    for index, branch in enumerate(sorted_branches, start=1):
        print(f"{index}. {branch['city']}: {branch['revenue']}")

get_sorted_report()


