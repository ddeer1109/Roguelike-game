
from model.board_objects.Empty_space import Empty_space
from model.creatures.Creature import Creature
from model.constants import UPPER, BOTTOM
import random
from model.items import Arrow, Food, Mana_potion

class BossPart(Creature):
    def __init__(self, x, y, icon):
        super().__init__(x, y)
        self.attack = 8
        self.defence = 10
        self.health = 70
        self.direction = UPPER
        self.icon = icon
        self.dropping_items = [Arrow.Arrow, Food.Food, Mana_potion.ManaPotion]

    def __repr__(self):
        return "THE GREAT AXEMAN"

        
    
    def get_possible_moves_list(self):
        return super().get_possible_moves_list()
        

    def drop_item(self, room):
        for boss_part in room.enemy_creatures[:5]:
            room.fields[boss_part.x][boss_part.y] = random.choice(self.dropping_items)(boss_part.x, boss_part.y)
        del room.enemy_creatures[:5]

       
