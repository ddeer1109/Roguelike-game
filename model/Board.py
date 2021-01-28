import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from model.Room import Room
from model.Gate import Gate


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


        self.central_room.gates["right"].connect_gates(self.right_room.gates["left"], self.right_room)
        self.central_room.gates["left"].connect_gates(self.left_room.gates["right"], self.left_room)

        self.left_room.gates["right"].connect_gates(self.central_room.gates["left"], self.central_room)
        self.left_room.gates["upper"].connect_gates(self.boss_room.gates["bottom"], self.boss_room)
        
        self.right_room.gates["left"].connect_gates(self.central_room.gates["right"], self.central_room)
        
        self.boss_room.gates["bottom"].connect_gates(self.left_room.gates["upper"], self.left_room)
        


    def place_player(self, room, x, y, player_object):    
            if room == "central":
                self.central_room.fields[x][y] = str(player_object)
            elif room == "left":
                self.left_room.fields[x][y] = str(player_object)
            elif room == "right":
                self.right_room.fields[x][y] = str(player_object)
            elif room == "boss":
                self.boss_room.fields[x][y] = str(player_object) 
            
         
    # def go_through_gate()
    
    #############################    






#
# board = Board(20, 30)
# board.central_room.print_room()
# board.right_room.print_room()
# board.left_room.print_room()
# board.boss_room.print_room()
