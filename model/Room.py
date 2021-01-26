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
                else:
                    added_area = Empty_space(row, col)

                inner_board.append(added_area)
            board.append(inner_board)

        return board

room = Room(5, 10)
room.board
