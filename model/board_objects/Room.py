import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from view import util
from model.board_objects.Empty_space import Empty_space
from model.board_objects.Wall import Wall
from model.board_objects.Gate import Gate
from model.creatures.Player import Player
from model.creatures.Bandit import Bandit
from model.constants import UPPER, BOTTOM, LEFT, RIGHT
from model.items.Key import Key
from model.items.Food import Food
import random

class Room:
    def __init__(self, height, width):
        self.fields = self.init_board(height, width)
        # self.upper_gate = None
        # self.bottom_gate =None
        # self.left_gate = None
        # self.right_gate = None
        self.gates = {
            UPPER: None,
            BOTTOM: None,
            LEFT: None,
            RIGHT: None
        }
        ######
    def init_board(self, height,width):
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


    def create_key(self, x, y):
        key = Key(x, y)
        self.fields[x][y] = key
        return self.fields[x][y]

    def create_food(self, x, y):
        food = Food(x,y)
        self.fields[x][y] = food

    def create_bandit(self, x, y):
        bandit = Bandit(x, y)
        self.fields[x][y] = bandit

####################    
    def create_upper_gate(self):
        first_row_index = 0 
        row_length = len(self.fields[0])
        
        column_index = random.randrange(first_row_index + 1, row_length-1)
        
        gate = Gate(first_row_index, column_index)
        self.fields[first_row_index][column_index] = gate
        
        self.gates[UPPER] = gate
    
    def create_bottom_gate(self):
        first_col_index = 0
        row_length = len(self.fields[0])
        col_length = len(self.fields)
        
        column_index = random.randrange(first_col_index + 1, row_length-1)

        gate = Gate(col_length - 1, column_index)
        self.fields[col_length - 1][column_index] = gate
        
        self.gates[BOTTOM] = gate

    def create_left_gate(self):
        first_col_index = 0
        first_row_index = 0
        col_length = len(self.fields)
        
        row_index = random.randrange(first_row_index + 1, col_length-1)
    
        gate = Gate(row_index, first_col_index)
        self.fields[row_index][first_col_index] = gate
        
        self.gates[LEFT] = gate


    def create_right_gate(self):
        first_row_index = 0
        row_length = len(self.fields[0])
        col_length = len(self.fields)
        row_index = random.randrange(first_row_index + 1, col_length-1)
        
        gate = Gate(row_index, row_length - 1)
        self.fields[row_index][row_length - 1] = gate
        
        self.gates[RIGHT] = gate

##################3
    def create_gates(self, upper=False, bottom=False, left=False, right=False):
        if upper: self.create_upper_gate()
        if bottom: self.create_bottom_gate()
        if left: self.create_left_gate()
        if right: self.create_right_gate()

    
    def service_move_up(self, creature_object):
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_up()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = str(creature_object)


    def service_move_down(self, creature_object):
        
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_down()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = str(creature_object)


    def service_move_left(self, creature_object):
        
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_left()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = str(creature_object)


    def service_move_right(self, creature_object):
        
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_right()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = str(creature_object)

    
    def service_moving_of_direction(self, player, direction):
        if direction == UPPER:
            self.service_move_up(player)
        elif direction == BOTTOM:
            self.service_move_down(player)
        elif direction == LEFT:
            self.service_move_left(player)
        elif direction == RIGHT:
            self.service_move_right(player)

    