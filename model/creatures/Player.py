from model.creatures.Creature import Creature
from model.constants import PLAYER, CENTRAL


class Player(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = PLAYER
        self.inventory = []

    def eat_food(self, food):
        self.health += food.health_increase
