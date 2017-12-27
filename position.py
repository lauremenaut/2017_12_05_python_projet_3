""" Defines Position class

This is an abstract class, and a mother class for macgyver, guard and item
classes, as their instantiated objects have a "position" on the labyrinth.

"""


class Position:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def up(self):
        self.x -= 1
        return self.x, self.y

    def down(self):
        self.x += 1
        return self.x, self.y

    def right(self):
        self.y += 1
        return self.x, self.y

    def left(self):
        self.y -= 1
        return self.x, self.y


def main():
    position = Position((5, 2))
    print(position.up()) # renvoie (4, 2)
    print(position.down()) # renvoie (5, 2)
    print(position.left()) # renvoie (5, 1)
    print(position.right()) # renvoie (5, 2)

if __name__ == "__main__":
    main()
