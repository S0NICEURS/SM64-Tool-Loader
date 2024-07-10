import os
import requests
import zipfile
import subprocess

# URL pour télécharger SM64Mus.zip
sm64mus_zip_url = "https://github.com/dylanpdx/SM64Mus/releases/download/0.1/SM64Mus.zip"

# Dossier où le fichier ZIP sera téléchargé et extrait
sm64mus_dir = os.path.join(os.path.dirname(__file__), 'SM64Mus')

# Chemin vers le fichier SM64Mus.exe après extraction
chemin_sm64mus_exe = os.path.join(sm64mus_dir, 'SM64Mus.exe')

# Fonction pour télécharger et extraire SM64Mus.zip si nécessaire
def telecharger_et_extraire_sm64mus():
    try:
        # Création du dossier SM64Mus s'il n'existe pas
        if not os.path.exists(sm64mus_dir):
            os.makedirs(sm64mus_dir)

        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {sm64mus_zip_url}...")
        response = requests.get(sm64mus_zip_url, stream=True)
        zip_path = os.path.join(sm64mus_dir, "SM64Mus.zip")

        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        # Extraction de SM64Mus.exe du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(sm64mus_dir)

        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)

        print("SM64Mus.exe a été téléchargé et extrait avec succès.")
        ouvrir_sm64mus_exe()  # Appel pour ouvrir SM64Mus.exe après extraction
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de SM64Mus.exe : {e}")
        return False

# Fonction pour ouvrir SM64Mus.exe
def ouvrir_sm64mus_exe():
    try:
        subprocess.Popen([chemin_sm64mus_exe], cwd=sm64mus_dir)
    except OSError as e:
        print(f"Erreur lors de l'ouverture de SM64Mus.exe : {e}")

# Vérification si le fichier SM64Mus.exe existe
if os.path.exists(chemin_sm64mus_exe):
    try:
        subprocess.Popen([chemin_sm64mus_exe], cwd=sm64mus_dir)
    except OSError as e:
        print(f"Erreur lors de l'ouverture de SM64Mus.exe : {e}")
        # Si une erreur se produit, tenter de télécharger et extraire SM64Mus.exe
        if not telecharger_et_extraire_sm64mus():
            print("Impossible de télécharger et extraire SM64Mus.exe.")
else:
    print("Le fichier SM64Mus.exe n'existe pas dans ce dossier.")
    # Télécharger et extraire SM64Mus.exe car il n'existe pas localement
    if not telecharger_et_extraire_sm64mus():
        print("Impossible de télécharger et extraire SM64Mus.exe depuis le lien spécifié.")