# Входные данные
usd_prices = { 
"Banana": 1.2, 
"Mango": 2.5, 
"Avocado": 2.0 
}

# Результат Dictionary Comprehension
eur_prices = {product: price * 0.9 for product, price in usd_prices.items()}
print(eur_prices)
