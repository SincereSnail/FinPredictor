from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import yfinance as yf
from app.schemas import stock as schemas
from app.crud import stock as crud
from app.db.database import get_db

router = APIRouter()

#주식 데이터 수집
@router.get("/stock/{ticker}")
def fetch_stock_data(ticker: str, db: Session = Depends(get_db)) :
    stock = yf.Tocker(ticker)
    hist = stock.history(preiod="1y")
    data = hist[['open','Close']].rest_index().to_dict(orient="records")
    for entry in data :
        crud.create_stock_data(db, schemas.StockDataCreate(**entry))
    return {"message": f"{ticker} data collected"}

@router.get("/news/{ticker}")
def fetch_news(ticker: str, db: Session = Depends(get_db)):
    #뉴스 기사 검색 후 스코어링 (LLM적용)
    articles = ["기사1 내용", "기사2 내용"]
    scores = [0.85,0.90]
    for article, score in zip(articles, scores) :
        crud.create_news_data(db, schemas.NewsDataCreate(ticker=ticker,content=article, score= score))
    return {"message": f"{ticker} news collected"}
