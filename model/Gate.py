from Field import Field
from constants import GATE_ICON

class Gate(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = GATE_ICON
        self.opened = False

    def __str__(self):
        return self.icon
