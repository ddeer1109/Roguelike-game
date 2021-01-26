from constants import EMPTY_AREA_ICON

class Room:
    def __init__(self, width, height):
        self.board = []
        for row in range(height):
            self.board.append([EMPTY_AREA_ICON]*width)


room = Room(5, 10)
room.board