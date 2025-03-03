# Utilisation d'une image Python
FROM python:3.12

# Définition du dossier de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définition de la commande de démarrage
CMD ["python", "send_notif.py"]

