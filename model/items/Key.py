from model.board_objects.Field import Field

class Key(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = 'K'
        self.opened_gate = None
    
    def add_gate_to_key(self, gate):
        self.opened_gate = gate

    def __str__(self):
        return self.icon