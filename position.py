#! /usr/bin/env python3
# coding: utf-8

""" Sets Position class.

Position class is imported in macgyver.py file.

"""


class Position:
    """ Sets Position class.

    The Position class consists of 5 methods :
        - __init__()
        - up()
        - down()
        - left()
        - right()

    """
    def __init__(self, position):
        """ Position constructor. """
        self.x = position[0]
        self.y = position[1]

    def up(self):
        """ Returns a new Position object, one step up. """
        return Position((self.x, self.y - 1))

    def down(self):
        """ Returns a new Position object, one step down. """
        return Position((self.x, self.y + 1))

    def left(self):
        """ Returns a new Position object, one step left. """
        return Position((self.x - 1, self.y))

    def right(self):
        """ Returns a new Position object, one step right. """
        return Position((self.x + 1, self.y))


def main():
    position = Position((5, 2))
    print("up(5, 2) : ", position.up().x, position.up().y)  # returns 5 1
    print("down(5, 2) : ", position.down().x, position.down().y)  # returns 5 3
    print("left(5, 2) : ", position.left().x, position.left().y)  # returns 4 2
    print("right(5, 2) : ", position.right().x, position.right().y)  # returns
    # 6 2

if __name__ == "__main__":
    main()
