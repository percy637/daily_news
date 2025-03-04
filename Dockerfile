# Utilisation d'une image Python
FROM python:3.12

# Définition du dossier de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Ajouter Playwright et les dépendances du navigateur
RUN pip install playwright
RUN playwright install

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définition de la commande de démarrage
CMD ["python", "app.py"]

