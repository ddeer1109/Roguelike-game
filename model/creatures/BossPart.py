
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
        return "THE GREAT BOSS"


    def fight_repr(self):
        return "{======}"
        
    
    def get_possible_moves_list(self):
        return super().get_possible_moves_list()
        
    
    def service_killing_boss_part(self, room):
        new_body_part = BossPart(self.x, self.y, self.icon)
        killed_part_index = room.enemy_creatures.index(self)
        
        del room.enemy_creatures[room.enemy_creatures.index(self)]
        room.fields[self.x][self.y] = new_body_part
        
        room.enemy_creatures.insert(killed_part_index, new_body_part)
        
        if len(room.enemy_creatures) != 0:
            for _ in range(5):
                removed = room.enemy_creatures.pop(0)
                room.fields[removed.x][removed.y] = Empty_space(self.x, self.y)

    def drop_item(self, room):
        self.service_killing_boss_part(room)



       
