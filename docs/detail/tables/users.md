    
# USERS

| 論理名              | 物理名               | 型       | 制約            | index | 備考                            |
| :------------------ | :------------------- | :------- | :-------------- | :---- | :------------------------------ |
| user_id             | ユーザーID           | ObjectID | PK              | 自動  |                                 |
| user_name           | ユーザー名           | string   | Not Null        |       | 100文字                         |
| email               | メールアドレス       | string   | NOT NULL UNIQUE |       | 100文字                         |
| password            | パスワード           | string   | NOT NULL        |       | SHA-256で暗号化されたパスワード |
| password_retry_time | パスワード試行回数   | int      | NOT NULL        |       | 5回間違えたらロック             |
| locked              | アカウントロック状態 | boolean  | NOT NULL        |       | True: ロック, false: open       |
| isWIthdrawal        | 退会状態             | boolean  | NOT NULL        |       | True: 退会, False: 継続中       |
| created_at          | 作成日時             | DATE     |                 |       | yyyy-MM-ddThh:mm:ss             |
| updated_at          | 更新日時             | DATE     |                 |       | yyyy-MM-ddThh:mm:ss             |

[テーブル定義一覧へ](../database-design.md)
