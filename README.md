# 簡易ブログアプリ

Django で作成したシンプルなブログアプリです。ユーザーがログインして記事を投稿し、記事にコメントできる基本的なブログ機能を実装しています。

## 主な機能

- 記事一覧の表示
- 記事詳細の表示
- ログインユーザーによる記事の作成、編集、削除
- ログインユーザーによるコメントの投稿、編集、削除
- 投稿者ごとの記事一覧表示
- 記事一覧とコメント一覧のページネーション
- Django の認証機能を利用したログイン、ログアウト
- Bootstrap を利用した簡単なレスポンシブ UI

## 使用技術

- Python
- Django 5.2
- SQLite
- Bootstrap 5
- django-widget-tweaks

## セットアップ

### 1. リポジトリを取得

```bash
git clone <repository-url>
cd 03_simple_blog_app
```

### 2. 仮想環境を作成して有効化

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows の場合は次のコマンドで有効化します。

```bash
.venv\Scripts\activate
```

### 3. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

### 4. マイグレーションを実行

```bash
python manage.py migrate
```

### 5. 管理ユーザーを作成

記事投稿や管理画面の確認に使うユーザーを作成します。

```bash
python manage.py createsuperuser
```

### 6. 開発サーバーを起動

```bash
python manage.py runserver
```

ブラウザで次の URL にアクセスします。

```text
http://127.0.0.1:8000/
```

## 画面と URL

| URL | 内容 |
| --- | --- |
| `/` | 記事一覧 |
| `/article/<id>/` | 記事詳細、コメント一覧、コメント投稿 |
| `/article/create/` | 記事作成 |
| `/article/<id>/update/` | 記事編集 |
| `/author/<id>/` | 投稿者の記事一覧 |
| `/accounts/login/` | ログイン |
| `/admin/` | Django 管理画面 |

## アプリの構成

```text
03_simple_blog_app/
├── config/                  # Django プロジェクト設定
├── simple_blog/             # ブログアプリ本体
│   ├── models.py            # Article、Comment モデル
│   ├── views.py             # 一覧、詳細、作成、編集、削除などのビュー
│   ├── forms.py             # 記事フォーム、コメントフォーム
│   ├── urls.py              # ブログ機能の URL 定義
│   └── templates/           # HTML テンプレート
├── manage.py
├── requirements.txt
└── README.md
```

## モデル概要

### Article

記事データを扱うモデルです。

- `user`: 投稿者
- `title`: タイトル
- `content`: 本文
- `created_at`: 作成日時
- `updated_at`: 更新日時

### Comment

記事に紐づくコメントを扱うモデルです。

- `user`: コメント投稿者
- `article`: コメント対象の記事
- `content`: コメント本文
- `created_at`: 作成日時
- `updated_at`: 更新日時

## 認証と権限

- 記事作成、記事編集、記事削除はログインが必要です。
- コメント投稿、コメント編集、コメント削除はログインが必要です。
- 記事を編集、削除できるのは、その記事を作成したユーザーだけです。
- コメントを編集、削除できるのは、そのコメントを投稿したユーザーだけです。

## 開発メモ

- データベースは開発用として SQLite を使用しています。
- Bootstrap は CDN から読み込んでいます。
- フォームの CSS クラス付与に `django-widget-tweaks` を使用しています。
- 本番運用する場合は `SECRET_KEY`、`DEBUG`、`ALLOWED_HOSTS` などの設定を見直してください。
