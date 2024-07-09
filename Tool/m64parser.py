import os
import requests
import zipfile
import subprocess

# Chemin vers le dossier où M64Parser_GUI.exe sera installé
dossier_installation = os.path.dirname(__file__)

# Nom du fichier M64Parser_GUI.exe dans l'archive ZIP
nom_parser_exe = 'M64 Parser 0.9/M64Parser_GUI.exe'

# Chemin complet vers M64Parser_GUI.exe
chemin_parser_exe = os.path.join(dossier_installation, nom_parser_exe)

# URL pour télécharger M64 Parser 0.9.zip
m64_parser_zip_url = "https://dl.smwcentral.net/13234/M64%20Parser%200.9.zip"

# Fonction pour télécharger et extraire un fichier ZIP
def telecharger_et_extraire_zip(url, destination_folder):
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {url}...")
        response = requests.get(url, stream=True)
        zip_path = os.path.join(destination_folder, "m64_parser.zip")
        
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

# Fonction pour vérifier et ouvrir M64Parser_GUI.exe
def verifier_et_ouvrir_parser():
    if os.path.exists(chemin_parser_exe):
        try:
            # Ouvre M64Parser_GUI.exe
            subprocess.Popen([chemin_parser_exe])
            print(f"{nom_parser_exe} a été ouvert avec succès.")
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {nom_parser_exe} : {e}")
    else:
        print(f"Le fichier {nom_parser_exe} n'existe pas.")
        installer_m64_parser()

# Fonction pour télécharger, extraire et ouvrir M64Parser_GUI.exe si nécessaire
def installer_m64_parser():
    print(f"Téléchargement et installation de {m64_parser_zip_url}...")
    if telecharger_et_extraire_zip(m64_parser_zip_url, dossier_installation):
        if os.path.exists(chemin_parser_exe):
            try:
                # Ouvre M64Parser_GUI.exe après installation
                subprocess.Popen([chemin_parser_exe])
                print(f"{nom_parser_exe} a été installé et ouvert avec succès.")
            except OSError as e:
                print(f"Erreur lors de l'ouverture de {nom_parser_exe} après installation : {e}")
        else:
            print(f"Le fichier {nom_parser_exe} n'a pas été trouvé après extraction du ZIP.")
    else:
        print("Impossible de télécharger et extraire M64 Parser 0.9.zip depuis le lien spécifié.")

# Vérification et tentative d'ouverture de M64Parser_GUI.exe
verifier_et_ouvrir_parser()
