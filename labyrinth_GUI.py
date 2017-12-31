""" Sets Labyrinth class. """

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
            for character in line:
                print(character, end='')
        print()

    def get_position(self, char):
        """ Returns a position as a tuple (x, y). """
        x = 0
        for line in self.lines_list:
            y = 0
            for character in line:
                if character == char:
                    self.position = x, y
                y += 1
            x += 1
        return self.position

    def get_walls_positions(self):
        """ Returns a list of walls positions. """
        walls_positions = []
        x = 0
        for line in self.lines_list:
            y = 0
            for character in line:
                if character == "W":
                    walls_positions.append((x, y))
                y += 1
            x += 1
        return walls_positions

    def get_available_positions(self):
        """ Returns a list of available positions. """
        available_positions = []
        x = 0
        for line in self.lines_list:
            y = 0
            for character in line:
                if character == " ":
                    available_positions.append((x, y))
                y += 1
            x += 1
        return available_positions

    def place_syringe_element(self, syringe_element, position):
        """ Replaces N spaces of the labyrinth with N syringe elements. """
        x = 0
        for line in self.lines_list:
            y = 0
            for character in line:
                if (x, y) == position:
                    self.lines_list[x][y] = syringe_element
                y += 1
            x += 1

    def is_a_syringe_element(self, position):
        """ Returns whether a syringe element is on this position. """
        return self.lines_list[position[0]][position[1]] in ["N", "T", "E"]

    def is_near_the_guard(self, position):
        """ Returns whether the guard is at one step from this position. """
        return self.lines_list[(position[0] + 1)][position[1]] == "G" or \
            self.lines_list[(position[0] - 1)][position[1]] == "G" or \
            self.lines_list[position[0]][(position[1] + 1)] == "G" or \
            self.lines_list[position[0]][(position[1] - 1)] == "G"

    def is_available(self, position):
        """ Returns whether this position is available (= " "). """
        available_positions = self.get_available_positions()
        return position in available_positions


def main():
    labyrinth = Labyrinth("labyrinth_test_GUI.json")
    labyrinth.display() # affiche le labyrinthe (sans les objets)
    print(labyrinth.get_position("M")) # renvoie (1, 0)
    print(labyrinth.get_available_positions()) # affiche la liste des positions libres
    print(labyrinth.get_walls_positions()) # affiche la liste des positions des murs
    print(labyrinth.is_a_syringe_element((1, 8))) # renvoie False
    print(labyrinth.is_near_the_guard((1, 8))) # renvoie False
    print(labyrinth.is_near_the_guard((3, 13))) # renvoie True
    print(labyrinth.is_available((1, 8))) # renvoie False
    print(labyrinth.is_available((1, 2))) # renvoie True

if __name__ == "__main__":
    main()
