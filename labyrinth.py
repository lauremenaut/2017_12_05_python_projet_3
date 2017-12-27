""" Defines Labyrinth class

...

"""

import json


class Labyrinth:
    def __init__(self, labyrinth_file="labyrinth.json"):
        with open(labyrinth_file, 'r') as f:
            self.lines_list = json.load(f)

    def display(self):
        print()
        for line in self.lines_list:
            for character in line:
                print(character, end='')
        print()

    def get_macgyver_position(self):
        x = 0
        for line in self.lines_list:
            y = 0
            for character in line:
                if character == "M":
                    self.position = x, y
                y += 1
            x += 1
        return self.position

    def get_available_positions(self):
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
        x = 0
        for line in self.lines_list:
            y = 0
            for character in line:
                if (x, y) == position:
                    self.lines_list[x][y] = syringe_element
                y += 1
            x += 1

    def is_a_wall(self, position):
        return self.lines_list[position[0]][position[1]] == "X"

    def is_an_item(self, position):
        return self.lines_list[position[0]][position[1]] in ["N", "T", "E"]

    def near_the_guard(self, position):
        return self.lines_list[(position[0] + 1)][position[1]] == "G" or \
            self.lines_list[(position[0] - 1)][position[1]] == "G" or \
            self.lines_list[position[0]][(position[1] + 1)] == "G" or \
            self.lines_list[position[0]][(position[1] - 1)] == "G"

    def is_available(self, position):
        available_positions = self.get_available_positions()
        return position in available_positions


def main():
    labyrinth = Labyrinth()
    labyrinth.display() # affiche le labyrinthe (sans les objets)
    print(labyrinth.get_macgyver_position()) # renvoie (1, 0)
    print(labyrinth.get_available_positions()) # affiche la liste des positions libres
    print(labyrinth.is_a_wall((1, 8))) # renvoie True
    print(labyrinth.is_an_item((1, 8))) # renvoie False
    print(labyrinth.near_the_guard((1, 8))) # renvoie False
    print(labyrinth.near_the_guard((3, 13))) # renvoie True
    print(labyrinth.is_available((1, 8))) # renvoie False


if __name__ == "__main__":
    main()
