"""
Open a labyrinth .xlsx file as a dictionnary
and choose random available positions for 3 objects

"""

import random

import xlrd # module qui permet de lire des feuilles Excel

laby = {}

wb = xlrd.open_workbook("labyrinth1.xlsx") # permet d'accéder au classeur
sh = wb.sheet_by_name(u"Feuil1") # permet d'accéder à la 1ère feuille

i = 0
while i < sh.nrows: # i = 0 à 14
    line = sh.row_values(i)
    j = 0
    while j < sh.ncols: # j = 0 à 14
        character = line[j]
        laby[(i, j)] = character
        j += 1
    i += 1
print(laby.values())

# liste les positions disponibles
available_positions = []
for position, character in laby.items():
    if character == "":
        available_positions.append(position)
print("Available positions : {}".format(available_positions))

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions = random.sample(available_positions, 3)
print("Objects positions : {}".format(objects_positions))
