# API一覧

| 属性  | API名            | endpoint              | メソッド | 機能                             | セキュリティ |
| :---- | :--------------- | :-------------------- | :------- | :------------------------------- | :----------- |
| auth  | csrfトークン取得 | /auth/csrftoken       | get      | CSRFトークンを取得する           |              |
| auth  | login            | /auth/login           | post     | ログイン                         | CSRF         |
| auth  | logout           | /auth/logout          | post     | ログアウト                       | CSRF         |
| user  | ユーザー登録     | /user/register        | post     | ユーザー登録                     | CSRF         |
| user  | ユーザー情報更新 | /user/edit            | patch    | パスワード以外のユーザー情報更新 | JWT, CSRF    |
| user  | パスワード更新   | /user/password/update | patch    | パスワード更新                   | JWT, CSRF    |
| user  | ユーザー情報取得 | /user/info            | get      | ユーザー情報取得                 | JWT          |
| user  | ユーザー情報削除 | /user/delete          | delete   | ユーザー情報削除                 | JWT, CSRF    |
| pet   | ペット登録       | /pet/register         | post     | ペット登録                       | JWT, CSRF    |
| pet   | ペット情報更新   | /pet/edit             | patch    | ペット情報更新                   | JWT, CSRF    |
| pet   | ペット情報取得   | /pet/info             | get      | ペット情報取得                   | JWT          |
| pet   | ペット情報削除   | /pet/delete           | delete   | ペット情報削除                   | JWT, CSRF    |
| breed | 種一覧           | /breed/info           | get      | 犬種猫種一覧取得                 | JWT          |
| meal  | 食事設定登録     | /meal/setting/create  | post     | 食事設定登録                     | JWT, CSRF    |
| meal  | 食事設定更新     | /meal/setting/edit    | patch    | 食事設定更新                     | JWT, CSRF    |

## 仕様

- post,patch系APIのレスポンスは作成、更新を行ったデータを取得する取得系APIと同じレスポンスを返す
  - パスワード変更のみ例外でメッセージのみを返す
    - 理由はセキュリティ面と描画するものではないため
- deleteは成功メッセージのみ返す
- post,patch,delete系はAPIはCSRF tokenの検証を行う
- ユーザー登録、login, logout以外はJWTの送信とJWTのリフレッシュを行う
