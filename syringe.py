""" Sets Syringe class. """

import random

from labyrinth import Labyrinth


class Syringe:
    """ Sets Syringe class.

    The Syringe class consists of 2 methods :
        - __init__()
        - dispatch()

    """
    def __init__(self, labyrinth):
        """ Syringe constructor.

        Sets a Labyrinth object as an attribute.
        Sets a list of syringe elements.
        Calls :
            - display()
            - labyrinth.place_syringe_element()

        """
        self.labyrinth = labyrinth
        self.syringe_elements = ["N", "T", "E"] # Needle, Tube, Ether
        self.positions = self.dispatch()

        for self.syringe_element, self.position in zip(self.syringe_elements, self.positions):
            self.labyrinth.place_syringe_element(self.syringe_element, self.position)

    def dispatch(self):
        """ Returns a list of random positions for syringe elements. """
        available_positions = self.labyrinth.get_available_positions()
        return random.sample(available_positions, len(self.syringe_elements))


def main():
    labyrinth = Labyrinth()
    syringe = Syringe(labyrinth)
    print(syringe.positions) # renvoie la liste des 3 positions choisies
    labyrinth.display() # affiche le labyrinthe contenant les 3 objets

if __name__ == "__main__":
    main()
