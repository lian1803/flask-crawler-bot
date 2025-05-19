from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ 서버 잘 뜸!"

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(debug=True)