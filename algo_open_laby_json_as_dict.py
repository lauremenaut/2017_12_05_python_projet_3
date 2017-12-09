"""
Open a labyrinth .json file as a dictionnary
and choose random available positions for 3 objects

"""

import json
import random


with open("labyrinth0.json", 'r') as f:
    elements = json.load(f) # renvoie une liste de dictionnaires

    laby = {}

    i = 0

    while i < (len(elements)):
        element = elements[i] # renvoie un dictionnaire contenant une clé (chaine contenant tuple) et une valeur (chaine contenant caractère)
        position_key = element.keys() # renvoie une "clé de dictionnaire" contenant une chaine contenant le tuple
        character_value = element.values() # renvoie une "valeur de dictionnaire" contenant une chaine contenant le caractère

        for position_tuple in position_key: # renvoie la chaîne contenant le tuple de position
            pass
        for character in character_value: # renvoie la chaîne contenant le caractère
            pass
        laby[position_tuple] = character
        i += 1
    print(laby)

# liste les positions disponibles
available_positions = []
for position, character in laby.items():
    if character == " ":
        available_positions.append(position)
print("Available positions : {}".format(available_positions))

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions = random.sample(available_positions, 3)
print("Objects positions : {}".format(objects_positions))
