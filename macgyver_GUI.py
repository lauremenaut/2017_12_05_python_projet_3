""" Sets MacGyver class, as a child class of Position class."""

from position import Position
from labyrinth_GUI import Labyrinth


class MacGyver(Position):
    """ Sets MacGyver class.

    The MacGyver class consists of 5 methods :
        - __init__()
        - move()
        - step()
        - pick_up_syringe_element()
        - fight_guard()
    It uses methods of Position and Labyrinth imported classes.

    """
    def __init__(self, labyrinth):
        """ MacGyver constructor.

        Sets a Labyrinth object as an attribute.
        Sets a starting position, calling labyrinth.get_macgyver_position().
        Calls Position constructor on position attribute.
        Initializes a counter for collected syringe elements.

        """
        self.labyrinth = labyrinth
        self.position = self.labyrinth.get_position("M")
        super().__init__(self.position)
        self.collected_syringe_elements = 0

    def move(self, direction):
        """ Manages MacGyver movements.

        Sets MacGyver next position, according to the direction given by user.
        Calls :
            step()
            pick_up_syringe_element()
            fight_guard()
            position.up()
            position.down()
            position.left()
            position.right()
            labyrinth.is_a_syringe_element()
            labyrinth.is_near_the_guard()
            labyrinth.is_available()
        Returns False in case of guard fighting.

        """
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
            if self.labyrinth.is_near_the_guard(next_position):
            # in case a syringe element is right next to the guard : pick_up + fight
                self.step(next_position)
                self.fight_guard()
                return False
            self.step(next_position)
        elif self.labyrinth.is_near_the_guard(next_position):
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
        """ Moves the "M" character on the next position. """
        self.labyrinth.lines_list[next_position[0]][next_position[1]] = "M"
        self.labyrinth.lines_list[self.position[0]][self.position[1]] = " "
        self.position = next_position

    def pick_up_syringe_element(self):
        """ Increments the counter of the collected syringe elements. """
        self.collected_syringe_elements += 1
        print("\nMacGyver picked up {} syringe element(s), find {} more !".format(self.collected_syringe_elements, 3 - self.collected_syringe_elements))

    def fight_guard(self):
        """ End of game : success or failure. """
        if self.collected_syringe_elements == 3:
            print("\nMacGyver managed to escape ... Congratulations !")
        else:
            print("\nMacGyver failed to put the guard to sleep ... He's dead !")


def main():
    labyrinth = Labyrinth("labyrinth_test_GUI.json")
    macgyver = MacGyver(labyrinth)
    print("Collected_syringe_elements : {}".format(macgyver.collected_syringe_elements)) # renvoie 0
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
        macgyver.move("r") # renvoie Failure
    print("New position : {}".format(macgyver.position)) # renvoie (3, 13)

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
