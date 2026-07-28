# Входные данные
raw_sku = "CARROT-001"
raw_regions = ("Minsk", "Warsaw", "Berlin", "Warsaw")
raw_weight_str = "2.5"
raw_stock_str = "150"

# Явное преобразование типов
weight_kg = float(raw_weight_str)
stock_quantity = int(raw_stock_str)

# Преобразование коллекций
sku_as_list = list(raw_sku)
regions_list = list(raw_regions)
unique_regions = set(raw_regions)
regions_tuple = tuple(unique_regions)

# Создание пустых коллекций двумя способами, где это возможно
empty_list_1 = list()
empty_list_2 = []
empty_dict_1 = dict()
empty_dict_2 = {}
empty_tuple_1 = tuple()
empty_tuple_2 = ()
empty_set = set()

# Проверка “пустоты” коллекций через bool()
check_list = bool(empty_list_1)
check_dict = bool(empty_dict_1)
check_tuple = bool(empty_tuple_2)
check_set = bool(empty_set)
list_1 = [1, 2, 3]
dict_1 = {1: "a", 2: "b", 3: "c"}
tuple_1 = ("a", "b", "c")
set_1 = {"aaa", "aaa", "bbb", "bbb", "ccc", "ccc"}

# Выведение в консоль значений и типов
print(weight_kg, type(weight_kg))
print(stock_quantity, type(stock_quantity))
print(sku_as_list, type(sku_as_list))
print(regions_list, type(regions_list))
print(unique_regions, type(unique_regions))
print(regions_tuple, type(regions_tuple))
print(check_list)
print(check_dict)
print(check_tuple)
print(check_set)
print(bool(list_1))
print(bool(dict_1))
print(bool(tuple_1))
print(bool(set_1))