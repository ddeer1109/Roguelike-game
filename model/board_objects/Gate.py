from builtins import IndexError, next
from model.board_objects.Field import Field
from model.constants import GATE_ICON, UPPER, BOTTOM, LEFT, RIGHT



class Gate(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = GATE_ICON
        self.is_opened = False
        self.connection_gate = None
        self.connected_room = None
        self.oppening_key = None
    
    
    def __str__(self):
        if self.is_opened:
            self.icon = ' '
        else:
            self.icon = GATE_ICON
        return self.icon

    def open_gate(self):
        self.is_opened = True
        self.connection_gate.is_opened = True


    def connect_gates(self, gate, room):
        self.connection_gate = gate
        self.connected_room = room


    def go_through_gate(self, player_object, direction):
            if direction == LEFT:
                next_gate_x, next_gate_y = self.connection_gate.x, self.connection_gate.y-1 
            elif direction == RIGHT:
                next_gate_x, next_gate_y = self.connection_gate.x, self.connection_gate.y+1
            elif direction == UPPER:
                next_gate_x, next_gate_y = self.connection_gate.x-1, self.connection_gate.y 
            elif direction == BOTTOM:
                 next_gate_x, next_gate_y = self.connection_gate.x+1, self.connection_gate.y

            self.connected_room.fields[next_gate_x][next_gate_y] = str(player_object)
            player_object.x, player_object.y = next_gate_x, next_gate_y
            return self.connected_room


