import os
import requests
import zipfile
import subprocess

# Chemin vers le fichier HxD.exe dans le même dossier que ce script
chemin_hxd_exe = os.path.join(os.path.dirname(__file__), 'HxD.exe')

# URL pour télécharger HxD_portable.zip
hxd_zip_url = "https://dl.smwcentral.net/4625/HxD_portable.zip"

# Fonction pour télécharger et extraire HxD.exe depuis HxD_portable.zip si nécessaire
def telecharger_et_extraire_hxd():
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {hxd_zip_url}...")
        response = requests.get(hxd_zip_url, stream=True)
        zip_path = os.path.join(os.path.dirname(__file__), "HxD_portable.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Extraction de HxD.exe du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extract("HxD.exe", os.path.dirname(__file__))
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print("HxD.exe a été téléchargé et extrait avec succès.")
        ouvrir_hxd_exe()  # Appel pour ouvrir HxD.exe après extraction
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de HxD.exe : {e}")
        return False

# Fonction pour ouvrir HxD.exe
def ouvrir_hxd_exe():
    try:
        subprocess.Popen([chemin_hxd_exe])
    except OSError as e:
        print(f"Erreur lors de l'ouverture de HxD.exe : {e}")

# Vérification si le fichier HxD.exe existe
if os.path.exists(chemin_hxd_exe):
    try:
        subprocess.Popen([chemin_hxd_exe])
    except OSError as e:
        print(f"Erreur lors de l'ouverture de HxD.exe : {e}")
        # Si une erreur se produit, tenter de télécharger et extraire HxD.exe
        if not telecharger_et_extraire_hxd():
            print("Impossible de télécharger et extraire HxD.exe.")
else:
    print("Le fichier HxD.exe n'existe pas dans ce dossier.")
    # Télécharger et extraire HxD.exe car il n'existe pas localement
    if not telecharger_et_extraire_hxd():
        print("Impossible de télécharger et extraire HxD.exe depuis le lien spécifié.")

