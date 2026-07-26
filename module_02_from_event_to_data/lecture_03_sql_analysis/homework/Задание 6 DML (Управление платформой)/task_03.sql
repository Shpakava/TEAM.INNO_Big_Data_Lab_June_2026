Установить modify_timestamp (функция NOW()) для продуктов без даты.

UPDATE products
SET modify_timestamp = NOW()
WHERE modify_timestamp IS NULL;