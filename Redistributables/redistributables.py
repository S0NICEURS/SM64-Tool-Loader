import tkinter as tk
import os

class InstallRedistributablesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Install Redistributables")
        self.root.geometry("320x174")  # Définition de la taille de la fenêtre

        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        btn_x64_vs2013 = tk.Button(frame, text="x64 VS2013", command=lambda: os.system("vcredist_x64_vs2013.exe"))
        btn_x64_vs2013.pack(pady=5)

        btn_x86_vs2013 = tk.Button(frame, text="x86 VS2013", command=lambda: os.system("vcredist_x86_vs2013.exe"))
        btn_x86_vs2013.pack(pady=5)

        btn_x86_vs2008 = tk.Button(frame, text="x86 VS2008", command=lambda: os.system("vcredist_x86_vs2008.exe"))
        btn_x86_vs2008.pack(pady=5)

    def run_installer(self, filename):
        if os.path.exists(filename):
            os.system(filename)
        else:
            print(f"Le fichier {filename} n'a pas été trouvé dans le dossier actuel.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallRedistributablesApp(root)
    root.mainloop()
