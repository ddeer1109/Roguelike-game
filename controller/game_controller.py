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

        current_room = room 
        
        if key_pressed in ["w","a","s","d"]:
            direction = cls.convert_key_for_direction(key_pressed)
            current_room = cls.service_pressing_move_key(room, direction, player)
                
        return current_room

    # @staticmethod
    # def get_data_after_key_press(direction, player):
    #     if direction == UPPER:
    #         modified_x, modified_y = player.x - 1, player.y
    #         direction = UPPER

    #     elif direction == BOTTOM:
    #         modified_x, modified_y = player.x + 1, player.y
    #         direction = BOTTOM

    #     elif direction == LEFT:
    #         modified_x, modified_y = player.x, player.y - 1
    #         direction = LEFT

    #     elif direction == RIGHT:
    #         modified_x, modified_y = player.x, player.y + 1
    #         direction = RIGHT

    #     return modified_x, modified_y, direction

    @classmethod
    def convert_key_for_direction(cls, key_pressed):
        if key_pressed == 'w':
            return UPPER
        elif key_pressed == 's':
            return BOTTOM
        elif key_pressed == 'a':
            return LEFT
        elif key_pressed == 'd':
            return RIGHT

    @classmethod
    def service_pressing_move_key(cls, room, direction, player):
        current_room = room.service_pressing_move_key(direction, player)
        if room.move_all_bandits() == "game_over":
            return "game_over"

        return current_room

    @classmethod
    def main(cls):
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
                current_room = cls.service_player_inputs(key, current_room, player)
                if current_room == "game_over": 
                    is_running = False
                    return ui.UI.display_info("Thank you for your time")