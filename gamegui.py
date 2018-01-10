#! /usr/bin/env python3
# coding: utf-8

""" Sets GameGUI class.

This class manages the "graphical version" of the game "Help MacGyver
to escape from the labyrinth !"

"""

import argparse

import pygame
from pygame.locals import *

from labyrinth import Labyrinth
from macgyver import MacGyver
from syringe import Syringe


class GameGUI:
    """ Sets GameGUI class.

    The GameGUI class consists of 2 methods :
        - __init__()
        - run()

    """
    def __init__(self, json_file="labyrinth.json"):
        """ GameGUI constructor.

        Instantiates objects from Labyrinth, MacGyver and Syringe classes.

        """
        self.labyrinth = Labyrinth(json_file)
        self.macgyver = MacGyver(self.labyrinth)
        self.syringe = Syringe(self.labyrinth)

    def run(self):
        """ Manages the game progress with Pygame."""
        pygame.init()
        window = pygame.display.set_mode((600, 600))

        # Window icon
        icone = pygame.image.load("images/macgyver_32_40.png")
        pygame.display.set_icon(icone)

        # Window title
        pygame.display.set_caption("Help MacGyver to escape from the \
labyrinth !")

        # Background
        background = pygame.image.load("images/background_800_545.jpg").convert()
        window.blit(background, (0, 0))
        window.blit(background, (0, 100))

        # MacGyver
        macgyver = pygame.image.load("images/macgyver_32_40.png").convert_alpha()
        macgyver_position = self.labyrinth.get_position("M")
        window.blit(macgyver, (macgyver_position[0] * 40 + 4,
                               macgyver_position[1] * 40))

        # Guard
        guard = pygame.image.load("images/guard_32_36.png").convert_alpha()
        guard_position = self.labyrinth.get_position("G")
        window.blit(guard, (guard_position[0] * 40 + 4, guard_position[1] *
                            40 + 2))

        # Syringe elements
        needle = pygame.image.load("images/needle_20_20.png").convert_alpha()
        tube = pygame.image.load("images/tube_20_20.png").convert_alpha()
        ether = pygame.image.load("images/ether_20_20.png").convert_alpha()
        syringe_elements_positions = self.syringe.positions

        window.blit(needle, (syringe_elements_positions[0][0] * 40 + 10,
                             syringe_elements_positions[0][1] * 40 + 10))
        window.blit(tube, (syringe_elements_positions[1][0] * 40 + 10,
                           syringe_elements_positions[1][1] * 40 + 10))
        window.blit(ether, (syringe_elements_positions[2][0] * 40 + 10,
                            syringe_elements_positions[2][1] * 40 + 10))

        # Walls
        wall = pygame.image.load("images/wall_40_40.png").convert()
        walls_positions = self.labyrinth.get_walls_positions()
        for wall_position in walls_positions:
            window.blit(wall, (wall_position[0] * 40, wall_position[1] * 40))

        pygame.display.flip()

        # Allows to hold down a key and move faster
        pygame.key.set_repeat(400, 30)

        carry_on = True
        success = None

        while carry_on:

            # Loop speed
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    carry_on = False
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        success = self.macgyver.move("u")
                    elif event.key == K_DOWN:
                        success = self.macgyver.move("d")
                    elif event.key == K_LEFT:
                        success = self.macgyver.move("l")
                    elif event.key == K_RIGHT:
                        success = self.macgyver.move("r")

                # New display
                window.blit(background, (0, 0))
                window.blit(background, (0, 100))

                # Get new MacGyver position
                macgyver_position = self.macgyver.position
                window.blit(macgyver, (macgyver_position.x * 40 + 4,
                                       macgyver_position.y * 40))

                window.blit(guard, (guard_position[0] * 40 + 4,
                                    guard_position[1] * 40 + 2))

                # Items are no longer displayed once they have been picked up
                if "N" not in self.macgyver.collected_syringe_elements:
                    window.blit(needle, (syringe_elements_positions[0][0] *
                                         40 + 10,
                                         syringe_elements_positions[0][1] *
                                         40 + 10))
                if "T" not in self.macgyver.collected_syringe_elements:
                    window.blit(tube, (syringe_elements_positions[1][0] * 40 +
                                       10,
                                       syringe_elements_positions[1][1] * 40 +
                                       10))
                if "E" not in self.macgyver.collected_syringe_elements:
                    window.blit(ether, (syringe_elements_positions[2][0] * 40 +
                                        10,
                                        syringe_elements_positions[2][1] * 40 +
                                        10))

                walls_positions = self.labyrinth.get_walls_positions()
                for wall_position in walls_positions:
                    window.blit(wall, (wall_position[0] * 40,
                                       wall_position[1] * 40))

                pygame.display.flip()

            # 'success' becomes True or False after fighting the guard
            if success:
                you_win = pygame.image.load("images/you_win_200_200.png").convert()
                window.blit(you_win, (200, 200))
                pygame.display.flip()
                carry_on = False
            elif success == False:
                game_over = pygame.image.load("images/game_over_320_256.jpg").convert()
                window.blit(game_over, (140, 172))
                pygame.display.flip()
                carry_on = False

        pygame.quit()

        # Wait 4 seconds before closing the game window
        pygame.time.wait(4000)


def parse_arguments():
    """ Returns an arguments parser with a "json_file" argument. """
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", help="Choose a .json file containing a \
                        labyrinth to load")
    return parser.parse_args()


def main():
    """ Runs the game """
    argument = parse_arguments()
    game = GameGUI(argument.json_file)
    game.run()

if __name__ == "__main__":
    main()
