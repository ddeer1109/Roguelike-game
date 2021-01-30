from model.creatures.Creature import Creature
from model.constants import BANDIT

class Bandit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = BANDIT
        self.attack = 5
        self.health = 20

    def attack_player(self, player):
        player.health -= self.attack