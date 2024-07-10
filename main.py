from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
import subprocess
import requests
import json

# Chemin vers le fichier JSON pour les raccourcis personnalisés
CUSTOM_SHORTCUTS_FILE = "custom_shortcuts.json"

class CreateShortcutWindow:
    def __init__(self, parent):
        self.parent = parent
        self.create_shortcut_window = Toplevel(parent)
        self.create_shortcut_window.geometry('400x200')
        self.create_shortcut_window.title('Create Custom Shortcut')
        self.create_shortcut_window.transient(parent)  # Pour lier la fenêtre enfant à la fenêtre parente
        self.create_shortcut_window.grab_set()  # Pour rendre la fenêtre parente inactive pendant que celle-ci est ouverte
        
        self.exe_path_var = StringVar()
        self.shortcut_name_var = StringVar()
        
        Label(self.create_shortcut_window, text="Executable Path:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_exe_path = Entry(self.create_shortcut_window, textvariable=self.exe_path_var, width=30)
        self.entry_exe_path.grid(row=0, column=1, padx=10, pady=10)
        Button(self.create_shortcut_window, text="Browse", command=self.select_executable).grid(row=0, column=2, padx=10, pady=10)
        
        Label(self.create_shortcut_window, text="Shortcut Name:").grid(row=1, column=0, padx=10, pady=10)
        Entry(self.create_shortcut_window, textvariable=self.shortcut_name_var, width=30).grid(row=1, column=1, padx=10, pady=10)
        
        Button(self.create_shortcut_window, text="Create Shortcut", command=self.create_shortcut).grid(row=2, column=1, padx=10, pady=10)
    
    def select_executable(self):
        exe_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
        if exe_path:
            self.exe_path_var.set(exe_path)
    
    def create_shortcut(self):
        exe_path = self.exe_path_var.get()
        shortcut_name = self.shortcut_name_var.get()
        
        if exe_path and shortcut_name:
            shortcut_data = {"exe_path": exe_path, "shortcut_name": shortcut_name}
            self.save_shortcut(shortcut_data)
            messagebox.showinfo("Success", f"Shortcut '{shortcut_name}' created successfully.")
            update_custom_load_buttons()  # Mettre à jour les boutons Custom Load
            self.exe_path_var.set("")
            self.shortcut_name_var.set("")
            self.create_shortcut_window.destroy()  # Fermer la fenêtre après la création du raccourci
        else:
            messagebox.showerror("Error", "Please fill in both fields.")
    
    def save_shortcut(self, data):
        try:
            with open(CUSTOM_SHORTCUTS_FILE, "r") as f:
                shortcuts = json.load(f)
        except FileNotFoundError:
            shortcuts = []
        
        shortcuts.append(data)
        
        with open(CUSTOM_SHORTCUTS_FILE, "w") as f:
            json.dump(shortcuts, f, indent=4)

def update_custom_load_buttons():
    try:
        with open(CUSTOM_SHORTCUTS_FILE, "r") as f:
            shortcuts = json.load(f)
    except FileNotFoundError:
        shortcuts = []
    
    # Effacer tous les boutons Custom Load précédents
    for widget in custom_load_frame.winfo_children():
        widget.destroy()
    
    if shortcuts:
        for shortcut in shortcuts:
            shortcut_name = shortcut["shortcut_name"]
            btn_frame = Frame(custom_load_frame, bg='#492E87')
            btn_frame.pack(side=LEFT, padx=5, pady=5)
            
            btn = Button(btn_frame, text=shortcut_name, command=lambda name=shortcut_name: open_custom_shortcut(name))
            btn.pack(side=TOP)
            
            delete_btn = Button(btn_frame, text="Delete", command=lambda name=shortcut_name: delete_custom_shortcut(name))
            delete_btn.pack(side=BOTTOM, pady=5)
    else:
        # Ne rien afficher si pas de raccourcis trouvés
        pass

def open_custom_shortcut(shortcut_name):
    with open(CUSTOM_SHORTCUTS_FILE, "r") as f:
        shortcuts = json.load(f)
        
    for shortcut in shortcuts:
        if shortcut["shortcut_name"] == shortcut_name:
            exe_path = shortcut["exe_path"]
            subprocess.Popen([exe_path])
            return

def delete_custom_shortcut(shortcut_name):
    try:
        with open(CUSTOM_SHORTCUTS_FILE, "r") as f:
            shortcuts = json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "No custom shortcuts found.")
        return
    
    new_shortcuts = [shortcut for shortcut in shortcuts if shortcut["shortcut_name"] != shortcut_name]
    
    with open(CUSTOM_SHORTCUTS_FILE, "w") as f:
        json.dump(new_shortcuts, f, indent=4)
    
    messagebox.showinfo("Success", f"Shortcut '{shortcut_name}' deleted successfully.")
    update_custom_load_buttons()  # Mettre à jour les boutons Custom Load après la suppression

def open_flips():
    exe_path = os.path.join("Tool", "flips.exe")  # Modifié pour ouvrir flips.exe
    subprocess.Popen([exe_path])

def add_custom_shortcut():
    create_window = CreateShortcutWindow(fenetre)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.geometry('719x513')
fenetre.title('SM64 Tool Loader')
fenetre.config(bg='#492E87')
fenetre.resizable(False, False)  # Fenêtre non redimensionnable

# Chargement de l'image de fond
image_url = "https://i.ibb.co/gWJ77Wg/sm64modmanage-V2.png"
img = Image.open(requests.get(image_url, stream=True).raw)
bg_image = ImageTk.PhotoImage(img)
canvas = Canvas(fenetre, width=720, height=523, bg='#492E87', highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Chargement de l'image du bouton Flips
button_image_url = "https://i.ibb.co/BTdYDNq/flipsv2.png"
button_img = Image.open(requests.get(button_image_url, stream=True).raw)
button_photo = ImageTk.PhotoImage(button_img)

# Placement du bouton Flips au centre
btn_open_flips = Button(fenetre, image=button_photo, command=open_flips, bd=0, highlightthickness=0, relief=FLAT)
btn_open_flips.place(x=(720 - button_photo.width()) // 2, y=(523 - button_photo.height()) // 2 - 4)

# Cadre pour les boutons Custom Load
custom_load_frame = Frame(fenetre, bg='#492E87')
custom_load_frame.place(x=10, y=470)

# Bouton Custom Load pour ajouter un nouveau raccourci
btn_custom_load = Button(fenetre, text="Custom Load", command=add_custom_shortcut)
btn_custom_load.place(x=15, y=430)

# Affichage de l'image de fond sur le canvas
canvas.create_image(0, 0, image=bg_image, anchor=NW)

# Mettre à jour les boutons Custom Load initialement
update_custom_load_buttons()

# Démarrage de la boucle principale Tkinter
fenetre.mainloop()
