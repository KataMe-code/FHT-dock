
# PETS

| 論理名     | 物理名         | 型       | 制約     | index | 備考                         |
| :--------- | :------------- | :------- | :------- | :---- | :--------------------------- |
| _id        | ペットID       | ObjectID | PK       | 自動  |                              |
| user_id    | ユーザーID     | ObjectID |          | 〇    | ユーザー情報のオブジェクトID |
| species    | ペットの種類   | string   | NOT NULL |       | 50文字                       |
| breed      | 犬種・猫種     | string   | NOT NULL |       | 50文字                       |
| name       | ペットの名前   | string   | NOT NULL |       | 50文字                       |
| birth_day  | ペットの誕生日 | DATE     |          |       | yyyy-MM-dd                   |
| sex        | ペットの性別   | string   | NOT NULL |       | male or female               |
| created_at | 作成日時       | DATE     |          |       | yyyy-MM-ddThh:mm:ss          |
| updated_at | 更新日時       | DATE     |          |       | yyyy-MM-ddThh:mm:ss          |

[テーブル定義一覧へ](../database-design.md)
