from model.board_objects.Field import Field
from model.constants import BOW


class Bow(Field):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.icon = BOW
        self.attack_increase = 4


    def __repr__(self) -> str:
        return "Wooden bow"