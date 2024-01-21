import tkinter as tki
from PIL import Image, ImageTk
from os import path
from tkinter import filedialog as fd
from tkinter import ttk
import kit_outils as kit


class IU_menu:
    def __init__(self) -> None:
        self.tk = tki.Tk()
        self.tk.title("Puissance_4 : Menu prinicpal")
        self.largeur_écran, self.hauteur_écran = kit.dimensions_écran(self.tk)
        self.hauteur_menu = 80
        self.menu = tki.Canvas(
            self.tk, width=self.largeur_écran, height=self.hauteur_menu, bg="#F0F0F0"
        )
        ensemble_boutons = [
            ("Fichiers", self.cmd_fichiers),
            ("Paramètres", self.cmd_paramètres),
            ("Lancer-Arrêter", self.cmd_lancer),
            ("Quitter", self.cmd_quitter),
        ]
        for nom_bouton, commande in ensemble_boutons:
            bouton = tki.Button(self.menu, text=nom_bouton, command=commande)
            bouton.pack(side=tki.LEFT)
        self.blanc = tki.Label(self.menu, width=self.largeur_écran, bg="#F0F0F0")
        self.blanc.pack(side=tki.LEFT)
        self.can = tki.Canvas(
            self.tk,
            width=self.largeur_écran,
            height=self.hauteur_écran - self.hauteur_menu,
            bg="black",
        )
        self.can_objets = []
        self.menu.pack()
        self.can.pack()
        self.choix_joueur = [
            "Humain",
            "IA Shadow",
            "IA Speedy",
            "IA Bashful",
            "IA Pokey",
        ]
        self.box_choix1 = ttk.Combobox(self.can, values=self.choix_joueur)
        self.box_choix2 = ttk.Combobox(self.can, values=self.choix_joueur)
        self.paramètres = dict()
        self.paramètres["joueur1"] = self.choix_joueur[0]
        self.paramètres["joueur2"] = self.choix_joueur[0]
        self.cmd_paramètres()

    def effacer_fenêtre_principale(self):
        # Efface tous les éléments du canvas
        for i in range(len(self.can_objets)):
            objet = self.can_objets.pop()
            objet.destroy()

    def cmd_fichiers(self):
        self.effacer_fenêtre_principale()
        label_fichier = tki.Label(self.can, text="Choix d'une sauvegarde")
        xf = self.largeur_écran // 2
        label_fichier.place(x=xf - 200, y=20)
        self.can_objets.append(label_fichier)

    def cmd_paramètres(self):
        self.effacer_fenêtre_principale()
        xf = self.largeur_écran // 2
        yf = (self.hauteur_écran - self.hauteur_menu) // 2
        #
        label_joueur1 = tki.Label(self.can, text="Joueur 1", width=200)
        label_joueur1.place(x=xf - 200, y=yf - 20, width=200, height=30)
        label_joueur2 = tki.Label(self.can, text="Joueur 2", width=200)
        label_joueur2.place(x=xf, y=yf - 20, width=200, height=30)
        #
        self.box_choix1 = ttk.Combobox(self.can, values=self.choix_joueur)
        self.box_choix1.bind("<<ComboboxSelected>>", self.combobox_modifiée)
        self.box_choix1.current(0)
        self.box_choix1.place(x=xf - 200, y=yf + 10, width=200)
        self.box_choix2 = ttk.Combobox(self.can, values=self.choix_joueur)
        self.box_choix2.bind("<<ComboboxSelected>>", self.combobox_modifiée)
        self.box_choix2.current(0)
        self.box_choix2.place(x=xf, y=yf + 10, width=200)
        self.can_objets.append(label_joueur1)
        self.can_objets.append(label_joueur2)
        self.can_objets.append(self.box_choix1)
        self.can_objets.append(self.box_choix2)

    def cmd_lancer(self):
        self.effacer_fenêtre_principale()
        text_joueurs = (
            "C'est parti :"
            + self.paramètres["joueur1"]
            + " vs "
            + self.paramètres["joueur2"]
        )
        label_GO = tki.Label(self.can, text=text_joueurs)
        xf = self.largeur_écran // 2
        label_GO.place(x=xf - 200, y=20)
        self.can_objets.append(label_GO)

    def cmd_quitter(self):
        self.tk.quit()
        self.tk.destroy()

    def combobox_modifiée(self, event):
        self.paramètres["joueur1"] = self.box_choix1.get()
        self.paramètres["joueur2"] = self.box_choix2.get()
