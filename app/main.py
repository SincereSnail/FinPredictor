from fastapi import FastAPI
from pydantic import BaseModel
import random

# FastAPI 앱 생성
app = FastAPI()

# 주식 예측 요청을 받을 데이터 모델
class StockRequest(BaseModel):
    ticker: str

# 기본 라우트 (헬스 체크)
@app.get("/")
def read_root():
    return {"message": "FastAPI 서버가 정상적으로 실행 중입니다!"}

# 주식 예측 API
@app.get("/model/predict/{ticker}")
def predict_stock(ticker: str):
    # 랜덤한 주가 예측 값 반환 (실제 모델이 연결되면 여기에 모델 예측 코드 추가)
    predicted_price = round(random.uniform(100, 500), 2)
    return {"ticker": ticker, "predicted_price": predicted_price}

