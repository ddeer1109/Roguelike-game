from model.creatures.Creature import Creature
from model.constants import BOSS_ICON
from model.constants import RIGHT, LEFT, UPPER, BOTTOM
class Boss(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = BOSS_ICON
        self.direction = UPPER
        self.parts = []

    def create_boss_parts(self):
        x = self.x
        y = self.y

        for row in range(5):
            x += 1
            for col in range(5):
                y += 1
                temp_boss = Boss(x, y)
                self.parts.append(temp_boss)
            y = 10
    
    def move_up(self):
        for part in self.parts:
            super().move_up()