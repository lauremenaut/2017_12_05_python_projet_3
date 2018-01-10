#! /usr/bin/env python3
# coding: utf-8

""" Sets Labyrinth class.

Labyrinth class is imported in macgyver.py, syringe.py, gametext.py and
gamegui.py files.

"""

import json


class Labyrinth:
    """ Sets Labyrinth class.

    The Labyrinth class consists of 9 methods :
        - __init__()
        - display()
        - get_position()
        - get_walls_positions()
        - get_available_positions()
        - place_syringe_element()
        - is_a_syringe_element()
        - is_near_the_guard()
        - is_available()

    """
    def __init__(self, labyrinth_file="labyrinth.json"):
        """ Labyrinth constructor.

        Load a .json file that contains a list of lists of characters.
        Default file is "labyrinth.json".

        """
        with open(labyrinth_file, 'r') as f:
            self.lines_list = json.load(f)

    def display(self):
        """ Display the labyrinth. """
        print()
        for line in self.lines_list:
            for char in line:
                if char != "\n":
                    print(char, end=' ')
                else:
                    print('')
        print()

    def get_position(self, letter):
        """ Returns a position as a tuple (x, y). """
        y = 0
        for line in self.lines_list:
            x = 0
            for char in line:
                if char == letter:
                    self.position = x, y
                x += 1
            y += 1
        return self.position

    def get_walls_positions(self):
        """ Returns a list of tuples of walls positions. """
        walls_positions = []
        y = 0
        for line in self.lines_list:
            x = 0
            for char in line:
                if char == "W":
                    walls_positions.append((x, y))
                x += 1
            y += 1
        return walls_positions

    def get_available_positions(self):
        """ Returns a list of tuples of available positions. """
        available_positions = []
        y = 0
        for line in self.lines_list:
            x = 0
            for char in line:
                if char == " ":
                    available_positions.append((x, y))
                x += 1
            y += 1
        return available_positions

    def place_syringe_element(self, syringe_element, position):
        """ Replaces N spaces of the labyrinth with N syringe elements. """
        y = 0
        for line in self.lines_list:
            x = 0
            for char in line:
                if (x, y) == position:
                    self.lines_list[y][x] = syringe_element
                x += 1
            y += 1

    def is_a_syringe_element(self, position):
        """ Returns syringe element settled on this position. """
        if self.lines_list[position.y][position.x] in ["N", "T", "E"]:
            return self.lines_list[position.y][position.x]

    def is_near_the_guard(self, position):
        """ Returns True if the guard is at one step from this position. """
        return self.lines_list[position.y][position.x] == "e"

    def is_available(self, position):
        """ Returns True if this position is available (== " "). """
        available_positions = self.get_available_positions()
        return position in available_positions


def main():
    labyrinth = Labyrinth("labyrinth_test.json")
    labyrinth.display() # displays the labyrinth (without syringe elements)
    print("Starting position : ", labyrinth.get_position("M")) # returns
    # (0, 1)
    print("Available positions : ", labyrinth.get_available_positions())
    # displays a list of available positions
    print("Walls positions : ", labyrinth.get_walls_positions()) # displays
    # a list of walls positions

if __name__ == "__main__":
    main()
