from model.board_objects.Field import Field
from model.constants import FOOD
import random

class Food(Field):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.icon = FOOD
        self.health_increase = random.randint(3, 10)


    def __repr__(self) -> str:
        return "Piece of food"