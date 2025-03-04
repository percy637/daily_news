from flask import Flask, render_template
import openai
import daily_news

app = Flask(__name__)

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Remplace avec ta clé API

@app.route("/")
def home():
    title = "Tesla atteint un nouveau record de ventes"
    link = "https://example.com/article"
    #summary = daily_news.summarize_article(title, link)
    summary  = "test de summary"
    return render_template("index.html", title=title, link=link, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
"""news_summary = get_motley_news()
send_notification(news_summary)
print(news_summary)"""