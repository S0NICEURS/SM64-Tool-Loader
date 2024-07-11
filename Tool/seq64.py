import os
import subprocess

# Fonction pour vérifier l'existence de seq64_gui.exe et l'ouvrir si présent
def ouvrir_seq64_gui(seq64_dir):
    seq64_gui_exe = os.path.join(seq64_dir, 'seq64_gui.exe')
    if os.path.exists(seq64_gui_exe):
        try:
            subprocess.Popen([seq64_gui_exe])
            return True
        except OSError as e:
            print(f"Erreur lors de l'ouverture de seq64_gui.exe : {e}")
            return False
    else:
        print("Le fichier seq64_gui.exe n'existe pas.")
        return False

# Vérification et ouverture de seq64_gui.exe s'il existe déjà
seq64_dir = os.path.join(os.path.dirname(__file__), "seq64v2.3.2")
if not ouvrir_seq64_gui(seq64_dir):
    # Téléchargement et extraction de seq64_v2.3.2.zip si seq64_gui.exe n'existe pas
    import requests
    import zipfile
    
    # URL pour télécharger seq64_v2.3.2.zip
    seq64_zip_url = "https://github.com/sauraen/seq64/releases/download/2.3.2/seq64_v2.3.2.zip"

    def telecharger_et_extraire_seq64():
        try:
            # Téléchargement du fichier ZIP
            print(f"Téléchargement de {seq64_zip_url}...")
            response = requests.get(seq64_zip_url, stream=True)
            zip_path = os.path.join(os.path.dirname(__file__), "seq64_v2.3.2.zip")
            
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            # Création du dossier seq64v2.3.2
            os.makedirs(seq64_dir, exist_ok=True)
            
            # Extraction du fichier ZIP dans le dossier seq64v2.3.2
            with zipfile.ZipFile(zip_path, 'r') as z:
                z.extractall(seq64_dir)
            
            # Suppression du fichier ZIP après extraction
            os.remove(zip_path)
            
            print("seq64_v2.3.2 a été téléchargé et extrait avec succès.")
            ouvrir_seq64_gui(seq64_dir)  # Appel pour ouvrir seq64_gui.exe après extraction
            return True
        except Exception as e:
            print(f"Erreur lors du téléchargement et de l'extraction de seq64_v2.3.2 : {e}")
            return False

    # Exécution de la fonction pour télécharger et extraire seq64_v2.3.2.zip si nécessaire
    telecharger_et_extraire_seq64()
