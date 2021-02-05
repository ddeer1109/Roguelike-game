from builtins import next
import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from controller import engine
from view import ui, util
from model.creatures.Player import Player
from model.constants import UPPER, BOTTOM, LEFT, RIGHT


PLAYER_ICON = '@'
PLAYER_START_X = 1
PLAYER_START_Y = 1

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


class Main:
    @classmethod
    def service_player_inputs(cls, key_pressed, room, player):

        game_state = room 
        
        if key_pressed in ["w","a","s","d"]:
            direction = cls.convert_key_for_direction(key_pressed)
            game_state = cls.service_pressing_move_key(room, direction, player)
        elif key_pressed == "i":
            ui.UI.display_full_statistics(player)
                
        return game_state


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
        game_state = room.service_pressing_move_key(direction, player)
        enemies_actions = Main.proceed_enemies_moves(room, player, 1)
        if enemies_actions == "game_over":
            return "game_over"
        return game_state

    @staticmethod
    def proceed_enemies_moves(room, player, moves_count=1):
        for _ in range(moves_count):
            if room.move_enemies(player) == "game_over":
                return "game_over"
            ui.UI.display_room(room)
        return room

    @classmethod
    def main(cls):
        player = Player(PLAYER_START_X, PLAYER_START_Y)
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

        engine.put_player_on_board(board, player)

        game_state = board.central_room
        is_running = True

        ui.UI.display_room(game_state)

        while is_running:
            if len(board.boss_room.enemy_creatures) == 0:
                return print("You have won congratulations")
            ui.UI.display_room(game_state)
            ui.UI.display_statistics(player)

            key = util.Util.key_pressed()

            if key == 'q':
                is_running = False
            else:
                game_state = cls.service_player_inputs(key, game_state, player)
                if game_state == "game_over": 
                    is_running = False
                    return ui.UI.display_info("Thank you for your time")