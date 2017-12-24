""" Defines MacGyver class

This is a child class of Positionable.

"""

from positionable import *


class MacGyver(Positionable):

    def __init__(self, position, laby):
        super().__init__(position)
        self.picked_items = 0
        self.laby = laby

    def move(self, direction, labyrinth):
        pass
        is_free(next_position)

    def pick_up_item(self):
        self.picked_objects += 1

    def neutralize_guard(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()
