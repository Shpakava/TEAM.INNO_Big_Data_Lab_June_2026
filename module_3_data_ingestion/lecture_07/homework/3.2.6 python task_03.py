# Входные данные
suppliers_log = [ 
	"FreshFarm Inc", 
	"GreenFields Ltd", 
	"AgroWorld Co", 
	"FreshFarm Inc", 
	"GreenFields Ltd" 
]

# Работа с множеством
unique_suppliers = set(suppliers_log)
unique_suppliers.add("GreenFields Ltd")

# Результат
if "FreshFarm Inc" in unique_suppliers:
    print("True")
print(unique_suppliers)
print(len(unique_suppliers))
