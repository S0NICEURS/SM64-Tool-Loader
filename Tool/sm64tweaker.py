import os
import requests
import zipfile
import subprocess

# Chemin vers le dossier où SM64 Tweaker - Start.exe sera installé
dossier_installation = os.path.dirname(__file__)

# Nom du fichier SM64 Tweaker - Start.exe
nom_tweaker_exe = 'SM64 Tweaker (V0.4.7.1 Beta)/SM64 Tweaker - Start.exe'

# Chemin complet vers SM64 Tweaker - Start.exe
chemin_tweaker_exe = os.path.join(dossier_installation, nom_tweaker_exe)

# URL pour télécharger SM64 Tweaker.zip
sm64_tweaker_zip_url = "https://cloud.pilzinsel64.de/s/qY8bX2aWmNAzoiH/download"

# Fonction pour télécharger et extraire un fichier ZIP
def telecharger_et_extraire_zip(url, destination_folder):
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {url}...")
        response = requests.get(url, stream=True)
        zip_path = os.path.join(destination_folder, "sm64_tweaker.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Extraction du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(destination_folder)
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print(f"Le fichier ZIP a été téléchargé et extrait avec succès dans {destination_folder}.")
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction du fichier ZIP : {e}")
        return False

# Fonction pour vérifier et ouvrir SM64 Tweaker - Start.exe
def verifier_et_ouvrir_tweaker():
    if os.path.exists(chemin_tweaker_exe):
        try:
            # Ouvre SM64 Tweaker - Start.exe
            subprocess.Popen([chemin_tweaker_exe])
            print(f"{nom_tweaker_exe} a été ouvert avec succès.")
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {nom_tweaker_exe} : {e}")
    else:
        print(f"Le fichier {nom_tweaker_exe} n'existe pas.")
        installer_sm64_tweaker()

# Fonction pour télécharger, extraire et ouvrir SM64 Tweaker - Start.exe si nécessaire
def installer_sm64_tweaker():
    print(f"Téléchargement et installation de {sm64_tweaker_zip_url}...")
    if telecharger_et_extraire_zip(sm64_tweaker_zip_url, dossier_installation):
        if os.path.exists(chemin_tweaker_exe):
            try:
                # Ouvre SM64 Tweaker - Start.exe après installation
                subprocess.Popen([chemin_tweaker_exe])
                print(f"{nom_tweaker_exe} a été installé et ouvert avec succès.")
            except OSError as e:
                print(f"Erreur lors de l'ouverture de {nom_tweaker_exe} après installation : {e}")
        else:
            print(f"Le fichier {nom_tweaker_exe} n'a pas été trouvé après extraction du ZIP.")
    else:
        print("Impossible de télécharger et extraire SM64 Tweaker.zip depuis le lien spécifié.")

# Vérification et tentative d'ouverture de SM64 Tweaker - Start.exe
verifier_et_ouvrir_tweaker()
