from tkinter import *
from tkinter import messagebox, filedialog, Menu
from PIL import Image, ImageTk
import os
import subprocess
import requests
import json
import ctypes  # To hide the console window

# Path to the JSON file for custom shortcuts
CUSTOM_SHORTCUTS_FILE = "custom_shortcuts.json"

class CreateShortcutWindow:
    def __init__(self, parent):
        self.parent = parent
        self.create_shortcut_window = Toplevel(parent)
        self.create_shortcut_window.geometry('400x200')
        self.create_shortcut_window.title('Create Custom Shortcut')
        self.create_shortcut_window.transient(parent)
        self.create_shortcut_window.grab_set()
        
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
            update_custom_load_buttons()
            self.exe_path_var.set("")
            self.shortcut_name_var.set("")
            self.create_shortcut_window.destroy()
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
    
    for widget in custom_load_frame.winfo_children():
        widget.destroy()
    
    if shortcuts:
        for shortcut in shortcuts:
            shortcut_name = shortcut["shortcut_name"]
            btn_frame = Frame(custom_load_frame, bg='#492E87')
            btn_frame.pack(side=LEFT, padx=5, pady=5)
            
            btn = Button(btn_frame, text=shortcut_name, command=lambda name=shortcut_name: open_custom_shortcut(name), bd=0, relief=FLAT)
            btn.pack(side=TOP)
            
            delete_btn = Button(btn_frame, text="Delete", command=lambda name=shortcut_name: delete_custom_shortcut(name), bd=0, relief=FLAT)
            delete_btn.pack(side=BOTTOM, pady=5)

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
    update_custom_load_buttons()

def open_flips():
    script_path = os.path.join("Tool", "flips.py")
    subprocess.Popen(["python", script_path])

def add_custom_shortcut():
    create_window = CreateShortcutWindow(fenetre)

def open_p64():
    script_path = os.path.join("Redistributables", "p64.py")
    subprocess.Popen(["python", script_path])

def open_vcredist():
    script_path = os.path.join("Redistributables", "vcredist.py")
    subprocess.Popen(["python", script_path])

def execute_selected_item(selection):
    script_paths = {
        "SM64 Extend": "sm64extend.py",
        "SM64 Rom Manager": "sm64rommanager.py",
        "SM64 Editor": "sm64editor.py",
        "SM64 Tweaker": "sm64tweaker.py",
        "HxD": "hxd.py",
        "Seq64": "seq64.py",
        "Quad64 v0.2": "quad64v0.2.py",
        "Quad64 v0.3": "quad64v0.3.py",
        "N64 Sound Tool": "n64soundtool.py",
        "N64 Soundbank Tool": "n64soundbanktool.py",
        "N64 Midi Tool": "pip install py7zr",
        "M64 Parser": "m64parser.py",
        "SM64 Mus": "sm64mus.py",
        "SM64 Save Editor": "sm64saveeditor.py",
    }
    
    if selection in script_paths:
        script_path = script_paths[selection]
        if script_path.endswith(".py"):
            script_path = os.path.join("Tool", script_path)
            subprocess.Popen(["python", script_path])
        else:
            subprocess.Popen(script_path.split())
    else:
        messagebox.showerror("Error", f"No script found for {selection}")

def execute_items_general(event=None):
    items_general = [
        "SM64 Extend", "SM64 Rom Manager", "SM64 Editor", "SM64 Tweaker", "HxD", "Seq64"
    ]
    create_item_buttons(items_general)

def execute_items_texture(event=None):
    items_texture = [
        "Quad64 v0.2", "Quad64 v0.3"
    ]
    create_item_buttons(items_texture)

def execute_items_sound(event=None):
    items_sound = [
        "N64 Sound Tool", "N64 Soundbank Tool", "N64 Midi Tool", "M64 Parser", "SM64 Mus"
    ]
    create_item_buttons(items_sound)

def execute_items_utility(event=None):
    items_utility = [
        "SM64 Save Editor"
    ]
    create_item_buttons(items_utility)

def create_item_buttons(items):
    for widget in item_frame.winfo_children():
        widget.destroy()

    for item in items:
        btn = Button(item_frame, text=item, command=lambda item=item: execute_selected_item(item), bd=0, relief=FLAT, bg='#492E87', fg='white')
        btn.pack(side=TOP, padx=5, pady=5)

