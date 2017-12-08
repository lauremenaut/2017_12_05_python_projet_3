""" Open a labyrinth file as a list of lists """

with open("labyrinth1.txt", 'r') as f:
    lines = f.readlines()
    lines_list = []
    for line in lines:
        characters = []
        for character in line:
            characters.append(character)
        lines_list.append(characters)
    print(lines_list)
