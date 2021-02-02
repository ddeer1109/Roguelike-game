from model.creatures.Creature import Creature
from model.constants import BANDIT, UPPER, BOTTOM, LEFT, RIGHT
import random

directions = [UPPER, BOTTOM, LEFT, RIGHT]
class Bandit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.icon = BANDIT
        self.attack = 2
        self.health = 20
        self.mana = 5
        self.arrows = 1
        self.direction = self.change_direction()
        self.number_of_steps = 5
        

    def attack_player(self, player):
        player.health -= self.attack

    def change_direction(self):
        self.direction = random.choice(directions)

    def update_steps(self):
        self.number_of_steps -= 1
        if self.number_of_steps == 0:
            self.number_of_steps = random.randrange(5, 15)
            self.change_direction()

    # def move(self):
    #     self.move_up()

    def melee_attack(self):
        return super().melee_attack()

    
    def range_attack(self):
        return super().range_attack()

    
    def magic_attack(self):
        return super().magic_attack()


    def get_possible_moves_list(self):
        return super().get_possible_moves_list()