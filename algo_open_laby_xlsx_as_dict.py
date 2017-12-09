"""
Open a labyrinth .xlsx file as a dictionnary
and choose random available positions for 3 objects

"""

with open("labyrinth0.xlsx", 'rb') as f:
    lines = f.readlines()
    laby = {}
    x_max = 5
    y_max = 15

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
# renvoie des valeurs incorrectes. Le chargement du fichier.xlsx doit se faire différemment.
