# app.py
from flask import Flask, render_template, request
import sentiment_model

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        sentiment = sentiment_model.predict_sentiment(text)
        return render_template("index.html", sentiment=sentiment)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
