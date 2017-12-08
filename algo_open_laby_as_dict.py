"""
Open a labyrinth file as a dictionnary of tuples
and show available positions

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
    print(laby)

available_positions = []
for position, character in laby.items():
    if character == " ":
        available_positions.append(position)
print(available_positions)
