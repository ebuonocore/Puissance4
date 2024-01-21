""" Jeu puissance 4
    Auteur: Eric Buonocore
    Date: 2020-05-20
    Objectifs: 
        Affichage du plateau de jeu
        Interaction avec le joueur
            Sélection de la colonne si coup valide
            Gestion des tours
            Gestion des victoires, matchs nuls
        Système de jeu
            Gestion des sauvegardes
            Gestion des chargements
            Gestion des options
            Gestion des scores
            Gestion des menus      
        IA
            Enregistrement d'une partie = Str ("Victoire", "Défaite", "Match_nul"), succession de coups joués
            Dictionnaire des stratégies (predicts) 

"""
from IU import *

""" Initialisation
        Plateau de jeu
        Initialisation (récupération) du dictionnaire des stratégies (predicts)
        Etat de partie en cours à True
        joueur actif à 0
        succesions des coups (liste coups)
"""
fenêtre = IU_menu()
""" Moteur du jeu
        Choix du type de jeu : 2 humains, humain contre IA, IA contre IA
        Tant que le plateau n'est pas plein et qu'il n'y a pas de victoire
            Affichage du plateau
            Demande de saisie de la colonne (valide)
            place le pion
            Teste la condition de fin de partie (plateau plein ou victoire)
            joueur actif suivant
        Enregistrement de la partie dans le dictionnaire des stratégies (predicts)
"""
fenêtre.tk.mainloop()
