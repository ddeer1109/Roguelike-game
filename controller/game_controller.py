from builtins import next
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from controller import engine
from view import ui, util
# from view.ui import UI
from model.creatures.Player import Player
from model.creatures.Bandit import Bandit
from model.fight.Fight import Fight
from model.board_objects.Wall import Wall
from model.board_objects.Gate import Gate
from model.constants import UPPER, BOTTOM, LEFT, RIGHT
from model.items.Key import Key
from model.items.Food import Food

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


class Main:
    @classmethod
    def service_player_inputs(cls, key_pressed, room, player):
        k_pressed = str.lower(key_pressed)

        # hello
        
        current_room = room 
        
        if k_pressed in ["w","a","s","d"]:
            current_room = cls.service_pressing_move_key(k_pressed, room, player)
                
        return current_room


    def get_data_after_key_press(pressed_key, player):
        if pressed_key == "w":
            modified_x, modified_y = player.x - 1, player.y
            direction = UPPER

        elif pressed_key == "s":
            modified_x, modified_y = player.x + 1, player.y
            direction = BOTTOM

        elif pressed_key == "a":
            modified_x, modified_y = player.x, player.y - 1
            direction = LEFT

        elif pressed_key == "d":
            modified_x, modified_y = player.x, player.y + 1
            direction = RIGHT

        return modified_x, modified_y, direction

    def service_pressing_move_key(key_pressed, room, player):
        modified_player_x, modified_player_y, direction = Main.get_data_after_key_press(key_pressed, player)

        next_object = room.fields[modified_player_x][modified_player_y]
        current_room = room

        if type(next_object) is Gate:
            current_gate = room.gates[direction]

            if not current_gate.is_opened:
                if current_gate.oppening_key in player.inventory:
                    del player.inventory[player.inventory.index(current_gate.oppening_key)]
                    current_gate.open_gate()
                    current_room = current_gate.go_through_gate(player, direction)

            else:
                current_room = current_gate.go_through_gate(player, direction)

        elif type(next_object) is not Wall:
            if type(next_object) is Key:
                player.inventory.append(next_object)
            elif type(next_object) is Food:
                player.eat_food(next_object.health_increase)
            elif type(next_object) is Bandit:
                fight = Fight(player, next_object)
                fight.print_fight()
                return current_room


            if direction == UPPER:
                room.service_move_up(player)
            elif direction == BOTTOM:
                room.service_move_down(player)
            elif direction == LEFT:
                room.service_move_left(player)
            elif direction == RIGHT:
                room.service_move_right(player)

        return current_room

    @staticmethod
    def main():
        print("START")
        player = Player(PLAYER_START_X, PLAYER_START_Y)
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

        engine.put_player_on_board(board, player)
        # util.clear_screen()
        # here
        current_room = board.central_room
        is_running = True

        ui.UI.display_room(current_room)

        while is_running:
            # util.clear_screen()
            ui.UI.display_room(current_room)
            ui.UI.display_statistics(player)
            # Here changed mostly

            key = util.Util.key_pressed()

            if key == 'q':
                is_running = False
            else:
                # TODO - check cls reference instead of Main
                current_room = Main.service_player_inputs(key, current_room, player)
