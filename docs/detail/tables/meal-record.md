            INT id PK "AUTO_INCREMENT"
            int meal_setting_id FK
            DATETIME recorded_at
            float quantity "食べた量"
            DATETIME created_at "DEFAULT CURRENT_TIMESTAMP"
            DATETIME updated_at "DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"