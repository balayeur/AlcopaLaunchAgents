import os
import time
import requests
from datetime import datetime
from pathlib import Path

# Fonction pour télécharger et sauvegarder une page web
def save_webpage(url, save_dir, prefix):
    response = requests.get(url)
    if response.status_code == 200:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        save_path = Path(save_dir) / f"{timestamp}_{prefix}.html"
        
        # Création du dossier si nécessaire
        save_path.parent.mkdir(parents=True, exist_ok=True)

        # Sauvegarde du contenu
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        
        print(f"✅ Page enregistrée : {save_path}")
        time.sleep(5)  # Pause pour éviter un envoi trop rapide
    else:
        print(f"❌ Erreur {response.status_code}: Impossible de charger {url}")

# Définition des URLs et des dossiers de sauvegarde
pages = [
    ("https://www.alcopa-auction.fr/",          "AuctionsList", "auctionsList")
    # ("https://www.alcopa-auction.fr/recherche", "GeneralList",  "generalList")
]

# Traitement des pages
for url, folder, prefix in pages:
    save_webpage(url, folder, prefix)