"""
Open a labyrinth .json file as a dictionnary
and choose random available positions for 3 objects

"""

import json
import random

with open("labyrinth0.json", 'r') as f:
    elements = json.load(f) # renvoie une liste de dictionnaires
laby = {}
for element in elements:
    for position_tuple, character in element.items():
        laby[position_tuple] = character
print(laby)

# -tc- Je pense qu'une liste de liste serait plus naturelle dans le fichier json.

# liste les positions disponibles
available_positions = []
for position, character in laby.items():
    if character == " ":
        available_positions.append(position)
print("Available positions : {}".format(available_positions))

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions = random.sample(available_positions, 3)
print("Objects positions : {}".format(objects_positions))
