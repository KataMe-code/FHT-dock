            INT id PK "AUTO_INCREMENT"
            INT pet_id FK "NOT NULL"
            VARCHAR(100) supplement_name "NOT NULL"
            VARCHAR(50) dosage "用量"
            DATETIME given_at "与えた日時"
            INT hospital_record_id
            DATETIME created_at "DEFAULT CURRENT_TIMESTAMP"
            DATETIME updated_at "DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"