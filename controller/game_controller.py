import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from controller import engine
from view import ui, util
from model.Player import Player
from model.Wall import Wall

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def service_player_moves(key_pressed, room, player):
    k_pressed = str.lower(key_pressed)
    if k_pressed == "w":
        
        if type(room.fields[player.x-1][player.y]) is not Wall:
            room.service_move_up(player)    
        
    elif k_pressed == "s":
        
        if type(room.fields[player.x+1][player.y]) is not Wall:
            room.service_move_down(player)
    
    elif k_pressed == "a":
        
        if type(room.fields[player.x][player.y-1]) is not Wall:
            room.service_move_left(player)

    elif k_pressed == "d":
        
        if type(room.fields[player.x][player.y+1]) is not Wall:
            room.service_move_right(player)
   
    
    


def main():
    print("START")
    player = Player(PLAYER_START_X, PLAYER_START_Y)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    engine.put_player_on_board(board, PLAYER_START_X, PLAYER_START_Y, player)
    util.clear_screen()
    board.central_room.print_room()
    is_running = True
    
    while is_running:
        if player.current_field == "G":
            engine.put_player_on_board(board, player)
        ui.display_board(board)
    
        key = util.key_pressed()
        
        if key == 'q':
            is_running = False
        else:
            service_player_moves(key, board.central_room, player)
        
        util.clear_screen()
        board.central_room.print_room()
        
    