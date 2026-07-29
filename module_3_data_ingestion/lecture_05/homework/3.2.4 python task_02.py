# Входные данные
product = " фермерский ТВОРОГ " 
price = 4.567 
qty = 3 
csv_row = "milk,bread,cheese" 
review = "Это лучший ТВОРОГ в городе!" 
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

# Преобразование строк
clean_product = product.strip().lower().title()
total = price * qty
csv_row_new = " | ".join(csv_row.split(','))
key_word = "творог"
file_path = r"C:\EcoMarket\data\2025\january\sales.csv" # Специальные символы не интерпретируются, они не изменяют текст (путь к файлу)

# Результат
print(f"Чек \"EcoMarket\" \nТовар: \t{clean_product} \nКол-во:\t{qty} \nИтого: \t{total:.2f} руб.")
print(csv_row_new)
if key_word in review.lower(): 
	print(f"Отзыв относится к категории: Dairy {file_path}")
