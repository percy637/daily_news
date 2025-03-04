from flask import Flask, render_template
import openai
import daily_news
import os

app = Flask(__name__)

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv("OPENAI_API_KEY")

# Vérifier que la clé est bien récupérée
if not api_key:
    raise ValueError("La clé API OpenAI n'est pas définie !")

# Initialiser le client OpenAI
client = openai.OpenAI(api_key=api_key)

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