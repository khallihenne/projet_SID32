# Utilisez une image officielle Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet dans le conteneur
COPY . /app/

# Exposer le port 8000 pour Django
EXPOSE 8000
