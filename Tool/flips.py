import os
import requests
import zipfile
import subprocess
import threading

# Chemin vers le fichier flips.exe dans le même dossier que ce script
chemin_flips_exe = os.path.join(os.path.dirname(__file__), 'flips.exe')

# URL pour télécharger floating.zip
floating_zip_url = "https://dl.smwcentral.net/11474/floating.zip"

# Fonction pour télécharger et extraire flips.exe depuis floating.zip si nécessaire
def telecharger_et_extraire_flips():
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {floating_zip_url}...")
        response = requests.get(floating_zip_url, stream=True)
        zip_path = os.path.join(os.path.dirname(__file__), "floating.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Extraction de flips.exe du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extract("flips.exe", os.path.dirname(__file__))
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print("flips.exe a été téléchargé et extrait avec succès.")
        ouvrir_flips_exe()  # Appel pour ouvrir flips.exe après extraction
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de flips.exe : {e}")
        return False

# Fonction pour ouvrir flips.exe
def ouvrir_flips_exe():
    try:
        subprocess.Popen([chemin_flips_exe])
    except OSError as e:
        print(f"Erreur lors de l'ouverture de flips.exe : {e}")

# Vérification si le fichier flips.exe existe
if os.path.exists(chemin_flips_exe):
    try:
        subprocess.Popen([chemin_flips_exe])
    except OSError as e:
        print(f"Erreur lors de l'ouverture de flips.exe : {e}")
        # Si une erreur se produit, tenter de télécharger et extraire flips.exe
        if not telecharger_et_extraire_flips():
            print("Impossible de télécharger et extraire flips.exe.")
else:
    print("Le fichier flips.exe n'existe pas dans ce dossier.")
    # Télécharger et extraire flips.exe car il n'existe pas localement
    if not telecharger_et_extraire_flips():
        print("Impossible de télécharger et extraire flips.exe depuis le lien spécifié.")

