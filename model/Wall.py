from Field import Field
from constants import WALL_ICON

class Wall(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = WALL_ICON
