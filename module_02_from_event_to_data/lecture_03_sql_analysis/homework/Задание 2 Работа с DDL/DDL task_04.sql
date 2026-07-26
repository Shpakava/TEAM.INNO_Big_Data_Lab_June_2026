Добавить ограничение UNIQUE к столбцу manager_email в таблице Data_Layers (предварительно заполнив столбец любыми значениями, чтобы избежать ошибки).

UPDATE Data_Layers SET manager_email = 'bronze_admin@store.com' WHERE LayerName = 'Bronze';
UPDATE Data_Layers SET manager_email = 'silver_admin@store.com' WHERE LayerName = 'Silver';
UPDATE Data_Layers SET manager_email = 'gold_admin@store.com' WHERE LayerName = 'Gold';

ALTER TABLE Data_Layers 
ADD CONSTRAINT unique_manager_email UNIQUE (manager_email);