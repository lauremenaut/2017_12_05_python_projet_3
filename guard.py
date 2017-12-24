""" Defines Guard class

This is a child class of Positionable.

"""

from positionable import *


class Guard(Positionable):
    def __init__(self, position):
        super().__init__(position)

    def block_exit(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()
