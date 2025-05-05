            INT id PK "AUTO_INCREMENT"
            INT pet_id FK "NOT NULL"
            VARCHAR(100) vaccine_name "NOT NULL ワクチン名"
            DATE vaccine_date "NOT NULL ワクチン接種日"
            DATE next_vaccine_date "次回ワクチン接種日"
            TEXT notes
            DATETIME created_at "DEFAULT CURRENT_TIMESTAMP"
            DATETIME updated_at "DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"