from fastapi import APIRouter

router = APIRouter()

@router.post("/buy/{ticker}")
def auto_buy(ticker: str):
    return {"status": "buy order executed", "ticker":ticker}

@router.post("/sell/{ticker}")
def auto_sell(ticker: str):
    return {"status": "Sell order exected", "ticker": ticker}