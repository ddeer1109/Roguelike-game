import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from model.board_objects.Room import Room
from model.board_objects.Gate import Gate
from model.constants import  UPPER, BOTTOM, LEFT, RIGHT, CENTRAL, BOSS


class Board:
    def __init__(self, width, height):
        self.central_room, self.left_room,\
             self.right_room, self.boss_room\
                 = self.generate_rooms(width, height)
        self.generate_gates()
    

    def generate_rooms(self, width, height, count=4):
        return (Room(height, width) for _ in range(count))



    def generate_gates(self):

        self.central_room.create_gates(left=True, right=True)
           
        
        self.right_room.create_gates(left=True)
        self.left_room.create_gates(upper=True, right=True)
        self.boss_room.create_gates(bottom=True)


        self.central_room.gates[RIGHT].connect_gates(self.right_room.gates[LEFT], self.right_room)
        self.central_room.gates[LEFT].connect_gates(self.left_room.gates[RIGHT], self.left_room)

        self.left_room.gates[RIGHT].connect_gates(self.central_room.gates[LEFT], self.central_room)
        self.left_room.gates[UPPER].connect_gates(self.boss_room.gates[BOTTOM], self.boss_room)
        
        self.right_room.gates[LEFT].connect_gates(self.central_room.gates[RIGHT], self.central_room)
        
        self.boss_room.gates[BOTTOM].connect_gates(self.left_room.gates[UPPER], self.left_room)
        

        self.central_room.create_key(10, 10)
        self.central_room.create_key(12, 15)

        self.left_room.create_key(12, 11)


    def place_player(self, player):    
            self.central_room.fields[player.x][player.y] = player
            '''elif room == LEFT:
                self.left_room.fields[x][y] = str(player_object)
            elif room == RIGHT:
                self.right_room.fields[x][y] = str(player_object)
            elif room == BOSS:
                self.boss_room.fields[x][y] = str(player_object) '''
            
         
    # def go_through_gate()
    
    #############################    






#
# board = Board(20, 30)
# board.central_room.print_room()
# board.right_room.print_room()
# board.left_room.print_room()
# board.boss_room.print_room()
