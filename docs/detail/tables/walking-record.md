            INT id PK "AUTO_INCREMENT"
            INT pet_id FK "NOT NULL"
            DATE date "日付"
            TIME walking_start_time "散歩開始時間"
            TIME walking_end_time "散歩終了時間"
            INT distance "距離"
            TEXT notes
            DATETIME created_at "DEFAULT CURRENT_TIMESTAMP"
            DATETIME updated_at "DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"