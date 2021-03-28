from model.board_objects.Field import Field
from model.constants import WALL_ICON

class Wall(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = WALL_ICON
    
    def __str__(self):
        return self.icon