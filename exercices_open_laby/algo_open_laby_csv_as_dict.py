"""
Open a labyrinth .csv file as a dictionnary
and choose random available positions for 3 objects

"""

import random
import csv

with open("labyrinth1.csv", newline='') as f:
    reader = csv.reader(f) # reader est un objet qui contient des listes de chaînes de caractères

    lines_list = []

    for line in reader: # line est une liste de chaînes de caractères
        laby_line = ' '.join(line) # laby_line est une chaîne concaténée obtenue à partir des caractères d'une "line"

        characters = []
        for character in laby_line:
            characters.append(character)

        lines_list.append(characters)

for line in lines_list:
    for c in line:
        print(c, end='')
    print()







"""
import pandas

dataframe = pandas.read_csv("labyrinth1.csv")

dataframe.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dataframe.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

J'aimerais utiliser ça pour définir index et columns avec range(1, x_max) et range(1, y_max) :
x_max = len(dataframe[1]) # renvoie 15 (lignes)
y_max = len(dataframe.iloc[0]) # renvoie 15 (colonnes)
print(x_max, y_max)

# print(dataframe)

laby = {}

for line in dataframe.iterrows(): # line est un tuple (index, contenu de la ligne)
    i = line[0]
    j = 1
    for character in line[1]:
        laby[(i, j)] = character
        j += 1
# print(laby.values())


# liste les positions disponibles
available_positions = []
for position, character in laby.items():
    if character == " ":
        available_positions.append(position)
print("Available positions : {}".format(available_positions))

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions = random.sample(available_positions, 3)
print("Objects positions : {}".format(objects_positions))
"""