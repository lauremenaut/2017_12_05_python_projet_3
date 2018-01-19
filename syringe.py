#! /usr/bin/env python3
# coding: utf-8

""" Sets Syringe class.

Syringe class is imported in gametext.py and gamegui.py files.

"""

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
            - dispatch()
            - labyrinth.place_syringe_element()

        """
        self.labyrinth = labyrinth
        self.syringe_elements = ["N", "T", "E"]  # Needle, Tube, Ether
        self.positions = self.dispatch()
        # Assigns a position to each element
        for self.syringe_element, self.position in zip(self.syringe_elements,
                                                       self.positions):
            self.labyrinth.place_syringe_element(self.syringe_element,
                                                 self.position)

    def dispatch(self):
        """ Returns a list of tuples of random positions for the elements. """
        available_positions = self.labyrinth.get_available_positions()
        return random.sample(available_positions, len(self.syringe_elements))


def main():
    labyrinth = Labyrinth("labyrinth_test.json")
    syringe = Syringe(labyrinth)
    print("Syringe elements positions : ", syringe.positions)  # returns a list
    # of random available positions
    labyrinth.display()  # displays the labyrinth (with the syringe elements)

if __name__ == "__main__":
    main()
