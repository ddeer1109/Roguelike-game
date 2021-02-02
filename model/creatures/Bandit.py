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

    def attack_player(self, player):
        player.health -= self.attack

    def change_direction(self):
        direction = random.choice(directions)
        return direction

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