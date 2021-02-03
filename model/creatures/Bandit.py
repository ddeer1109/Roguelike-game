from model.creatures.Creature import Creature
from model.constants import BANDIT, MELEE_ATTACK, UPPER, BOTTOM, LEFT, RIGHT
from model.items.Food import Food
import random

directions = [UPPER, BOTTOM, LEFT, RIGHT]
class Bandit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = BANDIT
        self.attack = super().get_random_stat(2,4)
        self.defence = super().get_random_stat(2,5)
        self.health = super().get_random_stat(25,35)
        self.mana = 0
        self.arrows = 0
        self.direction = self.get_start_direction()
        self.number_of_steps = 5
        self.dropping_items = [Food]
        
    def __repr__(self) -> str:
        return "Bandit"

        
    def attack_player(self, player):
        player.health -= self.attack

    def change_direction(self):
        direction = random.choice(list(set(directions) - set(self.direction)))
        return direction

    def update_steps(self):
        self.number_of_steps -= 1
        if self.number_of_steps == 0:
            self.number_of_steps = random.randrange(4, 8)
            self.direction = self.change_direction()

    def get_start_direction(self):
        return random.choice(directions)
    

    def melee_attack(self):
        return super().melee_attack()

    
    # def range_attack(self):
    #     return super().range_attack()

    
    # def magic_attack(self):
    #     return super().magic_attack()


    def get_possible_moves_list(self):
        return MELEE_ATTACK

    def drop_item(self, room):
        item = random.choice(self.dropping_items)
        del room.bandits[room.bandits.index(self)]
        room.fields[self.x][self.y] = item(self.x, self.y)