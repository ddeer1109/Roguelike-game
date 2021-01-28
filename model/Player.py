from model.Creature import Creature
from model.constants import PLAYER, CENTRAL_ROOM

class Player(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = PLAYER
        self.health = 100
        self.current_room = CENTRAL_ROOM