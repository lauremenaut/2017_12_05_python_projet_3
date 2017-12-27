#! /usr/bin/env python3
# coding: utf-8

""" Defines GameText class

This class manages the "textual version" of the game "Help MacGyver to
escape from the labyrinth !"
McGyver needs to find and pick up 3 items (a needle, a small plastic
tube and ether) in the labyrinth before neutralizing the guard and being
able to escape.

"""

from labyrinth import *
from macgyver import *
from guard import *
from syringe import *
from position import *


class GameText:
    def __init__(self):
        self.labyrinth = Labyrinth()
        self.macgyver = MacGyver(self.labyrinth)
        self.syringe = Syringe(self.labyrinth)
        # self.guard = Guard() # à supprimer ?

    def start(self):
        continuer = True
        print("Help MacGyver to escape from the labyrinth : he needs to pick \
up a needle, a tube and ether before fighting the guard !")
        while continuer:
            self.labyrinth.display()
            user_answer = input("In which direction do you want MacGyver to \
move ? Please enter 'u' for up, 'd' for down, 'l' for left and 'r' for \
right, or 'q' to quit : ")
            if user_answer not in ["q", "u", "d", "l", "r"]:
                print("Invalid choice !")
                continue
            elif user_answer == "q":
                continuer = False
            else:
                self.macgyver.move(user_answer)


def main():
    game = GameText()
    game.start()

if __name__ == "__main__":
    main()
