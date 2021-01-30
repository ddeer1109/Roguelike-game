from model.board_objects.Field import Field
from model.constants import FOOD

class Food(Field):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.icon = FOOD
        self.health_increase = 10
