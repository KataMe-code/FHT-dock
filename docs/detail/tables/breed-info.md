# BREED_INFO

| 論理名 | 物理名   | 型       | 制約 | index | 備考 |
| :----- | :------- | :------- | :--- | :---- | :--- |
| _id    | ID       | ObjectID | PK   | 自動  |      |
| dog    | 犬種一覧 | Array    |      |       |      |
| cat    | 猫種一覧 | Array    |      |       |      |

## サンプル

```json
{
    "dog":[
        "dog1",
        "dog2"
    ],
    "cat":[
        "cat1",
        "cat2"
    ]
}
```

[テーブル定義一覧へ](../database-design.md)
