from playwright.sync_api import sync_playwright

URL = "https://www.fool.com/investing-news/"

def get_motley_news():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        page = browser.new_page()
        page.goto(URL, timeout=60000)  

        # Attendre que les articles soient chargés
        page.wait_for_selector("h5", timeout=5000)  

        # Sélecteur basé sur la structure trouvée
        articles = page.locator("div.flex.py-12px.text-gray-1100").all()

        articles_data = []
        for article in articles[:5]:  # On prend les 5 premiers articles
            title = article.locator("h5").inner_text().strip()
            link = "https://www.fool.com" + article.locator("a").first.get_attribute("href")
            articles_data.append(f"{title} ({link})")

        browser.close()
    
    return articles_data

# Test du scraping
news = get_motley_news()
print(news)
