from model.board_objects.Field import Field
from model.constants import MANA_POTION
import random


class ManaPotion(Field):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.icon = MANA_POTION
        self.mana_increase = random.randint(5,15)

    def __repr__(self) -> str:
        return "Mana potion"

    