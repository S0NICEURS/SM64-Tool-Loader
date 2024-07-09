import os
import requests
import zipfile
import subprocess

# Chemin vers le dossier où Quad64.exe sera installé
dossier_installation = os.path.dirname(__file__)

# Nom du fichier Quad64.exe
nom_quad64_exe = 'Quad64 v0.2 (BB5)/Quad64.exe'

# Chemin complet vers Quad64.exe
chemin_quad64_exe = os.path.join(dossier_installation, nom_quad64_exe)

# URL pour télécharger Quad64.v0.2.BB5.zip depuis GitHub
quad64_zip_url = "https://github.com/DavidSM64/Quad64/releases/download/v0.2-beta-5/Quad64.v0.2.BB5.zip"

# Fonction pour télécharger et extraire un fichier ZIP
def telecharger_et_extraire_zip(url, destination_folder):
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {url}...")
        response = requests.get(url, stream=True)
        zip_path = os.path.join(destination_folder, "Quad64.v0.2.BB5.zip")
        
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

# Fonction pour vérifier et ouvrir Quad64.exe
def verifier_et_ouvrir_quad64():
    if os.path.exists(chemin_quad64_exe):
        try:
            # Ouvre Quad64.exe
            subprocess.Popen([chemin_quad64_exe])
            print(f"{nom_quad64_exe} a été ouvert avec succès.")
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {nom_quad64_exe} : {e}")
    else:
        print(f"Le fichier {nom_quad64_exe} n'existe pas.")
        installer_quad64()

# Fonction pour télécharger, extraire et ouvrir Quad64.exe si nécessaire
def installer_quad64():
    print(f"Téléchargement et installation de {quad64_zip_url}...")
    if telecharger_et_extraire_zip(quad64_zip_url, dossier_installation):
        if os.path.exists(chemin_quad64_exe):
            try:
                # Ouvre Quad64.exe après installation
                subprocess.Popen([chemin_quad64_exe])
                print(f"{nom_quad64_exe} a été installé et ouvert avec succès.")
            except OSError as e:
                print(f"Erreur lors de l'ouverture de {nom_quad64_exe} après installation : {e}")
        else:
            print(f"Le fichier {nom_quad64_exe} n'a pas été trouvé après extraction du ZIP.")
    else:
        print("Impossible de télécharger et extraire Quad64.v0.2.BB5.zip depuis le lien spécifié.")

# Vérification et tentative d'ouverture de Quad64.exe
verifier_et_ouvrir_quad64()

