
# PETS-IMAGES

| 論理名        | 物理名                   | 型       | 制約 | index | 備考                                    |
| :------------ | :----------------------- | :------- | :--- | :---- | :-------------------------------------- |
| _id           | ペット画像ID             | ObjectID |      |       |                                         |
| pet_id        | ペットID                 | ObjectID |      |       |                                         |
| file_id       | ペット画像ID             | ObjectID |      |       | MongoDBのGridFsを使って保存した画像のID |
| image_version | ペット画像バージョン番号 | int      |      |       |                                         |
| created_at    | 作成日時                 | DATE     |      |       | yyyy-MM-ddThh:mm:ss                     |
| updated_at    | 更新日時                 | DATE     |      |       | yyyy-MM-ddThh:mm:ss                     |

[テーブル定義一覧へ](../database-design.md)
