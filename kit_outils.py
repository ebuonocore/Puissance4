from PIL import Image, ImageTk


def dimensions_écran(fenêtre):
    """Renvoie les dimensions de la fenêtre en pixels"""
    fenêtre.update()
    LARGEUR = fenêtre.winfo_screenwidth()
    HAUTEUR = fenêtre.winfo_screenheight()
    return LARGEUR, HAUTEUR


def import_image(self, nom):
    """Import l'image désignée par nom"""
    file = "images/" + nom + ".png"
    image_source = Image.open(file)
    image = ImageTk.PhotoImage(image_source)
    return image
