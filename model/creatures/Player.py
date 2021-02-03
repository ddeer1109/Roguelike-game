from model.creatures.Creature import Creature
from model.constants import PLAYER, CENTRAL
from model.items import Key, Food, Arrow

class Player(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "Hero"
        self.icon = PLAYER
        self.inventory = []
        self.attack = 3
        self.defence = 3
        self.mana = 10
        self.killed_enemies = 0
        self.collected_food = 0


    def eat_food(self, food):
        self.health += food.health_increase

    def pick_key(self, key):
        self.inventory.append(key)

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

    def melee_attack(self):
        return super().melee_attack()

    
    def range_attack(self):
        return super().range_attack()


    def magic_attack(self):
        return super().magic_attack()