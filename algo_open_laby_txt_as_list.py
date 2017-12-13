"""
Open a labyrinth .txt file as a list of lists
and choose random available positions for 3 objects

"""

import random

with open("labyrinth1.txt", 'r') as f:
    lines = f.readlines()
    lines_list = []
    for line in lines:
        characters = []
        for character in line:
            characters.append(character) # "characters" contient tous les caractères d'une ligne
        lines_list.append(characters) # "lines_list" contient tous les lignes de "characters"
    print(lines_list) # "lines_list" est une liste de listes

# liste les positions disponibles
available_positions = []
for line in lines_list:
    for character in line:
        if character == " ":
            position_x = lines_list.index(line)
            position_y = line.index(character)
            available_positions.append((position_x, position_y))
print(available_positions) # Les positions affichées n'ont pas le bon "y" ...

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions = random.sample(available_positions, 3)
print("Objects positions : {}".format(objects_positions))
