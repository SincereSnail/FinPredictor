# 📈 FinPredictor

**FinPredictor**는 특정 종목의 주가 데이터를 자동으로 수집하고, 머신러닝 기반의 모델을 활용해 주가를 예측하며, 예측 결과에 따라 자동 매수·매도까지 진행하는 **완전자동화 주식 거래 시스템**입니다.  
앞으로는 성장 가능성이 높은 종목을 자동으로 탐색하는 기능도 추가할 계획입니다.

---

## 🚀 주요 기능

1. **데이터 저장 및 관리**
   - 📊 **데이터 자동 수집:** 주식 데이터 API를 통한 실시간 및 과거 데이터 수집  
   - 🗂️ **데이터 분류 및 평가:** 수집한 데이터를 종목별, 기간별로 분류 및 품질 평가  

2. **데이터 학습 및 예측**
   - 🤖 **머신러닝 학습:** 주식 데이터를 기반으로 예측 모델 학습  
   - 📈 **주가 예측:** 학습된 모델을 통해 실시간 주가 예측  
   - 💾 **예측 데이터 저장:** 예측 결과를 저장하여 성능 개선 및 기록  

3. **자동 거래 (Auto Trading)**
   - 💰 **자동 매수:** 예측 결과에 따라 자동 매수 전략 실행  
   - 💸 **자동 매도:** 목표가 도달 시 자동 매도 전략 실행  

4. **지속적 학습**
   - 🔄 **예측 데이터 기반 재학습:** 일정 주기마다 예측 결과를 기반으로 모델 업데이트  

---

## ⚙️ 사용 방법

### 1️⃣ 설치

```bash
git clone https://github.com/SincereSnail/FinPredictor.git
cd FinPredictor
pip install -r requirements.txt

### 2️⃣ 실행
```bash
python main.py

### 3️⃣ 환경 변수 설정 (.env)
```makefile
API_KEY=your_api_key
TRADING_API_KEY=your_trading_api_key
TRADING_SECRET_KEY=your_secret_key

## 🛠️ 기술 스택
- Python 3.10
- TensorFlow / PyTorch – 머신러닝 모델 학습 및 예측
- Pandas, NumPy – 데이터 처리 및 분석
- Matplotlib, Seaborn – 데이터 시각화
- Fast Api – 주식 데이터 수집 
- Selenium / BeautifulSoup – 웹 크롤링
- Docker – 배포 및 환경 관리 (예정)

## 🏗️ 아키텍처
[ 데이터 수집 ] → [ 데이터 전처리 ] → [ 모델 학습 ] → [ 예측 ] → [ 자동 거래 ]
       ▲                                                    |
       └───────────────── 피드백 및 성능 개선 ───────────────┘

