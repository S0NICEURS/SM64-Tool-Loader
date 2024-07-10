import os
import subprocess
import urllib.request
import tempfile

# Définir les chemins de fichiers
username = os.getenv('USERNAME')
project64_path = f"C:\\Users\\{username}\\AppData\\Local\\Project64\\Project64.exe"
installer_url = "https://github.com/Rosalie241/BetterMajorasMaskInstaller/releases/download/4.1.0/BetterMajorasMaskInstaller.exe"

def run_executable(path):
    try:
        result = subprocess.run([path], check=True)
        print(f"Executed {path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {path}. Error: {e}")

# Vérifier si Project64.exe existe
if os.path.exists(project64_path):
    print(f"Found Project64.exe at {project64_path}.")
    # Exécuter Project64.exe
    run_executable(project64_path)
else:
    print(f"Project64.exe not found at {project64_path}. Downloading installer...")

    # Créer un répertoire temporaire
    with tempfile.TemporaryDirectory() as temp_dir:
        installer_path = os.path.join(temp_dir, "BetterMajorasMaskInstaller.exe")
        
        # Télécharger l'installateur
        urllib.request.urlretrieve(installer_url, installer_path)
        print(f"Downloaded BetterMajorasMaskInstaller.exe to {installer_path}.")
        
        # Exécuter l'installateur
        run_executable(installer_path)