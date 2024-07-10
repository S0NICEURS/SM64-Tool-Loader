import os
import subprocess
import requests
import py7zr
import tempfile

# URL pour télécharger N64.Midi.Tool.7z
n64_url = "https://github.com/jombo23/N64-Tools/releases/download/3ae0013/N64.Midi.Tool.7z"

# Nom du fichier exécutable à extraire
n64_exe_name = "N64MidiTool.exe"

# Chemin où vous souhaitez placer N64MidiTool.exe
extract_folder = os.path.join(os.path.dirname(__file__), "N64MidiTool")

# Chemin complet du fichier exécutable
n64_exe_path = os.path.join(extract_folder, "Release", n64_exe_name)

# Vérifier si le dossier extract_folder existe, sinon le créer
os.makedirs(extract_folder, exist_ok=True)

# Fonction pour vérifier l'existence de N64MidiTool.exe et l'ouvrir si présent
def ouvrir_n64_midi_tool():
    if os.path.exists(n64_exe_path):
        try:
            subprocess.Popen([n64_exe_path], cwd=os.path.dirname(n64_exe_path))
            return True
        except OSError as e:
            print(f"Erreur lors de l'ouverture de {n64_exe_name} : {e}")
            return False
    else:
        print(f"Le fichier {n64_exe_name} n'existe pas.")
        return False

# Fonction pour télécharger, extraire et ouvrir N64MidiTool.exe à partir de l'archive .7z
def telecharger_extraire_et_ouvrir_n64():
    try:
        # Téléchargement du fichier .7z
        print(f"Téléchargement de {n64_url}...")
        response = requests.get(n64_url, stream=True)
        
        # Création d'un dossier temporaire pour sauvegarder le contenu du .7z
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    tmp_file.write(chunk)
            temp_filename = tmp_file.name
        
        # Extraction du fichier N64MidiTool.exe du .7z dans le dossier extract_folder
        with py7zr.SevenZipFile(temp_filename, mode='r') as z:
            z.extractall(extract_folder)
        
        # Fermeture et suppression du fichier temporaire après extraction
        os.remove(temp_filename)
        
        print("N64MidiTool a été téléchargé et extrait avec succès.")
        
        # Ouvrir N64MidiTool.exe
        ouvrir_n64_midi_tool()
        
        return True
    except Exception as e:
        print(f"Erreur lors du téléchargement et de l'extraction de N64MidiTool : {e}")
        return False

# Exécution de la fonction pour télécharger, extraire et ouvrir N64MidiTool.exe
if not ouvrir_n64_midi_tool():
    telecharger_extraire_et_ouvrir_n64()