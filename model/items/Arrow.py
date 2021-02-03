from model.board_objects.Field import Field
from model.constants import ARROW
import random

class Arrow(Field):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.icon = ARROW
        self.count = random.randrange(2,5)


    def __repr__(self) -> str:
        return "Arrow"