#! /usr/bin/env python3
# coding: utf-8

""" Sets GameGUI class

This class manages the "graphical version" of the game "Help MacGyver to escape
from the labyrinth !"
McGyver needs to find and pick up 3 items (a needle, a small plastic
tube and ether) in the labyrinth to make a syringe. Then, he will be
able to neutralize the guard and escape.

"""

import pygame
from pygame.locals import *

from labyrinth_GUI import Labyrinth
from macgyver_GUI import MacGyver
from syringe_GUI import Syringe


class GameGUI:
    """ Sets GameGUI class.

    The GameGUI class consists of 2 methods :
        - __init__()
        - run()
    It needs pygame library and Labyrinth, MacGyver and Syringe imported classes.

    """
    def __init__(self):
        self.labyrinth = Labyrinth("labyrinth_test_GUI.json")
        self.macgyver = MacGyver(self.labyrinth)
        self.syringe = Syringe(self.labyrinth)

    def run(self):
        pygame.init()

        window = pygame.display.set_mode((600, 600))

        background = pygame.image.load("background_450_450.jpg").convert()
        window.blit(background, (0, 0))
        window.blit(background, (160, 0))
        window.blit(background, (0, 160))
        window.blit(background, (160, 160))

        macgyver = pygame.image.load("macgyver_32_40.png").convert_alpha()
        macgyver_position = self.labyrinth.get_position("M")
        # x et y sont inversés dans mes classes ...
        window.blit(macgyver, (macgyver_position[1] * 40 + 4, macgyver_position[0] * 40))

        guard = pygame.image.load("guard_32_36.png").convert_alpha()
        guard_position = self.labyrinth.get_position("G")
        window.blit(guard, (guard_position[1] * 40 + 4, guard_position[0] * 40 + 2))

        needle = pygame.image.load("needle_20_20.png").convert_alpha()
        tube = pygame.image.load("tube_20_20.png").convert_alpha()
        ether = pygame.image.load("ether_20_20.png").convert_alpha()
        syringe_elements_positions = self.syringe.dispatch()
        window.blit(needle, (syringe_elements_positions[0][1] * 40 + 10, syringe_elements_positions[0][0] * 40 + 10))
        window.blit(tube, (syringe_elements_positions[1][1] * 40 + 10, syringe_elements_positions[1][0] * 40 + 10))
        window.blit(ether, (syringe_elements_positions[2][1] * 40 + 10, syringe_elements_positions[2][0] * 40 + 10))

        wall = pygame.image.load("wall_40_40.png").convert()

        walls_positions = self.labyrinth.get_walls_positions()
        for wall_position in walls_positions:
            window.blit(wall, (wall_position[1] * 40, wall_position[0] * 40))

        pygame.display.flip()

        carry_on = True

        while carry_on:
            for event in pygame.event.get():
                if event.type == QUIT:
                    carry_on = False
        pygame.quit()


def main():
    game = GameGUI()
    game.run()

if __name__ == "__main__":
    main()
