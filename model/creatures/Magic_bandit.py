from model.creatures.Creature import Creature
from model.creatures.Bandit import Bandit
from model.constants import MAGIC, MAGIC_ATTACK, MELEE_ATTACK
from model.items import Mana_potion, Food
import random

class MagicianBandit(Bandit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.mana = 30
        self.icon = MAGIC
        self.attack = super().get_random_stat(2,4)
        self.defence = 0
        self.health = super().get_random_stat(20,25)
        self.dropping_items = [Mana_potion.ManaPotion]
    def __repr__(self) -> str:
        return "Magician Bandit"


    def melee_attack(self):
        return super().melee_attack()

    def magic_attack(self):
        return super().magic_attack()

    def get_possible_moves_list(self):
        if self.mana == 0:
            return MELEE_ATTACK
        return MAGIC_ATTACK

    def drop_item(self, room):
        item = random.choice(self.dropping_items)
        del room.bandits[room.bandits.index(self)]
        room.fields[self.x][self.y] = item(self.x, self.y)