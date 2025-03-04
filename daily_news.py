import os
from playwright.sync_api import sync_playwright
import openai  # Utilisation de l'API pour résumer
import requests


URL = "https://www.fool.com/investing-news/"

# Récupérer la clé API depuis les variables d'environnement
api_key = os.getenv("OPENAI_API_KEY")

# Vérifier que la clé est bien récupérée
if not api_key:
    raise ValueError("La clé API OpenAI n'est pas définie !")

# Initialiser le client OpenAI
client = openai.OpenAI(api_key=api_key)

def summarize_article(title, link):
    prompt = f"""
    Voici un titre d'article : {title}.
    Résume cet article de manière claire, en incluant le nom de l'entreprise mentionnée dans l'article et les points les plus importants. Le résumé doit être pertinent, en mettant en évidence les facteurs qui expliquent la situation de l'entreprise et ses perspectives d'avenir.

    Titre de l'article : {title}
    Lien de l'article : {link}
    """

    response = client.chat.completions.create(  # Nouvelle façon d'appeler l'API
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un assistant très compétent pour générer des résumés clairs et informatifs d'économie et de finance."},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content.strip()



def get_motley_news():
    """Récupère les articles et génère une newsletter résumée."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        page = browser.new_page()
        page.goto(URL, timeout=60000)  

        page.wait_for_selector("h5", timeout=5000)  
        articles = page.locator("div.flex.py-12px.text-gray-1100").all()

        newsletter = "**📰 Motley Fool - News du Jour**\n\n"

        for article in articles[:5]:  
            title = article.locator("h5").inner_text().strip()
            link = "https://www.fool.com" + article.locator("a").first.get_attribute("href")
            summary = summarize_article(title, link)

            newsletter += f"### {title}\n🔗 [Lire l'article]({link})\n📌 {summary}\n\n"

        browser.close()
    
    return newsletter

def send_notification(message):
    user_key = 'u2hnnf63dad9kra1ud3xrvg7aeecfn'  # Remplace avec ton User Key
    api_token = 'aogfsegqv59kqvnwwwj21zv6qb2xts'  # Remplace avec ton API Token
    
    url = 'https://api.pushover.net/1/messages.json'
    
    payload = {
        'user': user_key,
        'token': api_token,
        'message': message,
        'title': 'Motley Fool - News du Jour',  # Titre de la notification
        'url' : "http://www.apple.com/fr/",  
        'url_title' : "Lire l'article"
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Notification envoyée avec succès!")
    else:
        print("Erreur lors de l'envoi de la notification", response.text)


# Exécution et affichage
"""news_summary = get_motley_news()
send_notification(news_summary)
print(news_summary)"""
