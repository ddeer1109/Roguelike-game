class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.icon = None

    def __str__(self):
        return self.icon

    def get_coords_around(self):
        coords_around = [
        (self.x, self.y),
        (self.x+1, self.y), 
        (self.x, self.y+1),
        (self.x-1, self.y),
        (self.x, self.y-1),
        (self.x+1, self.y+1),
        (self.x-1, self.y-1),
        (self.x+1, self.y-1),
        (self.x-1, self.y+1)]
        return coords_around
