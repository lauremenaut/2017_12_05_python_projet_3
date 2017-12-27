""" Defines MacGyver class

This is a child class of Position.

"""

from position import *
from labyrinth import *


class MacGyver(Position):

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.position = self.labyrinth.get_position()
        super().__init__(self.position)
        self.picked_items = 0

    def move(self, direction):
        if direction == "u":
            next_position = self.up()
            print("Up !")
        elif direction == "d":
            next_position = self.down()
            print("Down !")
        elif direction == "l":
            next_position = self.left()
            print("Left !")
        elif direction == "r":
            next_position = self.right()
            print("Right !")

        if self.labyrinth.is_available(next_position):
            self.position = next_position
            print("Available !")
        elif self.labyrinth.is_an_item(next_position):
            self.position = next_position
            self.pick_up_item()
            print("Item !")
        elif self.labyrinth.is_the_guard(next_position):
            self.position = next_position
            self.fight_guard()
            print("Guard !!!")
        else:
            print("MacGyver can't move in this direction !")
        return self.position

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
    for i in range(12):
        macgyver.move("r")
    print("New position : {}".format(macgyver.position))

# si on envoie MacGyver dans le mur :
    labyrinth = Labyrinth()
    macgyver = MacGyver(labyrinth)
    print("Starting position : {}".format(macgyver.position)) # renvoie (1, 0)
    macgyver.move("r")
    print("New position : {}".format(macgyver.position)) # ça ne marche pas !!
    macgyver.move("l")
    print("New position : {}".format(macgyver.position)) # 
    macgyver.move("r")
    print("New position : {}".format(macgyver.position)) # 

if __name__ == "__main__":
    main()
