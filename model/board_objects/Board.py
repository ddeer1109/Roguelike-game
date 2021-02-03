from model.creatures.Magic_bandit import MagicianBandit
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from model.board_objects.Room import Room
from model.board_objects.Gate import Gate
from model.creatures.Bandit import Bandit
from model.creatures.Archer_bandit import ArcherBandit
from model.constants import  UPPER, BOTTOM, LEFT, RIGHT, CENTRAL, BOSS
import random


class Board:
    def __init__(self, width, height):
        self.central_room, self.left_room,\
             self.right_room, self.boss_room\
                 = self.generate_rooms(width, height)
        self.generate_room_elements()
    

    def generate_rooms(self, width, height, count=4):
        return (Room(height, width) for _ in range(count))



    def generate_room_elements(self):

        for room in [self.central_room, self.left_room, self.right_room]:
            for _ in range(random.randint(3,7)): room.create_food()
            for _ in range(random.randint(1,4)): room.create_bandit()
            for _ in range(random.randint(1,3)): room.create_bandit(ArcherBandit)
            for _ in range(random.randint(0,2)): room.create_bandit(MagicianBandit)

        self.generate_gates()
        self.generate_keys()

    def generate_gates(self):
        self.central_room.create_gates(left=True, right=True)
        self.right_room.create_gates(left=True)
        self.left_room.create_gates(upper=True, right=True)
        self.boss_room.create_gates(bottom=True)


        self.central_room.gates[RIGHT].connect_gates(self.right_room.gates[LEFT], self.right_room)
        self.central_room.gates[LEFT].connect_gates(self.left_room.gates[RIGHT], self.left_room)

        self.right_room.gates[LEFT].connect_gates(self.central_room.gates[RIGHT], self.central_room)

        self.left_room.gates[RIGHT].connect_gates(self.central_room.gates[LEFT], self.central_room)
        self.left_room.gates[UPPER].connect_gates(self.boss_room.gates[BOTTOM], self.boss_room)
        
        self.boss_room.gates[BOTTOM].connect_gates(self.left_room.gates[UPPER], self.left_room)

    def generate_keys(self):
        
        key_central_left = self.central_room.create_key("Central left key")
        key_central_right = self.central_room.create_key("Central right key")
        key_left_upper = self.right_room.create_key("Left upper key")

        key_central_left.add_gate_to_key(self.central_room.gates[LEFT])
        key_central_right.add_gate_to_key(self.central_room.gates[RIGHT])
        key_left_upper.add_gate_to_key(self.left_room.gates[UPPER])


    def place_player(self, player):    
            self.central_room.fields[player.x][player.y] = player

    