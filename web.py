from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder="templates")  # 🔥 템플릿 폴더 명시

API_URL = "http://127.0.0.1:8000"  # FastAPI 서버 주소

@app.route("/")
def index():
    return render_template("index.html")  # 🔥 templates 폴더의 index.html을 로드

@app.route("/predict", methods=["POST"])
def predict():
    ticker = request.form["ticker"]
    response = requests.get(f"{API_URL}/model/predict/{ticker}")
    #플라스크를 사용하면 다음과 같이 액션을 취할 수 있습니다.
    #render_template함수를 사용하여 html에 변수를 추가하여 렌더링할 수 있습니다.
    return render_template("index.html", prediction=response.json())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
