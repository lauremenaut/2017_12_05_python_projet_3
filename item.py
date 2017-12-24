""" Defines Item class

This is a child class of Positionable.

"""

from positionable import *


class Item(Positionable):
    def __init__(self, position):
        super().__init__(position)


def main():
    pass

if __name__ == "__main__":
    main()
