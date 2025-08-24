from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

myapp = FastAPI()

# CORSの設定
myapp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@myapp.get("/")   # ルートエンドポイントにGETリクエストが来たときにroot関数を呼び出す
async def root():
    return {"message": "Hello World"} 