import os
import requests
import zipfile
import subprocess

# Chemin vers le dossier où SM64 ROM Manager.exe sera installé
dossier_installation = os.path.dirname(__file__)

# Nom du fichier SM64 ROM Manager.exe dans l'archive ZIP
nom_manager_exe = 'SM64 ROM Manager (v1.14.16)/SM64 ROM Manager.exe'

# Chemin complet vers SM64 ROM Manager.exe
chemin_manager_exe = os.path.join(dossier_installation, nom_manager_exe)

# URL pour télécharger SM64 ROM Manager.zip
sm64_manager_zip_url = "https://cloud.pilzinsel64.de/s/ypi2FqWkAm97coY/download?path=%2F&files=SM64%20ROM%20Manager.zip"

# Fonction pour télécharger et extraire un fichier ZIP
def telecharger_et_extraire_zip(url, destination_folder):
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {url}...")
        response = requests.get(url, stream=True)
        zip_path = os.path.join(destination_folder, "sm64_manager.zip")
        
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

# Fonction pour vérifier et ouvrir SM64 ROM Manager.exe
def verifier_et_ouvrir_manager():
    if os.path.exists(chemin_manager_exe):
        try:
            # Ouvre SM64 ROM Manager.exe
            subprocess.Popen([chemin_manager_exe])
            print(f"{nom_manager_exe} a été ouvert avec succès.")
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {nom_manager_exe} : {e}")
    else:
        print(f"Le fichier {nom_manager_exe} n'existe pas.")
        installer_sm64_manager()

# Fonction pour télécharger, extraire et ouvrir SM64 ROM Manager.exe si nécessaire
def installer_sm64_manager():
    print(f"Téléchargement et installation de {sm64_manager_zip_url}...")
    if telecharger_et_extraire_zip(sm64_manager_zip_url, dossier_installation):
        if os.path.exists(chemin_manager_exe):
            try:
                # Ouvre SM64 ROM Manager.exe après installation
                subprocess.Popen([chemin_manager_exe])
                print(f"{nom_manager_exe} a été installé et ouvert avec succès.")
            except OSError as e:
                print(f"Erreur lors de l'ouverture de {nom_manager_exe} après installation : {e}")
        else:
            print(f"Le fichier {nom_manager_exe} n'a pas été trouvé après extraction du ZIP.")
    else:
        print("Impossible de télécharger et extraire SM64 ROM Manager.zip depuis le lien spécifié.")

# Vérification et tentative d'ouverture de SM64 ROM Manager.exe
verifier_et_ouvrir_manager()
