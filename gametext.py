#! /usr/bin/env python3
# coding: utf-8

""" Defines GameText class

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
    def __init__(self):
        self.labyrinth = Labyrinth()
        self.macgyver = MacGyver(self.labyrinth)
        self.syringe = Syringe(self.labyrinth)

    def start(self):
        continuer = True
        print("\nHelp MacGyver to escape from the labyrinth : he needs to pick \
up a needle, a tube and ether before fighting the guard !")
        while continuer is not False:
            self.labyrinth.display()
            user_answer = input("In which direction do you want MacGyver to \
move ? Please enter 'u' for up, 'd' for down, 'l' for left and 'r' for \
right, or 'q' to quit : ")
            if user_answer not in ["q", "u", "d", "l", "r"]:
                print("\nInvalid choice !")
                continue
            elif user_answer == "q":
                continuer = False
            else:
                continuer = self.macgyver.move(user_answer)
                if not continuer:
                    self.labyrinth.display()


def main():
    game = GameText()
    game.start()

if __name__ == "__main__":
    main()
