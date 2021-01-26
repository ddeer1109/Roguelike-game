from Empty_space import Empty_space
from Wall import Wall
from Gate import Gate
import random

class Room:
    def __init__(self, width, height):
        self.board = self.init_board(width, height)
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
        for i in range(len(self.board)):
            temp_str = ''
            for j in range(len(self.board[0])):
                temp_str += f"{(str(self.board[i][j]))} "
            print(temp_str)

    
    def create_upper_gate(self):
        current_index = random.randrange(3, len(self.board[0]) - 1)
        for _ in range(3):
            self.board[0][current_index] = Gate(0, current_index)
            current_index -= 1

    
    def create_bottom_gate(self):
        current_index = random.randrange(3, len(self.board[0]) - 1)
        for _ in range(3):
            self.board[-1][current_index] = Gate(len(self.board)-1, current_index)
            current_index -= 1

    
    def create_left_gate(self):
        current_index = random.randrange(3, len(self.board) - 1)
        left_side = 0
        for _ in range(3):
            self.board[current_index][left_side] = Gate(current_index, left_side)
            current_index -= 1


    def create_right_gate(self):
        current_index = random.randrange(3, len(self.board) - 1)
        right_side = -1
        for _ in range(3):
            self.board[current_index][right_side] = Gate(current_index, right_side)
            current_index -= 1


    def create_gates(self, up=True, bot=True, left=True, right=True):
        if up: self.create_upper_gate()
        if bot: self.create_bottom_gate()
        if left: self.create_left_gate()
        if right: self.create_right_gate()
room = Room(20, 30)
room.print_room()
room.create_gates(left=False, right=False)
room.print_room()