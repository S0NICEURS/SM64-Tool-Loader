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
        exe_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if exe_path:
            self.exe_path_var.set(exe_path)
    
    def create_shortcut(self):
        exe_path = self.exe_path_var.get()
        shortcut_name = self.shortcut_name_var.get()
        
        if exe_path and shortcut_name:
            shortcut_data = {"exe_path": exe_path, "shortcut_name": shortcut_name}
            self.save_shortcut(shortcut_data)
            messagebox.showinfo("Success", f"Shortcut '{shortcut_name}' created successfully.")
            update_custom_load_menu(shortcut_name)
            self.exe_path_var.set("")
            self.shortcut_name_var.set("")
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

def update_custom_load_menu_from_file():
    try:
        with open(CUSTOM_SHORTCUTS_FILE, "r") as f:
            shortcuts = json.load(f)
    except FileNotFoundError:
        shortcuts = []
    
    for shortcut in shortcuts:
        shortcut_name = shortcut["shortcut_name"]
        update_custom_load_menu(shortcut_name)

def update_custom_load_menu(shortcut_name):
    custom_menu.add_command(label=shortcut_name, command=lambda: open_custom_shortcut(shortcut_name))

def open_custom_shortcut(shortcut_name):
    with open(CUSTOM_SHORTCUTS_FILE, "r") as f:
        shortcuts = json.load(f)
        
    for shortcut in shortcuts:
        if shortcut["shortcut_name"] == shortcut_name:
            exe_path = shortcut["exe_path"]
            subprocess.Popen(["python", exe_path])
            return

def open_flips():
    exe_path = os.path.join("Tool", "flips.py")
    subprocess.Popen(["python", exe_path])

fenetre = Tk()
fenetre.geometry('719x513')
fenetre.title('SM64 Tool Loader')
fenetre.config(bg='#492E87')
fenetre.resizable(False, False)  # Fenêtre fixée

image_url = "https://i.ibb.co/gWJ77Wg/sm64modmanage-V2.png"
img = Image.open(requests.get(image_url, stream=True).raw)
bg_image = ImageTk.PhotoImage(img)
canvas = Canvas(fenetre, width=720, height=523, bg='#492E87', highlightthickness=0)
canvas.pack(fill='both', expand=True)

button_image_url = "https://i.ibb.co/BTdYDNq/flipsv2.png"
button_img = Image.open(requests.get(button_image_url, stream=True).raw)
button_photo = ImageTk.PhotoImage(button_img)

# Centrer le bouton au milieu de la fenêtre
btn_open_flips = Button(fenetre, image=button_photo, command=open_flips, bd=0, highlightthickness=0, relief=FLAT)
btn_open_flips.place(x=(720 - button_photo.width()) // 2, y=(523 - button_photo.height()) // 2 - 4)

menubar = Menu(fenetre, font=('Arial', 14))
custom_menu = Menu(menubar, tearoff=0, font=('Arial', 10, 'bold italic'))
custom_menu.add_command(label="Create Shortcut Load", command=lambda: CreateShortcutWindow(fenetre))
menubar.add_cascade(label="Custom Load", menu=custom_menu)
fenetre.config(menu=menubar)

update_custom_load_menu_from_file()
canvas.create_image(0, 0, image=bg_image, anchor=NW)

fenetre.mainloop()


