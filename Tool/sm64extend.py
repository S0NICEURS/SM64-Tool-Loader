import os
import requests
import zipfile
import subprocess

# Chemin vers le dossier où sm64extendGUI.exe est installé
dossier_installation = os.path.dirname(__file__)

# Nom du fichier sm64extendGUI.exe
nom_sm64extend_exe = 'sm64extend-0.3.2-win32/sm64extendGUI.exe'

# Chemin complet vers sm64extendGUI.exe
chemin_sm64extend_exe = os.path.join(dossier_installation, nom_sm64extend_exe)

# URL pour télécharger sm64extend-0.3.2-win32.zip
sm64extend_zip_url = "https://dl.smwcentral.net/20095/sm64extend-0.3.2-win32.zip"

# Fonction pour télécharger et extraire un fichier ZIP
def telecharger_et_extraire_zip(url, destination_folder):
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {url}...")
        response = requests.get(url, stream=True)
        zip_path = os.path.join(destination_folder, "sm64extend.zip")
        
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

# Fonction pour vérifier et ouvrir sm64extendGUI.exe
def verifier_et_ouvrir_sm64extend():
    if os.path.exists(chemin_sm64extend_exe):
        try:
            # Ouvre sm64extendGUI.exe
            subprocess.Popen([chemin_sm64extend_exe])
            print(f"{nom_sm64extend_exe} a été ouvert avec succès.")
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {nom_sm64extend_exe} : {e}")
    else:
        print(f"Le fichier {nom_sm64extend_exe} n'existe pas.")
        installer_sm64extend()

# Fonction pour télécharger, extraire et ouvrir sm64extendGUI.exe si nécessaire
def installer_sm64extend():
    print(f"Téléchargement et installation de {sm64extend_zip_url}...")
    if telecharger_et_extraire_zip(sm64extend_zip_url, dossier_installation):
        if os.path.exists(chemin_sm64extend_exe):
            try:
                # Ouvre sm64extendGUI.exe après installation
                subprocess.Popen([chemin_sm64extend_exe])
                print(f"{nom_sm64extend_exe} a été installé et ouvert avec succès.")
            except OSError as e:
                print(f"Erreur lors de l'ouverture de {nom_sm64extend_exe} après installation : {e}")
        else:
            print(f"Le fichier {nom_sm64extend_exe} n'a pas été trouvé après extraction du ZIP.")
    else:
        print("Impossible de télécharger et extraire sm64extend-0.3.2-win32.zip depuis le lien spécifié.")

# Vérification et tentative d'ouverture de sm64extendGUI.exe
verifier_et_ouvrir_sm64extend()
