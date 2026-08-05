class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Ошибка безопасности: Цена должна быть положительной!")

    def calculate_cost(self):
        return self.get_price()

    def get_display_info(self):
        return f"Товар: {self.name} | Цена: {self.get_price()} руб."

class WeighableProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def calculate_cost(self):
            return self.get_price() * self.weight

    def get_display_info(self):
            return f"Весовой товар: {self.name} | Вес: {self.weight} кг | Итого: {self.calculate_cost()} руб."

class PackagedProduct(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def calculate_cost(self):
            return self.get_price() * self.quantity

    def get_display_info(self):
            return f"Упаковка: {self.name} | Количество: {self.quantity} шт | Итого: {self.calculate_cost()} руб."

# Создание товаров
milk = Product("Молоко", 100)
apples = WeighableProduct("Яблоки", 50, 2.5)
eggs = PackagedProduct("Яйца", 12, 10)

# Корзина
cart = [milk, apples, eggs]

# Попытка "взлома" цены для молока
milk.set_price(-200)


print("\n--- Чек EcoMarket ---")
total_sum = 0

for prod in cart:
     print(prod.get_display_info())
     total_sum += prod.calculate_cost()

print("---------------------")
print(f"ИТОГО К ОПЛАТЕ: {total_sum} руб.")    
