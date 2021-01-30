from model.board_objects.Field import Field
from model.constants import KEY

class Key(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = KEY
        self.opened_gate = None
    
    def add_gate_to_key(self, gate):
        self.opened_gate = gate
        gate.oppening_key = self
