"""
Open a labyrinth .txt file as a dictionnary
and choose random available positions for 3 objects

"""

with open("labyrinth1.txt", 'r') as f:
    lines = f.readlines()
    laby = {}
    x_max = len(lines)
    y_max = len(lines[0])
    x = 0
    while x < x_max:
        y = 0
        while y < y_max:
            position = (x, y)
            character = lines[x][y]
            laby[position] = character
            y += 1
        x += 1
    print(laby.values())


""" Random choice of positions for 3 objects in the labyrinth """

import random


""" 1_Choice on available positions only """

# liste les positions disponibles
available_positions = []
for position, character in laby.items():
    if character == " ":
        available_positions.append(position)
print("Available positions : {}".format(available_positions))

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions_1 = random.sample(available_positions, 3)
print("Objects positions 1 : {}".format(objects_positions_1))


""" 2_On all positions, choose another one if not available (juste pour le fun !!) """

# liste toutes les positions
all_positions = []
for key in laby.keys():
    all_positions.append(key)

# choisit 3 positons parmi toutes les positions et recommence tant qu'on n'a pas 3 positions disponibles
objects_positions_2 = []
while len(objects_positions_2) < 3:
    object_position = random.choice(all_positions)
    if laby[object_position] == " ":
        objects_positions_2.append(object_position)
        continue
print("Objects positions 2 : {}".format(objects_positions_2))


""" 3_On all positions, choose another one if not available (juste pour le fun, bis !!) """

x = 0
y = 0

# choisit 3 positons parmi toutes les positions et recommence tant qu'on n'a pas 3 positions disponibles
objects_positions_3 = []
while laby[(x, y)] != " " or len(objects_positions_3) < 3:
    x = random.randint(1, x_max - 1)
    y = random.randint(1, y_max - 1)
    if laby[(x, y)] == " ":
        objects_positions_3.append((x, y))
        continue

print("Objects positions 3 : {}".format(objects_positions_3))