# Hide the console window
if __name__ == "__main__":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Create the main window
fenetre = Tk()
fenetre.geometry('719x513')
fenetre.title('SM64 Tool Loader')
fenetre.config(bg='#492E87')
fenetre.resizable(False, False)

# Load background image
image_url = "https://i.ibb.co/Y761xfR/Background-V3.png"
img = Image.open(requests.get(image_url, stream=True).raw)
bg_image = ImageTk.PhotoImage(img)
canvas = Canvas(fenetre, width=720, height=523, bg='#492E87', highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Load Flips button image
button_image_url = "https://i.ibb.co/BTdYDNq/flipsv2.png"
button_img = Image.open(requests.get(button_image_url, stream=True).raw)
button_photo = ImageTk.PhotoImage(button_img)

# Place Flips button
btn_open_flips = Button(fenetre, image=button_photo, command=open_flips, bd=0, highlightthickness=0, relief=FLAT)
btn_open_flips.place(x=(720 - button_photo.width()) // 2, y=(523 - button_photo.height()) // 2 - 4)

# Load p64 button image
p64_button_image_url = "https://i.ibb.co/DDnJsvJ/p64.png"
p64_button_img = Image.open(requests.get(p64_button_image_url, stream=True).raw)
p64_button_photo = ImageTk.PhotoImage(p64_button_img)

# Place p64 button at the top
btn_open_p64 = Button(fenetre, image=p64_button_photo, command=open_p64, bd=0, highlightthickness=0, relief=FLAT)
btn_open_p64.place(x=(708 - p64_button_photo.width()) // 2, y=5)

# Frame for main buttons
main_button_frame = Frame(fenetre, bg='black')
main_button_frame.place(x=20, y=170)

# Main buttons
btn_general = Button(main_button_frame, text="General", command=execute_items_general, bg='black', fg='white', bd=0, relief=FLAT)
btn_general.pack(side=TOP, padx=7, pady=7)
btn_general.bind("<Enter>", lambda event, category="General": execute_items_general(event))

btn_texture = Button(main_button_frame, text="Texture", command=execute_items_texture, bg='black', fg='white', bd=0, relief=FLAT)
btn_texture.pack(side=TOP, padx=7, pady=7)
btn_texture.bind("<Enter>", lambda event, category="Texture": execute_items_texture(event))

btn_sound = Button(main_button_frame, text="Sound", command=execute_items_sound, bg='black', fg='white', bd=0, relief=FLAT)
btn_sound.pack(side=TOP, padx=7, pady=7)
btn_sound.bind("<Enter>", lambda event, category="Sound": execute_items_sound(event))

btn_utility = Button(main_button_frame, text="Utility", command=execute_items_utility, bg='black', fg='white', bd=0, relief=FLAT)
btn_utility.pack(side=TOP, padx=7, pady=7)
btn_utility.bind("<Enter>", lambda event, category="Utility": execute_items_utility(event))

# Frame for item category buttons
item_frame = Frame(fenetre, bg='#492E87')
item_frame.place(x=120, y=200)

# Frame for custom load buttons
custom_load_frame = Frame(fenetre, bg='#492E87')
custom_load_frame.place(x=10, y=460)

# Button for adding a custom load shortcut
btn_custom_load = Button(fenetre, text="Custom Load", command=add_custom_shortcut)
btn_custom_load.place(x=15, y=430)

# Create the menu
menu_bar = Menu(fenetre)
fenetre.config(menu=menu_bar)

# Dependency menu
dependency_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dependency", menu=dependency_menu)
dependency_menu.add_command(label="N64 Tool vcredist", command=open_vcredist)

# About menu
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Update", command=lambda: messagebox.showinfo("Info", "This is a tool for SM64."))
about_menu.add_command(label="Request", command=lambda: subprocess.Popen(["python", "Menu/request.py"]))
about_menu.add_command(label="SM64 Tool Loader", command=lambda: subprocess.Popen(["python", "Menu/sm64toolloader.py"]))

# Display the background image on the canvas
canvas.create_image(0, 0, image=bg_image, anchor=NW)

# Update custom load buttons initially
update_custom_load_buttons()

# Start the Tkinter main loop
fenetre.mainloop()




