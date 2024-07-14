import os
import requests
import zipfile
import subprocess

# Chemin vers le fichier SM64SaveEditor.exe dans le dossier SM64 Save Editor
chemin_sm64saveeditor_exe = os.path.join(os.path.dirname(__file__), 'SM64 Save Editor', 'SM64SaveEditor.exe')

# URL pour télécharger SM64 Save Editor.zip
sm64saveeditor_zip_url = "https://archive.org/download/sm64-save-editor/SM64%20Save%20Editor.zip"

# Fonction pour télécharger et extraire SM64SaveEditor.exe depuis SM64 Save Editor.zip
def telecharger_et_extraire_save_editor():
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {sm64saveeditor_zip_url}...")
        response = requests.get(sm64saveeditor_zip_url, stream=True)
        zip_path = os.path.join(os.path.dirname(__file__), "SM64SaveEditor.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Extraction du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(os.path.dirname(__file__))
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print("SM64 Save Editor a été téléchargé et extrait avec succès.")
        ouvrir_sm64saveeditor_exe()  # Ouvrir SM64SaveEditor.exe après extraction
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de SM64SaveEditor : {e}")

# Fonction pour ouvrir SM64SaveEditor.exe
def ouvrir_sm64saveeditor_exe():
    try:
        if os.path.exists(chemin_sm64saveeditor_exe):
            subprocess.Popen([chemin_sm64saveeditor_exe], cwd=os.path.dirname(chemin_sm64saveeditor_exe))
            print(f"{chemin_sm64saveeditor_exe} a été ouvert avec succès.")
        else:
            print(f"Le fichier {chemin_sm64saveeditor_exe} n'existe toujours pas.")
    except OSError as e:
        print(f"Erreur lors de l'ouverture de SM64SaveEditor.exe : {e}")

# Vérification si le fichier SM64SaveEditor.exe existe
if os.path.exists(chemin_sm64saveeditor_exe):
    ouvrir_sm64saveeditor_exe()
else:
    print("Le fichier SM64SaveEditor.exe n'existe pas dans ce dossier.")
    # Télécharger et extraire SM64SaveEditor.exe car il n'existe pas localement
    telecharger_et_extraire_save_editor()
