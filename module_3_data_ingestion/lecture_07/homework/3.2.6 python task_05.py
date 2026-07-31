import json

# Входные данные
api_response_json = """ 
{ 
	"store": "StoreHub", 
	"orders": [ 
		{"id": 1, "total": 50}, 
		{"id": 2, "total": 200}, 
		{"id": 3, "total": 150} 
		]
 } 
"""

# Работа с dict и json
api_response_dict = json.loads(api_response_json)
orders = api_response_dict.get("orders")
high_value_orders = [order for order in orders if order["total"] > 100]
api_response_dict["high_value_orders"] = high_value_orders
api_response_json = json.dumps(api_response_dict)

# Результат
print(api_response_json)

