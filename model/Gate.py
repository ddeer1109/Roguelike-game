from builtins import next
from model.Field import Field
from model.constants import GATE_ICON


class Gate(Field):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = GATE_ICON
        self.isopened = False
        self.connection_gate = None
        self.connected_room = None
    
    
    def __str__(self):
        return self.icon


    def connect_gates(self, gate, room):
        self.connection_gate = gate
        self.connected_room = room


    def go_through_gate(self, player_object):
        next_gate_x, next_gate_y = self.connection_gate.x, self.connection_gate.y 
        
        self.connected_room.fields[next_gate_x][next_gate_y] = str(player_object)
        player_object.x, player_object.y = next_gate_x, next_gate_y
        return self.connected_room