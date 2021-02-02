from os import error
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
from model.fight.Fight import Fight
import random


class Room:
    def __init__(self, height, width):
        self.fields = self.init_board(height, width)
        self.gates = {
            UPPER: None,
            BOTTOM: None,
            LEFT: None,
            RIGHT: None
        }
        self.bandits = []

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
        return bandit

    def add_bandit(self, bandit):
        self.bandits.append(bandit)

    def move_all_bandits(self):
        current_room = self

        for bandit in self.bandits:

            current_room = self.service_enemies_actions(bandit)
        
        return current_room

    def is_next_object_empty(self, creature_object):
        if creature_object.direction == UPPER:
            if type(self.fields[creature_object.x - 1][creature_object.y]) is Empty_space:
                return True
        elif creature_object.direction == BOTTOM:
            if type(self.fields[creature_object.x + 1][creature_object.y]) is Empty_space:
                return True
        elif creature_object.direction == LEFT:
            if type(self.fields[creature_object.x][creature_object.y - 1]) is Empty_space:
                return True
        elif creature_object.direction == RIGHT:
            if type(self.fields[creature_object.x][creature_object.y + 1]) is Empty_space:
                return True 

        return False

    def service_interaction_with_gate(self, direction, player):
        # if type(next_object) is Gate:
        current_gate = self.gates[direction]
        room_after_stepping_into_gate = current_gate.service_interaction(player, direction)
        
        if type(room_after_stepping_into_gate) is Room:
            self.fields[player.x][player.y] = Empty_space(player.x, player.y)
            return room_after_stepping_into_gate
        else:
            return self


    def service_interaction_with_creature(self, moving_object, next_object):
        # if type(next_object) is not Wall:
            
            # if type(next_object) in [Key, Food]:  
            #     player.service_picking_item(next_object)
            
            # elif type(next_object) is Bandit:
        if type(moving_object) is not Player:
            result_of_fight = Fight(next_object, moving_object).service_fight()
        else:
            result_of_fight = Fight(moving_object, next_object).service_fight()


        if result_of_fight == "victory":
            if type(moving_object) is Player:
                self.fields[next_object.x][next_object.y] = Empty_space(next_object.x, next_object.y)
                del self.bandits[self.bandits.index(next_object)]
            else:
                self.fields[moving_object.x][moving_object.y] = Empty_space(moving_object.x, moving_object.y)
                del self.bandits[self.bandits.index(moving_object)]
        
        elif result_of_fight == "defeat":
            raise error("You have lost. Game over.")

        return result_of_fight
        

        # current_room.service_moving_of_direction(player, direction)
        # current_room.move_all_bandits()

    def get_objects_around_creature(self, creature_object, type_of_objects):
        coords = creature_object.get_coords_around()
        objects = [self.fields[coord[0]][coord[1]] for coord in coords if type(self.fields[coord[0]][coord[1]]) is type_of_objects]

        return objects


    def service_enemies_actions(self, enemy_object):
        next_x, next_y, direction = enemy_object.get_data_after_key_press(enemy_object.direction)
        enemy_object.update_steps()

        next_object = self.fields[next_x][next_y]

        objects_around = self.get_objects_around_creature(enemy_object, Player)

        if Player in list(map(type, objects_around)):
            fight_result = self.service_interaction_with_creature(enemy_object, objects_around[0])
            if fight_result == "victory":
                self.fields[enemy_object.x][enemy_object.y] = Food(enemy_object.x, enemy_object.y)

        elif type(next_object) in [Gate, Wall, Key, Food]:
            enemy_object.direction = enemy_object.change_direction()
        else:
            self.service_moving_of_direction(enemy_object, enemy_object.direction)

        
        
        


    def service_pressing_move_key(self, direction, player):
        
        modified_player_x, modified_player_y, direction = player.get_data_after_key_press(direction)

        next_object = self.fields[modified_player_x][modified_player_y]
        current_room = self

        if type(next_object) is Gate:
            current_room = self.service_interaction_with_gate(direction, player)
            return current_room
        
        # objects_around = self.get_objects_around_creature(player, Bandit)
        
        # if Bandit in list(map(type, objects_around)):
        if type(next_object) is Bandit:
            fight_result = self.service_interaction_with_creature(player, next_object)
            if fight_result == "victory":
                self.fields[next_object.x][next_object.y] = Food(next_object.x, next_object.y)

        elif type(next_object) is not Wall:
                if type(next_object) in [Key, Food]:
                    player.service_picking_item(next_object)

                self.service_moving_of_direction(player, direction)

            
        #     if type(player) is Player:
        #         if type(next_object) in [Key, Food]:
        #             player.service_picking_item(next_object)
        #             self.service_moving_of_direction(player, direction)
            
        #     # elif type(player) is Bandit:
        #     #     if type(next_object) is Empty_space:
        #     #         self.service_moving_of_direction(player, direction)
        # elif type(next_object) in [Key, Food, Wall] and type(player) is not Player:
        #     player.change_direction()
        #     player.update_steps()
        # # current_room = self.move_all_bandits()
        return current_room

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
        self.fields[creature_object.x][creature_object.y] = creature_object


    def service_move_down(self, creature_object):
        
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_down()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = creature_object


    def service_move_left(self, creature_object):
        
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_left()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = creature_object


    def service_move_right(self, creature_object):
        
        self.fields[creature_object.x][creature_object.y] = Empty_space(creature_object.x, creature_object.y)
        creature_object.move_right()
        creature_object.current_field = self.fields[creature_object.x][creature_object.y]
        self.fields[creature_object.x][creature_object.y] = creature_object

    
    def service_moving_of_direction(self, player, direction):
        if direction == UPPER:
            self.service_move_up(player)            
        elif direction == BOTTOM:
            self.service_move_down(player)
        elif direction == LEFT:
            self.service_move_left(player)
        elif direction == RIGHT:
            self.service_move_right(player)

    