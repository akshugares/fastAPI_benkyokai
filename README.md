# 体重管理アプリ(FastAPI勉強会)

## よく使う

```bash
# コンテナ起動
docker compose up -d

# コンテナに入る(必ずしも必須ではない)
docker compose exec app bash

# ドキュメント確認
http://localhost:8000/docs

# データベースモデル定義
alembic revision --autogenerate -m "Add user model"
alembic upgrade head
```