""" Defines Items class

This is a child class of Position.

"""

import random

from labyrinth import *


class Syringe:
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.syringe_elements = ["N", "T", "E"] # Needle, Tube, Ether
        self.positions = self.dispatch()

        for self.syringe_element, self.position in zip(self.syringe_elements, self.positions):
            self.labyrinth.place_syringe_element(self.syringe_element, self.position)

    def dispatch(self):
        available_positions = self.labyrinth.get_available_positions()
        return random.sample(available_positions, len(self.syringe_elements))


def main():
    labyrinth = Labyrinth()
    syringe = Syringe(labyrinth)
    print(syringe.positions) # renvoie la liste des 3 positions choisies
    labyrinth.display() # affiche le labyrinthe contenant les 3 objets

if __name__ == "__main__":
    main()
