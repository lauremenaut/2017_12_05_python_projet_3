"""
Open a labyrinth .csv file as a dictionnary
and show available positions

"""

import pandas

dataframe = pandas.read_csv("labyrinth0.csv")

dataframe.index = ["A", "B", "C", "D", "E"]
dataframe.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
J'aimerais utiliser ça pour définir index et columns avec range(1, x_max) et range(1, y_max) :
x_max = len(dataframe[1]) # renvoie 5 (lignes)
y_max = len(dataframe.iloc[0]) # renvoie 15 (colonnes)
print(x_max, y_max)
"""
# print(dataframe)


""" Work in progress !!"""
available_positions = []
lines = []
for line in dataframe.iterrows():
    line_content = line[1]  # renvoie un objet contenant une ligne
    lines.append(line_content)

for line in lines:
    for character in line:
        if character != "X":
            available_positions.append(character) # je ne sais pas ajouter la position à la liste
        print(character)

# print(lines[2][2])

"""
i = 1
while i < 15:
    dataframe[i]
    i += 1
"""
