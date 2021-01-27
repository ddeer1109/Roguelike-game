from Room import Room

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






#
# board = Board(20, 30)
# board.central_room.print_room()
# board.right_room.print_room()
# board.left_room.print_room()
# board.boss_room.print_room()
