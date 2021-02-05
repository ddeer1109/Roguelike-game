from model.creatures.Creature import Creature
from model.constants import PLAYER, CENTRAL
from model.items import Key, Food, Arrow
from view.ui import UI
class Player(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Hero"
        self.icon = PLAYER
        self.inventory = []
        self.attack = 20
        self.defence = 5
        self.mana = 50
        self.killed_enemies = 0
        self.collected_items = 0

    def get_statistics(self):
        return {
            'name': self.name,
            'attack': str(self.attack),
            'defence': str(self.defence),
            'mana': str(self.mana),
            'killed_enemies': str(self.killed_enemies),
            'collected_items': str(self.collected_items),
            
        }

    def eat_food(self, food):
        self.health += food.health_increase


    def pick_key(self, key):
        self.inventory.append(key)


    def pick_mana_potion(self, potion):
        self.mana += potion.mana_increase


    def pick_arrow(self, arrow):
        self.arrows += arrow.count


    def get_coords_around(self):
        return super().get_coords_around()

    def service_picking_item(self, item):
        if type(item) is Key.Key:
            self.pick_key(item)
        elif type(item) is Food.Food:
            self.eat_food(item)
        elif type(item) is Arrow.Arrow:
            self.pick_arrow(item)
        else:
            self.pick_mana_potion(item)
        self.collected_items += 1
        
        UI.display_decor_info(item, "WAS PICKED.")

    def melee_attack(self):
        return super().melee_attack()

    
    def range_attack(self):
        return super().range_attack()


    def magic_attack(self):
        return super().magic_attack()