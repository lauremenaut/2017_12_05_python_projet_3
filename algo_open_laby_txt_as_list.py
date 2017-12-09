""" Open a labyrinth file as a list of lists """

with open("labyrinth1.txt", 'r') as f:
    lines = f.readlines()
    lines_list = []
    for line in lines:
        characters = []
        for character in line:
            characters.append(character) # "characters" contient tous les caractères d'une ligne
        lines_list.append(characters) # "lines_list" contient tous les lignes de "characters"
    print(lines_list) # "lines_list" est une liste de listes



""" Random choice of positions for 3 objects in the labyrinth """

""" Pas pratique, il faudrait récupérer les index des positions choisies, plutôt
 que leur contenu : comment faire ? - Non terminé. """

import random

random_lines = random.choices(lines_list, k=3)
objects_positions = []
object_position = "X"
while object_position != " ":
    for line in random_lines:
        object_position = random.choice(line)
        if object_position == " ":
            objects_positions.append(object_position)
            continue
print("Objects positions : {}".format(objects_positions))
