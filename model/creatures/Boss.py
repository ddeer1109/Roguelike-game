from model.creatures.Creature import Creature
from model.creatures.BossPart import BossPart
from model.constants import BOSS_ICON_TOP, BOSS_ICON_SIDE, BOSS_ICON_INNER
from model.constants import RIGHT, LEFT, UPPER, BOTTOM

class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parts = self.create_boss_parts()

    def create_boss_parts(self):
        temp_list = []

        
        x = self.x - 3
        y = self.y - 3
        for row_time in range(5):
            x += 1
            for col_time in range(5):
                y +=1
                if row_time in [0, 4]:
                    icon = BOSS_ICON_TOP
                elif col_time in [0, 4]:
                    icon = BOSS_ICON_SIDE
                else:
                    icon = BOSS_ICON_INNER

                boss_part = BossPart(x, y, icon) 
                temp_list.append(boss_part)
            y = self.y - 3
        return temp_list
    
    # def move_up(self):
    # # for part in self.parts:
    #     super().move_up()