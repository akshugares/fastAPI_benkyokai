from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# 環境変数の読み込み
load_dotenv()

# データベースURLの設定
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL"
)
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

# データベースエンジンの作成
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# セッションファクトリーの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスの定義
Base = declarative_base()

# データベースセッションを取得する関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    # 環境変数の確認
    print(f"DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")
    
    # エンジンの確認
    print(f"Engine: {engine}")
    
    # セッションの確認
    try:
        db = SessionLocal()
        print("✓ session created successfully")
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"Tables: {tables}")
        db.close()
        print("✓ session closed successfully")
    except Exception as e:
        print(f"✗ session creation failed: {e}")
    
    # ベースクラスの確認
    print(f"Base class: {Base}")
