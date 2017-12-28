""" Defines MacGyver class, as a child class of Position class."""

from position import Position
from labyrinth import Labyrinth


class MacGyver(Position):

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.position = self.labyrinth.get_macgyver_position()
        super().__init__(self.position)
        self.picked_up_syringe_elements = 0

    def move(self, direction):
        if direction == "u":
            next_position = self.up()
        elif direction == "d":
            next_position = self.down()
        elif direction == "l":
            next_position = self.left()
        elif direction == "r":
            next_position = self.right()

        if self.labyrinth.is_a_syringe_element(next_position):
            self.pick_up_syringe_element()
            if self.labyrinth.near_the_guard(next_position):
            # in case a syringe element is right next to the guard : pick_up + fight
                self.fight_guard()
                return False
            self.step(next_position)
        elif self.labyrinth.near_the_guard(next_position):
            self.step(next_position)
            self.fight_guard()
            return False
        elif self.labyrinth.is_available(next_position):
            self.step(next_position)

        else:
            print("\nMacGyver can't move in this direction !")
            # next_position needs to be brought one step back
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

    def pick_up_syringe_element(self):
        self.picked_up_syringe_elements += 1
        print("\nMacGyver picked up {} syringe element(s), find {} more !".format(self.picked_up_syringe_elements, 3 - self.picked_up_syringe_elements))

    def fight_guard(self):
        if self.picked_up_syringe_elements == 3:
            print("\nMacGyver managed to escape ... Congratulations !")
        else:
            print("\nMacGyver failed to put the guard to sleep ... He's dead !")


def main():
    labyrinth = Labyrinth()
    macgyver = MacGyver(labyrinth)
    print("Picked_up_syringe_elements : {}".format(macgyver.picked_up_syringe_elements)) # renvoie 0
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
