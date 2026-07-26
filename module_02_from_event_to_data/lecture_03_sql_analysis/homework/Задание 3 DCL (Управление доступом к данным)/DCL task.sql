Создать новую роль (пользователя) PostgreSQL с именем data_engineer_trainee (стажер) и простым паролем.
Предоставить data_engineer_trainee право SELECT на таблицу Sales.
Тест 1: 
(В новой сессии) подключитесь как data_engineer_trainee и выполните SELECT * FROM Sales;.
Как data_engineer_trainee попытаться выполнить INSERT новой продажи в Sales. (Должно завершиться неудачей).
Как пользователь-администратор предоставить data_engineer_trainee права INSERT и UPDATE на таблицу Sales.
Тест 2: 
Как data_engineer_trainee попробовать выполнить INSERT и UPDATE. (Теперь должно сработать).

CREATE ROLE data_engineer_trainee WITH LOGIN PASSWORD 'TraineePass123';

GRANT SELECT ON sales TO data_engineer_trainee;

GRANT INSERT, UPDATE ON sales TO data_engineer_trainee;

INSERT INTO sales (sales_id, employee_id, customer_id, product_id, quantity, discount, total_price, sales_timestamp, transaction_number)
VALUES (2000001, 1, 1, 1, 1, 0, 100, CURRENT_TIMESTAMP, 'TEST_TR_001');

UPDATE sales 
SET quantity = 5, 
    total_price = 500.00 
WHERE sales_id = 1; 