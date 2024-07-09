import os
import requests
import zipfile
import subprocess

# Chemin vers le dossier où SM64 Editor.exe sera installé
dossier_installation = os.path.dirname(__file__)

# Nom du fichier SM64 Editor.exe
nom_sm64editor_exe = 'SM64 Editor 2.2/SM64 Editor.exe'

# Chemin complet vers SM64 Editor.exe
chemin_sm64editor_exe = os.path.join(dossier_installation, nom_sm64editor_exe)

# URL pour télécharger SM64 Editor 2.2.zip
sm64editor_zip_url = "http://pabloscorner.akawah.net/SM64EditorArchive/SM64%20Editor%202.2.zip"

# Fonction pour télécharger et extraire un fichier ZIP
def telecharger_et_extraire_zip(url, destination_folder):
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {url}...")
        response = requests.get(url, stream=True)
        zip_path = os.path.join(destination_folder, "sm64editor.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Vérification que le fichier ZIP est téléchargé correctement
        if not zipfile.is_zipfile(zip_path):
            raise zipfile.BadZipFile(f"Le fichier téléchargé n'est pas un fichier ZIP valide : {zip_path}")
        
        # Extraction du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(destination_folder)
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print(f"Le fichier ZIP a été téléchargé et extrait avec succès dans {destination_folder}.")
        return True
    except (requests.RequestException, zipfile.BadZipFile) as e:
        print(f"Erreur lors du téléchargement et de l'extraction du fichier ZIP : {e}")
        return False

# Fonction pour vérifier et ouvrir SM64 Editor.exe
def verifier_et_ouvrir_sm64editor():
    if os.path.exists(chemin_sm64editor_exe):
        try:
            # Ouvre SM64 Editor.exe
            subprocess.Popen([chemin_sm64editor_exe])
            print(f"{nom_sm64editor_exe} a été ouvert avec succès.")
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {nom_sm64editor_exe} : {e}")
    else:
        print(f"Le fichier {nom_sm64editor_exe} n'existe pas.")
        installer_sm64editor()

# Fonction pour télécharger, extraire et ouvrir SM64 Editor.exe si nécessaire
def installer_sm64editor():
    print(f"Téléchargement et installation de {sm64editor_zip_url}...")
    if telecharger_et_extraire_zip(sm64editor_zip_url, dossier_installation):
        if os.path.exists(chemin_sm64editor_exe):
            try:
                # Ouvre SM64 Editor.exe après installation
                subprocess.Popen([chemin_sm64editor_exe])
                print(f"{nom_sm64editor_exe} a été installé et ouvert avec succès.")
            except OSError as e:
                print(f"Erreur lors de l'ouverture de {nom_sm64editor_exe} après installation : {e}")
        else:
            print(f"Le fichier {nom_sm64editor_exe} n'a pas été trouvé après extraction du ZIP.")
    else:
        print("Impossible de télécharger et extraire SM64 Editor 2.2.zip depuis le lien spécifié.")

# Vérification et tentative d'ouverture de SM64 Editor.exe
verifier_et_ouvrir_sm64editor()
