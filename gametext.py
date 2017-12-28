#! /usr/bin/env python3
# coding: utf-8

""" Sets GameText class

This class manages the "textual version" of the game "Help MacGyver to
escape from the labyrinth !"
McGyver needs to find and pick up 3 items (a needle, a small plastic
tube and ether) in the labyrinth to make a syringe. Then, he will be
able to neutralize the guard and escape.

"""

from labyrinth import Labyrinth
from macgyver import MacGyver
from syringe import Syringe


class GameText:
    """ Sets GameText class.

    The GameText class consists of 2 methods :
        - __init__()
        - run()
    It needs Labyrinth, MacGyver and Syringe imported classes.

    """
    def __init__(self):
        """ GameText constructor.

        Instantiate objects from Labyrinth, MacGyver and Syringe classes.

        """
        self.labyrinth = Labyrinth()
        self.macgyver = MacGyver(self.labyrinth)
        self.syringe = Syringe(self.labyrinth)

    def run(self):
        """ Manages the game progress.

        Sets :
            "carry_on" boolean variable
            user interaction
            labyrinth display

        """
        carry_on = True
        print("\nHelp MacGyver to escape from the labyrinth : he needs to pick\
 up a needle, a tube and ether before fighting the guard !")
        while carry_on is not False:
            self.labyrinth.display()
            user_answer = input("In which direction do you want MacGyver to \
move ? Please enter 'u' for up, 'd' for down, 'l' for left and 'r' for \
right, or 'q' to quit : ")
            if user_answer not in ["q", "u", "d", "l", "r"]:
                print("\nInvalid choice !")
                continue
            elif user_answer == "q":
                carry_on = False
            else:
                carry_on = self.macgyver.move(user_answer)
                if carry_on == False:
                    self.labyrinth.display()


def main():
    game = GameText()
    game.run()

if __name__ == "__main__":
    main()
