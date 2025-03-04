from flask import Flask, render_template
import openai
import daily_news
import os

app = Flask(__name__)


@app.route("/")
def home():
    articles = daily_news.get_motley_news()
    summaries = [{"title": article["title"], "summary": daily_news.summarize_article(article["title"], article["link"])} for article in articles]
    daily_news.send_notification(summaries)
    return render_template('index.html', summaries=summaries)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#écouter sur : dailynews-production.up.railway.app