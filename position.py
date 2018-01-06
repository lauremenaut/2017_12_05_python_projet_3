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
    print(position.up().x, position.up().y) # renvoie 5, 1
    print(position.down().x, position.down().y) # renvoie 5, 3
    print(position.left().x, position.left().y) # renvoie 4, 2
    print(position.right().x, position.right().y) # renvoie 6, 2


if __name__ == "__main__":
    main()
