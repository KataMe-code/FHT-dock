# お手入れ記録

| 論理名     | 物理名       | 型       | 制約   | index | 備考                       |
| :--------- | :----------- | :------- | :----- | :---- | :------------------------- |
| _id        | ケアID       | ObjectID | PK     | 自動  |                            |
| pet_id     | ペットID     | ObjectID |        | 〇    | ペット情報のオブジェクトID |
| notes      | お手入れ記録 | string   | string |       | 255文字                    |
| created_at | 作成日時     | DATE     |        |       | yyyy-MM-ddThh:mm:ss        |
| updated_at | 更新日時     | DATE     |        |       | yyyy-MM-ddThh:mm:ss        |

[テーブル定義一覧へ](../database-design.md)
