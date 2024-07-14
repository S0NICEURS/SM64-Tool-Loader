import os
import requests
import zipfile
import subprocess

# Chemin vers le fichier N64SoundbankTool.exe dans le dossier N64 Soudbank Tool
chemin_n64soundbanktool_exe = os.path.join(os.path.dirname(__file__), 'N64 Soudbank Tool', 'N64SoundbankTool.exe')

# URL pour télécharger N64 Soundbank Tool.zip
n64soundbanktool_zip_url = "https://archive.org/download/n64-soudbank-tool/N64%20Soudbank%20Tool.zip"

# Fonction pour télécharger et extraire N64SoundbankTool.exe depuis N64 Soundbank Tool.zip
def telecharger_et_extraire_soundbank_tool():
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {n64soundbanktool_zip_url}...")
        response = requests.get(n64soundbanktool_zip_url, stream=True)
        zip_path = os.path.join(os.path.dirname(__file__), "N64SoundbankTool.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Extraction du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(os.path.dirname(__file__))
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print("N64 Soundbank Tool a été téléchargé et extrait avec succès.")
        ouvrir_n64soundbanktool_exe()  # Ouvrir N64SoundbankTool.exe après extraction
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de N64SoundbankTool : {e}")

# Fonction pour ouvrir N64SoundbankTool.exe
def ouvrir_n64soundbanktool_exe():
    try:
        if os.path.exists(chemin_n64soundbanktool_exe):
            subprocess.Popen([chemin_n64soundbanktool_exe], cwd=os.path.dirname(chemin_n64soundbanktool_exe))
            print(f"{chemin_n64soundbanktool_exe} a été ouvert avec succès.")
        else:
            print(f"Le fichier {chemin_n64soundbanktool_exe} n'existe toujours pas.")
    except OSError as e:
        print(f"Erreur lors de l'ouverture de N64SoundbankTool.exe : {e}")

# Vérification si le fichier N64SoundbankTool.exe existe
if os.path.exists(chemin_n64soundbanktool_exe):
    ouvrir_n64soundbanktool_exe()
else:
    print("Le fichier N64SoundbankTool.exe n'existe pas dans ce dossier.")
    # Télécharger et extraire N64SoundbankTool.exe car il n'existe pas localement
    telecharger_et_extraire_soundbank_tool()
