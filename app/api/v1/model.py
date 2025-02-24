from fastapi import APIRouter
from app.yolo_model.predict import predict_stock_price

router = APIRouter()

@router.get("/predict/{ticker}")
def predict_stock(ticker: str):
    prediction = predict_stock_price(ticker)
    return {"ticker": ticker, "predicted_price" : prediction}
