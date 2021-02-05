from model.board_objects.Field import Field
from model.constants import MAGIC_STICK


class MagicStick(Field):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.icon = MAGIC_STICK
        self.attack_increase = 6


    def __repr__(self) -> str:
        return "Magic stick"