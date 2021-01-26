from Empty_space import Empty_space
from Wall import Wall

class Room:
    def __init__(self, width, height):
        self.board = self.init_board(width, height)

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
                temp_str += f"{(self.board[i][j].icon)} "
            print(temp_str)

room = Room(20, 30)
room.print_room()
room2 = Room(40, 20)
room.print_room()