import subprocess
import importlib

# Modules à vérifier et installer si nécessaire
required_modules = [
    'tkinter',
    'pillow',
    'requests',
    'json',
    'ctypes',
    'zipfile',
    'shutil',
    'subprocess',
    'urllib.request',
    'threading',
    'tempfile',
]

# Vérifier et installer les modules nécessaires
for module in required_modules:
    try:
        importlib.import_module(module)
        print(f"{module} is already installed.")
    except ImportError:
        print(f"{module} is not installed, install in progress...")
        subprocess.check_call(['pip', 'install', module])

# Une fois les modules installés, ouvrir SM64 Tool Loader.py
subprocess.run(['python', 'SM64 Tool Loader.py'])
