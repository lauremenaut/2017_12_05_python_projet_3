""" Sets Position class.

This is an abstract class and a mother class for MacGyver class.

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
        """ Returns a new position, one step up. """
        self.y -= 1
        return self.x, self.y

    def down(self):
        """ Returns a new position, one step down. """
        self.y += 1
        return self.x, self.y

    def left(self):
        """ Returns a new position, one step left. """
        self.x -= 1
        return self.x, self.y

    def right(self):
        """ Returns a new position, one step right. """
        self.x += 1
        return self.x, self.y


def main():
    position = Position((5, 2))
    print(position.up()) # renvoie (4, 2)
    print(position.down()) # renvoie (5, 2)
    print(position.left()) # renvoie (5, 1)
    print(position.right()) # renvoie (5, 2)

if __name__ == "__main__":
    main()
