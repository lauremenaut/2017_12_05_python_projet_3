#! /usr/bin/env python3
# coding: utf-8

""" Sets GameText class.

This class manages the "textual version" of the game "Help MacGyver to
escape from the labyrinth !"

"""

import argparse

from labyrinth import Labyrinth
from macgyver import MacGyver
from syringe import Syringe


class GameText:
    """ Sets GameText class.

    The GameText class consists of 2 methods :
        - __init__()
        - run()

    """
    def __init__(self, json_file="labyrinth.json"):
        """ GameText constructor.

        Instantiates objects from Labyrinth, MacGyver and Syringe classes.

        """
        self.labyrinth = Labyrinth(json_file)
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
        while carry_on:
            self.labyrinth.display()
            user_answer = input("In which direction do you want MacGyver to \
move ? Please enter 'u' for up, 'd' for down, 'l' for left and 'r' for \
right, or 'q' to quit : ")
            success = None
            if user_answer not in ["q", "u", "d", "l", "r"]:
                print("\nInvalid choice !")
                continue
            elif user_answer == "q":
                carry_on = False
            else:
                success = self.macgyver.move(user_answer)
                # 'success' becomes True or False after fighting the guard
                if success is not None:
                    carry_on = False
                    self.labyrinth.display()


def parse_arguments():
    """ Returns an arguments parser with a "json_file" argument. """
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", help="Choose a .json file containing a \
                        labyrinth to load")
    return parser.parse_args()


def main():
    """ Runs the game """
    argument = parse_arguments()
    game = GameText(argument.json_file)
    game.run()

if __name__ == "__main__":
    main()
