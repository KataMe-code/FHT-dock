
# MEAL_SETTING

| 論理名           | 物理名         | 型           | 制約                                                        | index | 備考           |
| :--------------- | :------------- | :----------- | :---------------------------------------------------------- | :---- | :------------- |
| id               | ID             | INT          | PK                                                          | 〇    | AUTO_INCREMENT |
| pet_id           | ペットID       | INT          | FK                                                          |       |                |
| meal_time        | 給餌時間       | TIME         | NOT NULL                                                    |       |                |
| meal_description | 給餌の説明     | VARCHAR(255) |                                                             |       |                |
| birth_day        | ペットの誕生日 | DATE         |                                                             |       |                |
| created_at       | ユーザーID     | DATETIME     | DEFAULT <br/> CURRENT_TIMESTAMP                             |       |                |
| updated_at       | ユーザーID     | DATETIME     | DEFAULT <br/> CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP |       |                |

[テーブル定義一覧へ](../database-design.md)
