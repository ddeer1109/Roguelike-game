import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from view import util
from model.Empty_space import Empty_space
from model.Wall import Wall
from model.Gate import Gate
from model.Player import Player
import random

class Room:
    def __init__(self, width, height):
        self.fields = self.init_board(width, height)
        self.left_gate = None
        self.right_gate = None


    def init_board(self, width, height):
        board = []
        for row in range(height):
            inner_board = []
            for col in range(width):
                
                if row == 0 or row == height - 1:
                    added_area = Wall(row, col)
                elif col == 0 or col == width - 1:
                    added_area = Wall(row, col)
                else:
                    added_area = Empty_space(row, col)

                inner_board.append(added_area)
            board.append(inner_board)

        return board


    def print_room(self):
        for i in range(len(self.fields)):
            temp_str = ''
            for j in range(len(self.fields[0])):
                temp_str += str(self.fields[i][j])
            print(temp_str)
        print()            

    
    def create_upper_gate(self):
        current_index = random.randrange(3, len(self.fields[0]) - 1)
        for _ in range(3):
            self.fields[0][current_index] = Gate(0, current_index)
            current_index -= 1

    
    def create_bottom_gate(self):
        current_index = random.randrange(3, len(self.fields[0]) - 1)
        for _ in range(3):
            self.fields[-1][current_index] = Gate(len(self.fields)-1, current_index)
            current_index -= 1

    
    def create_left_gate(self):
        current_index = random.randrange(3, len(self.fields) - 1)
        left_side = 0
        for _ in range(3):
            self.fields[current_index][left_side] = Gate(current_index, left_side)
            current_index -= 1


    def create_right_gate(self):
        current_index = random.randrange(3, len(self.fields) - 1)
        right_side = -1
        for _ in range(3):
            self.fields[current_index][right_side] = Gate(current_index, right_side)
            current_index -= 1


    def create_gates(self, upper=False, bottom=False, left=False, right=False):
        if upper: self.create_upper_gate()
        if bottom: self.create_bottom_gate()
        if left: self.create_left_gate()
        if right: self.create_right_gate()

    
    def service_move_up(self, creature_object):
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_up()
        self.fields[creature_object.x][creature_object.y] = str(creature_object)


    def service_move_down(self, creature_object):
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_down()
        self.fields[creature_object.x][creature_object.y] = str(creature_object)

    def service_move_left(self, creature_object):
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_left()
        self.fields[creature_object.x][creature_object.y] = str(creature_object)


    def service_move_right(self, creature_object):
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_right()
        self.fields[creature_object.x][creature_object.y] = str(creature_object)


    