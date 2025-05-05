            INT id PK "AUTO_INCREMENT"
            INT pet_id FK "NOT NULL"
            DATETIME visit_date "NOT NULL"
            VARCHAR(255) reason "NOT NULL"
            DATETIME next_visit_date "次回来院日時予定"
            TEXT notes
            DATETIME created_at "DEFAULT CURRENT_TIMESTAMP"
            DATETIME updated_at "DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"