# 排せつ記録

| 論理名             | 物理名       | 型       | 制約     | index | 備考                       |
| :----------------- | :----------- | :------- | :------- | :---- | :------------------------- |
| _id                | 排せつ記録ID | ObjectID | PK       | 自動  |                            |
| pet_id             | ペットID     | ObjectID |          |       | ペット情報のオブジェクトID |
| excretion_datetime | 排せつ日時   | DATE     | NOT NULL |       | yyyy-MM-ddThh:mm:ss        |
| type               | タイプ       | string   | NOT NULL |       | おしっこorうんち           |
| quantity           | 量           | string   | NOT NULL |       | 50文字                     |
| condition          | 状態         | string   |          |       | 50文字                     |
| notes              | メモ         | string   |          |       | 255文字                    |
| created_at         | 作成日時     | DATE     |          |       | yyyy-MM-ddThh:mm:ss        |
| updated_at         | 更新日時     | DATE     |          |       | yyyy-MM-ddThh:mm:ss        |

[テーブル定義一覧へ](../database-design.md)