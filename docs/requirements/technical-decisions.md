# 技術スタック

## ドキュメント

- mkdocs
  - ドキュメントをmdで管理、ホスティングもできるため
  - mermaid記法でER図なども記載できるため

## フロントエンド

- React.js
    - 多くの開発現場で利用されるため
    - まずはReact.jsとライブラリのみで作成する
- ルーティング
    - React Router v7
- 開発環境/バンドラー
    - vite
- テストフレームワーク
    - vitest
- unit test
    - vitest React Testing library
- インテグレーションテスト
    - storybook
- UIテスト
- E2Eテスト
    - 現在は導入を考えていない
        - まずはjest(vitest) Testing libraryを使いこなすことに注力したいため

## バックエンド

- python
    - FastAPI

## データベース
- Dockerで立ち上げたMongoDB
- ※余裕があったらMongoDBの有料版

## インフラストラクチャー/デプロイメン

- コンテナ化
    - Docker
- クラウドプロバイダ
    - GCP
- CI/CDツール
    - GitHub Actions
- 監視ツール
    - 今のところ考えていない

## 開発ツール

- バージョン管理システム
    - Git
- コードエディタ
    - cursor(visual studio code)

## 認証

- JWT
    - Tokenの管理はDBでは行わない
        - アプリケーションが大きくなったり、必要となった場合はDB管理にする
