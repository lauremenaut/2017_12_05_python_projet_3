""" Models the game : Help MacGyver to escape from the labyrinth """


class Positionable:
    def __init__(self, position):
        self.position = position


class MacGyver(Positionable):
    def __init__(self, position, laby):
        super().__init__(position)
        self.picked_objects = 0
        self.laby = laby

    def move(self, direction, labyrinth):
        pass
        is_free(next_position)

    def pick_up_object(self):
        self.picked_objects += 1

    def neutralize_guard(self):
        pass


class Guard(Positionable):
    def __init__(self, position):
        super().__init__(position)

    def block_exit(self):
        pass


class Object(Positionable):
    def __init__(self, position, name):
        super().__init__(position)
        self.name = name


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

class Labyrinth:
    def __init__(self, file="labyrinth.json"): # chargement du laby dans un attribut
        pass
        # width=15 (attribut de classe)
        # entrance, exit, walls
        # positions disponibles ?
    def get_available_positions(self):
        pass

    def is_a_wall(self):
        pass

class GameText:
    def __init__(self):
        laby = Labyrinth()
        mcgyver = MacGyver(laby)
        guard = Guard()

    def start(self):
        pass # boucle qui affiche le laby, pose question à l'utilisateur ...
    """    
        if "q"
            if h b d g: # saisie sécurisée pour reposer la question si invalide
                self.mcgyver(move, reponse) # doit savoir si dispo, objets = besoin de Labyrinth
# après déplacement, maj position McG
    """
class GameGUI:
    def __init__(self):
        laby = Labyrinth()
        mcgyver = MacGyver()
        guard = Guard()

    def start(self):
        pass # boucle jusqu'à la fin du jeu (while True / break ou variable "continuer" True > False)
