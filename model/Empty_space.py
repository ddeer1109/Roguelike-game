from model.Field import Field
from model.constants import EMPTY_AREA_ICON

class Empty_space(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = EMPTY_AREA_ICON

    def __str__(self):
        return self.icon
