import os
import requests
import zipfile
import subprocess
import shutil

# Chemin vers le fichier N64SoundListTool.exe dans le dossier N64SoundListTool
chemin_n64soundlisttool_exe = os.path.join(os.path.dirname(__file__), 'N64SoundListTool', 'Release', 'N64SoundListTool.exe')

# URL pour télécharger N64SoundTools.zip
n64soundtools_zip_url = "https://github.com/derselbst/N64SoundTools/archive/refs/heads/master.zip"

# Fonction pour télécharger et extraire le dossier Release depuis N64SoundTools.zip
def telecharger_et_extraire_release():
    try:
        # Téléchargement du fichier ZIP
        print(f"Téléchargement de {n64soundtools_zip_url}...")
        response = requests.get(n64soundtools_zip_url, stream=True)
        zip_path = os.path.join(os.path.dirname(__file__), "N64SoundTools.zip")
        
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        # Extraction du fichier ZIP
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(os.path.dirname(__file__))
        
        # Déplacer le dossier Release extrait vers le dossier souhaité
        extrait_dossier = os.path.join(os.path.dirname(__file__), 'N64SoundTools-master', 'N64SoundListTool', 'Release')
        cible_dossier = os.path.join(os.path.dirname(__file__), 'N64SoundListTool', 'Release')
        
        os.makedirs(os.path.dirname(cible_dossier), exist_ok=True)
        
        if os.path.exists(cible_dossier):
            shutil.rmtree(cible_dossier)
        
        shutil.move(extrait_dossier, cible_dossier)
        
        # Supprimer le dossier temporaire N64SoundTools-master
        shutil.rmtree(os.path.join(os.path.dirname(__file__), 'N64SoundTools-master'))
        
        # Suppression du fichier ZIP après extraction
        os.remove(zip_path)
        
        print("Le dossier Release a été téléchargé et extrait avec succès.")
        ouvrir_n64soundlisttool_exe()  # Appel pour ouvrir N64SoundListTool.exe après extraction
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction du dossier Release : {e}")
        return False

# Fonction pour ouvrir N64SoundListTool.exe
def ouvrir_n64soundlisttool_exe():
    try:
        if os.path.exists(chemin_n64soundlisttool_exe):
            subprocess.Popen([chemin_n64soundlisttool_exe], cwd=os.path.dirname(chemin_n64soundlisttool_exe))
            print(f"{chemin_n64soundlisttool_exe} a été ouvert avec succès.")
        else:
            print(f"Le fichier {chemin_n64soundlisttool_exe} n'existe toujours pas.")
    except OSError as e:
        print(f"Erreur lors de l'ouverture de N64SoundListTool.exe : {e}")

# Vérification si le fichier N64SoundListTool.exe existe
if os.path.exists(chemin_n64soundlisttool_exe):
    ouvrir_n64soundlisttool_exe()
else:
    print("Le fichier N64SoundListTool.exe n'existe pas dans ce dossier.")
    # Télécharger et extraire N64SoundListTool.exe car il n'existe pas localement
    if not telecharger_et_extraire_release():
        print("Impossible de télécharger et extraire le dossier Release depuis le lien spécifié.")
