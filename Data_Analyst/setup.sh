#!/bin/bash

# Créer un environnement virtuel
echo "Creating virtual environment..."
python3.12 -m venv venv

# Activer l'environnement virtuel
echo "Activating virtual environment..."
source venv/bin/activate

# Installer les dépendances
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready!"