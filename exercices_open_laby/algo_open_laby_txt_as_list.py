"""
Open a labyrinth .txt file as a list of lists
and choose random available positions for 3 objects

"""

import random

with open("labyrinth1.txt", 'r') as f:
    #lines = f.readlines()
    lines_list = []
    #for line in lines:
    # -tc- Ici, la lecture ligne par ligne peut directement se faire avec une
    # -tc- boucle for sur f
    for line in f:
        # -tc- la transformation de line en une liste de caractères peut se faire
        # -tc- directement avec list(line)
        # -tc- Mais ton code fonctionne
        characters = []
        for character in line:
            # -tc- Techniquement, il faudrait faire attention de ne pas inclure
            # -tc- les caractères de fin de ligne.
            if character != '\n':
                characters.append(character) # "characters" contient tous les caractères d'une ligne
        lines_list.append(characters) # "lines_list" contient tous les lignes de "characters"

# print(lines_list) # "lines_list" est une liste de listes

# -tc- pour mieux se rendre compte de ce que donne le labyrinthe, on peut
# -tc- ligne par ligne. Il vient:
for line in lines_list:
    for c in line:
        print(c, end='')
print()

# liste les positions disponibles
available_positions = []
# -tc- le plus simple et efficace est d'utiliser un compteur sur les lignes et
# -tc- les colonnes
i = 0
for line in lines_list:
    j = 0
    for character in line:
        if character == " ":
            # -tc ne va pas fonctionner si il y a plusieurs lignes identiques
            # position_x = lines_list.index(line)
            # -tc- rechercher à chaque fois le caractère " " dans line ne va pas
            # -tc- fonctionner si il y a plusieurs " " sur la même ligne
            #position_y = line.index(character)
            # -tc- tu utilises directement la valeur des compteurs i et j
            available_positions.append((i, j))
        j += 1
    i += 1
    
print(available_positions) # Les positions affichées n'ont pas le bon "y" ...

# -tc- le plus simple pour le même résultat est d'utiliser la fonction enumerate()
available_positions = []
for i, line in enumerate(lines_list):
    for j, c in enumerate(line):
        if c == " ":
            available_positions.append((i, j))
print(available_positions)

# choisit 3 positions parmi les positions disponibles, sans doublon
objects_positions = random.sample(available_positions, 3)
print("Objects positions : {}".format(objects_positions))
