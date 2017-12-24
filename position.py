""" Defines Position class """


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1


def main():
    pass

if __name__ == "__main__":
    main()
