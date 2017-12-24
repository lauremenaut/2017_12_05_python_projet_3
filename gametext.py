#! /usr/bin/env python3
# coding: utf-8

""" Defines GameText class

This class manages the "textual version" of the game "Help MacGyver to escape
from the labyrinth !"
McGyver needs to find and pick up 3 items (a needle, a small plastic tube and
ether) in the labyrinth before neutralizing the guard and being able to escape.

"""

from labyrinth import *
from macgyver import *
from guard import *
from item import *
from position import *


class GameText:
    def __init__(self):
        labyrinth = Labyrinth(file(?))
        macgyver = MacGyver(position, labyrinth(?))
        guard = Guard(position)
        needle = Item(position)
        tube = Item(position)
        ether = Item(position)

    def start(self):
        pass # boucle qui affiche le laby, pose question à l'utilisateur ...
        # boucle jusqu'à la fin du jeu (while True / break ou variable "continuer" True > False)

    """    
        if "q"
            if h b d g: # saisie sécurisée pour reposer la question si invalide
                self.mcgyver(move, reponse) # doit savoir si dispo, objets = besoin de Labyrinth
# après déplacement, maj position McG
    """


def main():
    pass

if __name__ == "__main__":
    main()
