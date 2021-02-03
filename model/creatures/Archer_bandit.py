from model.creatures.Creature import Creature
from model.creatures.Bandit import Bandit
from model.constants import ARCHER, MELEE_ATTACK, RANGE_ATTACK
from model.items import Arrow
from model.items.Food import Food
import random

class ArcherBandit(Bandit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.arrows = 10
        self.icon = ARCHER
        self.attack = super().get_random_stat(3,6)
        self.defence = super().get_random_stat(0,2)
        self.health = super().get_random_stat(20,30)

        self.dropping_items = [Arrow.Arrow, Arrow.Arrow, Arrow.Arrow, Food]

    def __repr__(self) -> str:
        return "Archer Bandit"

    def melee_attack(self):
        return super().melee_attack()

    def range_attack(self):
        return super().range_attack()

    def get_possible_moves_list(self):
        if self.arrows == 0:
            return MELEE_ATTACK
        return RANGE_ATTACK

    def drop_item(self, room):
        item = random.choice(self.dropping_items)
        del room.bandits[room.bandits.index(self)]
        room.fields[self.x][self.y] = item(self.x, self.y)