from Creature import Creature

class Player(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 100