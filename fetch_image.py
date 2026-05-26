import tkinter as tk
from tkinter import filedialog
import os

# Dossier d'ouverture par défaut : celui contenant ce script
INITIAL_DIR = os.path.dirname(os.path.abspath(__file__))

# Filtres de types d'images acceptés dans la boîte de dialogue
IMAGE_TYPES = [
    ("Images", "*.png *.jpg *.jpeg *.bmp *.tif *.tiff"),
    ("PNG", "*.png"),
    ("JPEG", "*.jpg *.jpeg"),
    ("Tous les fichiers", "*.*"),
]

def fetch_image() -> str | None:
    """Ouvre une boîte de dialogue pour sélectionner un fichier image.

    Retourne le chemin absolu du fichier sélectionné, ou None si annulé.
    """
    # Crée une fenêtre Tk masquée (nécessaire pour afficher la boîte de dialogue)
    root = tk.Tk()
    root.withdraw()

    # Ouvre la boîte de dialogue de sélection de fichier
    path = filedialog.askopenfilename(
        title="Sélectionner une image",
        initialdir=INITIAL_DIR,
        filetypes=IMAGE_TYPES,
    )

    root.destroy()
    return path if path else None


if __name__ == "__main__":
    image_path = fetch_image()
    if image_path:
        print(f"Image sélectionnée : {image_path}")
    else:
        print("Aucune image sélectionnée.")
