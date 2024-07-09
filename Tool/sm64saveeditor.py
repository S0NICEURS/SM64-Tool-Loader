import os
import subprocess
import requests
import py7zr
import tempfile

# URL pour télécharger SM64SaveEditor-windows-x64-v1.2.0.7z
sm64_url = "https://github.com/MaikelChan/SM64SaveEditor/releases/download/v1.2.0/SM64SaveEditor-windows-x64-v1.2.0.7z"

# Nom du fichier exécutable à extraire
sm64_exe_name = "SM64SaveEditor.exe"

# Chemin où vous souhaitez télécharger le fichier .7z
download_folder = os.path.join(os.path.dirname(__file__), "downloads")

# Chemin où vous souhaitez placer SM64SaveEditor.exe
extract_folder = os.path.join(os.path.dirname(__file__), "SM64SaveEditor")

# Vérifier si le dossier extract_folder existe, sinon le créer
os.makedirs(extract_folder, exist_ok=True)

# Fonction pour vérifier l'existence de SM64SaveEditor.exe et l'ouvrir si présent
def ouvrir_sm64_save_editor():
    sm64_exe = os.path.join(extract_folder, sm64_exe_name)
    if os.path.exists(sm64_exe):
        try:
            subprocess.Popen([sm64_exe])
            return True
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {sm64_exe_name} : {e}")
            return False
    else:
        print(f"Le fichier {sm64_exe_name} n'existe pas.")
        return False

# Fonction pour télécharger, extraire et ouvrir SM64SaveEditor.exe à partir de l'archive .7z
def telecharger_extraire_et_ouvrir_sm64():
    try:
        # Téléchargement du fichier .7z
        print(f"Téléchargement de {sm64_url}...")
        response = requests.get(sm64_url, stream=True)
        
        # Création d'un dossier temporaire pour sauvegarder le contenu du .7z
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    tmp_file.write(chunk)
            temp_filename = tmp_file.name
        
        # Extraction du fichier SM64SaveEditor.exe du .7z dans un dossier temporaire
        with py7zr.SevenZipFile(temp_filename, mode='r') as z:
            # Extraction de tous les fichiers dans un dossier temporaire
            z.extractall(extract_folder)
        
        # Fermeture et suppression du fichier temporaire après extraction
        os.remove(temp_filename)
        
        print("SM64SaveEditor a été téléchargé, extrait et déplacé avec succès.")
        
        # Renommer le dossier extract_folder en SM64SaveEditor
        os.rename(extract_folder, os.path.join(os.path.dirname(__file__), "SM64SaveEditor"))
        
        # Ouvrir SM64SaveEditor.exe
        ouvrir_sm64_save_editor()
        
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de SM64SaveEditor : {e}")
        return False

# Exécution de la fonction pour télécharger, extraire et ouvrir SM64SaveEditor.exe
if not ouvrir_sm64_save_editor():
    telecharger_extraire_et_ouvrir_sm64()
