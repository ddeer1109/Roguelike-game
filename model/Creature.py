class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return self.icon

    def move_up(self):
        self.x -= 1

    def move_down(self):
        self.x += 1
        
    def move_left(self):
        self.y -= 1

    def move_right(self):
        self.y += 1