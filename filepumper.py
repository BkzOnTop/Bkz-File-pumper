import tkinter as tk
from tkinter import filedialog, messagebox
import os
import ttkbootstrap as ttk

def increase_file_size(input_file, output_file, target_size_mb):
    # Calculer la taille à ajouter en octets
    current_size = os.path.getsize(input_file)
    target_size_bytes = target_size_mb * 1024 * 1024
    bytes_to_add = target_size_bytes - current_size

    if bytes_to_add > 0:
        with open(input_file, 'ab') as f:
            f.write(b'\x00' * bytes_to_add)

        messagebox.showinfo("Succès", f"Le fichier {output_file} a été créé avec succès avec une taille de {target_size_mb} Mo.")
    else:
        messagebox.showwarning("Avertissement", "Le fichier est déjà plus grand que la taille cible ou égale.")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Executable files", "*.exe")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def start_processing():
    input_file = entry_file_path.get()
    if not input_file:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un fichier .exe.")
        return

    output_file = entry_new_file_name.get()
    if not output_file:
        messagebox.showwarning("Avertissement", "Veuillez entrer un nom pour le nouveau fichier.")
        return

    try:
        target_size_mb = int(entry_target_size.get())
        if target_size_mb <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Avertissement", "Veuillez entrer un nombre valide de mégaoctets.")
        return

    increase_file_size(input_file, output_file, target_size_mb)

# Créer la fenêtre principale
root = ttk.Window(themename="darkly")  # Utiliser un thème sombre pour un look futuriste
root.title("Augmenter la taille d'un fichier .exe")
root.geometry("500x400")  # Définir une taille de fenêtre fixe

# Créer les widgets
label_instruction = ttk.Label(root, text="Sélectionnez un fichier .exe :", font=("Helvetica", 12))
label_instruction.pack(pady=10)

entry_file_path = ttk.Entry(root, width=50, font=("Helvetica", 12))
entry_file_path.pack(pady=5)

button_browse = ttk.Button(root, text="Parcourir", command=browse_file, style="primary.TButton")
button_browse.pack(pady=5)

label_target_size = ttk.Label(root, text="Taille cible en Mo :", font=("Helvetica", 12))
label_target_size.pack(pady=10)

entry_target_size = ttk.Entry(root, width=20, font=("Helvetica", 12))
entry_target_size.pack(pady=5)

label_new_file_name = ttk.Label(root, text="Nouveau nom du fichier (avec extension .exe) :", font=("Helvetica", 12))
label_new_file_name.pack(pady=10)

entry_new_file_name = ttk.Entry(root, width=50, font=("Helvetica", 12))
entry_new_file_name.pack(pady=5)

button_start = ttk.Button(root, text="Augmenter la taille", command=start_processing, style="success.TButton")
button_start.pack(pady=20)

# Lancer la boucle principale
root.mainloop()