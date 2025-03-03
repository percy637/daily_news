import requests

def send_notification(message):
    user_key = 'u2hnnf63dad9kra1ud3xrvg7aeecfn'  # Remplace avec ton User Key
    api_token = 'aogfsegqv59kqvnwwwj21zv6qb2xts'  # Remplace avec ton API Token
    
    url = 'https://api.pushover.net/1/messages.json'
    
    payload = {
        'user': user_key,
        'token': api_token,
        'message': message,
        'title': 'Motley Fool - News du Jour',  # Titre de la notification
    }
    
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Notification envoyée avec succès!")
    else:
        print("Erreur lors de l'envoi de la notification", response.text)

# Exemple d'appel de la fonction avec un résumé
message = """
How Are 9 Out of the 11 Stock Market Sectors Outperforming the S&P 500 in 2025? - 9 sectors outperforming the S&P 500, with tech and health sectors leading.
"""
send_notification(message)
