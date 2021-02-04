from model.creatures.Creature import Creature
from model.constants import BOSS_ICON

class Boss(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = BOSS_ICON
