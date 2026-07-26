Вставить нового сотрудника и первую продажу в одной транзакции.

BEGIN;

INSERT INTO employees (
    employee_id, 
    first_name, 
    middle_initial, 
    last_name, 
    birth_date, 
    gender, 
    city_id, 
    shop_id, 
    hire_date
) VALUES (
    321,
    'Alex', 
    'J', 
    'Smith', 
    '1995-08-20', 
    'Male', 
    1,
    1,
    '2026-07-26'
);

INSERT INTO sales (
    sales_id, 
    employee_id, 
    customer_id, 
    product_id, 
    quantity, 
    discount, 
    total_price, 
    sales_timestamp, 
    transaction_number
) VALUES (
    2000002,
    321,
    3,
    1,
    2,
    10.00, 
    500.50, 
    CURRENT_TIMESTAMP, 
    'T0000000000'
);

COMMIT;