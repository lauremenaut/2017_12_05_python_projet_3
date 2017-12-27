""" Defines MacGyver class

This is a child class of Position.

"""

from position import *
from labyrinth import *


class MacGyver(Position):

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.position = self.labyrinth.get_macgyver_position()
        super().__init__(self.position)
        self.picked_items = 0

    def move(self, direction):
        if direction == "u":
            next_position = self.up()
        elif direction == "d":
            next_position = self.down()
        elif direction == "l":
            next_position = self.left()
        elif direction == "r":
            next_position = self.right()

        if self.labyrinth.near_the_guard(next_position):
            self.step(next_position)
            self.fight_guard()
        elif self.labyrinth.is_available(next_position):
            self.step(next_position)
        elif self.labyrinth.is_an_item(next_position):
            self.step(next_position)
            self.pick_up_item()
        else: # il faut ramener next_position d'une position en arrière
            print("MacGyver can't move in this direction !")
            if direction == "u":
                next_position = self.down()
            elif direction == "d":
                next_position = self.up()
            elif direction == "l":
                next_position = self.right()
            elif direction == "r":
                next_position = self.left()

    def step(self, next_position):
        self.labyrinth.lines_list[next_position[0]][next_position[1]] = "M"
        self.labyrinth.lines_list[self.position[0]][self.position[1]] = " "
        self.position = next_position

    def pick_up_item(self):
        self.picked_items += 1

    def fight_guard(self):
        if self.picked_items == 3:
            print("Congratulations !")
        else:
            print("Game over !")


def main():
    labyrinth = Labyrinth()
    macgyver = MacGyver(labyrinth)
    print("Picked_items : {}".format(macgyver.picked_items)) # renvoie 0
# si on prend le "bon" chemin :
    print("Starting position : {}".format(macgyver.position)) # renvoie (1, 0)
    macgyver.move("r")
    print("New position : {}".format(macgyver.position)) # renvoie (1, 1)
    macgyver.move("r")
    print("New position : {}".format(macgyver.position)) # renvoie (1, 2)
    macgyver.move("d")
    print("New position : {}".format(macgyver.position)) # renvoie (2, 2)
    macgyver.move("d")
    print("New position : {}".format(macgyver.position)) # renvoie (3, 2)
    for i in range(11):
        macgyver.move("r")
    print("New position : {}".format(macgyver.position))

# si on envoie MacGyver dans le mur :
    labyrinth = Labyrinth()
    macgyver = MacGyver(labyrinth)
    print("Starting position : {}".format(macgyver.position)) # renvoie (1, 0)
    macgyver.move("r")
    print("New position : {}".format(macgyver.position)) # renvoie (1, 1)
    macgyver.move("u")
    print("New position : {}".format(macgyver.position)) # renvoie "Can't move" (1, 1) 
    macgyver.move("r")
    print("New position : {}".format(macgyver.position)) # renvoie (1, 2) 

if __name__ == "__main__":
    main()
