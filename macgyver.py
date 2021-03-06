#! /usr/bin/env python3
# coding: utf-8

""" Sets MacGyver class.

MacGyver class is imported in gametext.py and gamegui.py files.

"""

from position import Position
from labyrinth import Labyrinth


class MacGyver:
    """ Sets MacGyver class.

    The MacGyver class consists of 5 methods :
        - __init__()
        - move()
        - step()
        - pick_up_syringe_element()
        - fight_guard()

    """
    def __init__(self, labyrinth):
        """ MacGyver constructor.

        Sets a Labyrinth object as an attribute.
        Sets a starting position, calling labyrinth.get_macgyver_position().
        Sets an empty list of collected syringe elements.

        """
        self.labyrinth = labyrinth
        self.position = Position(self.labyrinth.get_position("M"))
        self.collected_syringe_elements = []

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
        Returns "success" in case of guard fighting.

        """
        # 'direction' is given by user keyboard
        # 'next_position' is the hypothetical next position if available
        if direction == "u":
            next_position = self.position.up()
        elif direction == "d":
            next_position = self.position.down()
        elif direction == "l":
            next_position = self.position.left()
        elif direction == "r":
            next_position = self.position.right()

        # Checks if there is an element to pick up on the next position
        if self.labyrinth.is_a_syringe_element(next_position):
            element = self.labyrinth.is_a_syringe_element(next_position)
            self.pick_up_syringe_element(element)
            self.step(next_position)

        # Checks if the guard is on the next position
        elif self.labyrinth.is_near_the_guard(next_position):
            self.step(next_position)
            success = self.fight_guard()
            return success

        # Checks if the next position is available (== space)
        elif self.labyrinth.is_available((next_position.x, next_position.y)):
            self.step(next_position)

        else:
            print("\nMacGyver can't move in this direction !")

    def step(self, next_position):
        """ Moves the "M" character on the next position. """
        self.labyrinth.lines_list[next_position.y][next_position.x] = "M"
        self.labyrinth.lines_list[self.position.y][self.position.x] = " "
        self.position = next_position

    def pick_up_syringe_element(self, element):
        """ Add the collected element to the list. """
        self.collected_syringe_elements.append(element)
        print("\nMacGyver picked up {} syringe element(s), find {} more !".
              format(len(self.collected_syringe_elements),
                     3 - len(self.collected_syringe_elements)))

    def fight_guard(self):
        """ End of game : success or failure. """
        if len(self.collected_syringe_elements) == 3:
            print("\nMacGyver managed to escape ... Congratulations !")
            return True
        else:
            print("\nMacGyver failed to put the guard to sleep ... He's dead\
                  !")
            return False


def main():

    labyrinth = Labyrinth("labyrinth_test.json")
    macgyver = MacGyver(labyrinth)
    print("Collected_syringe_elements : {}".
          format(macgyver.collected_syringe_elements))  # returns []
    print("Starting position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns (0, 1)
    macgyver.move("r")
    print("New position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns (1, 1)
    macgyver.move("r")
    print("New position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns (2, 1)
    macgyver.move("r")
    print("New position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns "Can't
          # move ..." then (2, 1)
    macgyver.move("d")
    print("New position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns (2, 2)
    macgyver.move("d")
    print("New position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns (2, 3)
    for i in range(11):
        macgyver.move("r")  # returns "MacGyver failed ..."
    print("New position : {}".
          format((macgyver.position.x, macgyver.position.y)))  # returns (13, 3)

if __name__ == "__main__":
    main()
