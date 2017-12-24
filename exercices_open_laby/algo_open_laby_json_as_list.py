"""
Open a labyrinth .json file as a list
and choose random available positions for 3 items

"""

import json
import random

with open("labyrinth1.json", 'r') as f:
    elements = json.load(f) # renvoie une liste de dictionnaires
    lines_list = []
    line = []
    for element in elements: # element est un dictionnaire
        for position, character in element.items():
            line.append(character)
            if character == "\n":
                lines_list.append(line)
                line = []

for line in lines_list:
    for character in line:
        print(character, end='')
print()

# liste les positions disponibles
available_positions = []

i = 0
for line in lines_list:
    j = 0
    for character in line:
        if character == " ":
            available_positions.append((i, j))
        j += 1
    i += 1

print("Available positions : {}".format(available_positions))

# choisit 3 positions parmi les positions disponibles, sans doublon
items_positions = random.sample(available_positions, 3)
print("Items positions : {}".format(items_positions))
