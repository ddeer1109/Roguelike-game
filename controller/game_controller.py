from builtins import next
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from controller import engine
from view import ui, util
from model.Player import Player
from model.Wall import Wall
from model.Gate import Gate
PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def service_player_moves(key_pressed, room, player, current_room):
    k_pressed = str.lower(key_pressed)
    if k_pressed == "w":
        next_area = type(room.fields[player.x-1][player.y])
    
        if next_area is Gate:
            return current_room.gates["upper"].go_through_gate(player, "upper")
        elif next_area is not Wall:
            room.service_move_up(player)    
            return current_room    
    
    elif k_pressed == "s":
        next_area = type(room.fields[player.x+1][player.y])
        
        if next_area is Gate:
            return current_room.gates["bottom"].go_through_gate(player, "bottom")
        elif next_area is not Wall:
            room.service_move_down(player)
            return current_room
    
    elif k_pressed == "a":
        next_area = type(room.fields[player.x][player.y-1])
        
        if next_area is Gate:
            return current_room.gates["left"].go_through_gate(player, "left")
        elif next_area is not Wall:
            room.service_move_left(player)
            return current_room

    elif k_pressed == "d":
        next_area = type(room.fields[player.x][player.y+1])
        
        if next_area is Gate:
            return current_room.gates["right"].go_through_gate(player, "right")
        elif next_area is not Wall:
            room.service_move_right(player)
            return current_room
        
    return current_room
    


def main():
    print("START")
    player = Player(PLAYER_START_X, PLAYER_START_Y)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    engine.put_player_on_board(board, PLAYER_START_X, PLAYER_START_Y, player)
    util.clear_screen()
    # here
    current_room = board.central_room
    is_running = True
    
    while is_running:
        util.clear_screen()
        current_room.print_room()
        #Here changed mostly

        key = util.key_pressed()
        
        if key == 'q':
            is_running = False
        else:
            current_room = service_player_moves(key, current_room, player, current_room)

        if player.current_field == current_room.gates["right"]:
            # engine.put_player_on_board(board, board.boss_room.gates["bottom"].x, board.boss_room.gates["bottom"].y, player)
            # current_room = board
            current_room = current_room.gates["right"].go_through_gate(player, "right")
            
        
        if player.current_field == current_room.gates["left"]:
            # engine.put_player_on_board(board, board.boss_room.gates["bottom"].x, board.boss_room.gates["bottom"].y, player)
            # current_room = board
            current_room = current_room.gates["left"].go_through_gate(player, "left")
            
        
        
        

        
    