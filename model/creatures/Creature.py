from model.constants import MELEE_ATTACK, RANGE_ATTACK, MAGIC_ATTACK, UPPER, BOTTOM, LEFT, RIGHT
import random

class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 50
        self.mana = 0
        self.attack = None
        self.defence = None
        self.arrows = 0

    def __str__(self):
        return self.icon

    def move_up(self):
        self.x -= 1

    def move_down(self):
        self.x += 1
        
    def move_left(self):
        self.y -= 1

    def move_right(self):
        self.y += 1

    def get_data_after_key_press(self, direction):
        if direction == UPPER:
            modified_x, modified_y = self.x - 1, self.y
            direction = UPPER

        elif direction == BOTTOM:
            modified_x, modified_y = self.x + 1, self.y
            direction = BOTTOM

        elif direction == LEFT:
            modified_x, modified_y = self.x, self.y - 1
            direction = LEFT

        elif direction == RIGHT:
            modified_x, modified_y = self.x, self.y + 1
            direction = RIGHT

        return modified_x, modified_y, direction

    def melee_attack(self):
        dice_roll = random.randint(0,4)
        damage = dice_roll * self.attack
        return damage

    def range_attack(self):
        if self.arrows > 0:
            dice_roll = random.choice([0,0,0,7,8])
            damage = dice_roll * self.attack
            self.arrows -= 1
            return damage
        else:
            return 0

    def magic_attack(self):
        if self.mana >= 5:
            dice_roll = 10
            damage = dice_roll * self.attack
            return damage
        else:
            return 0

    
    def get_random_possible_move(self):
        possible_moves = [MELEE_ATTACK]
        if self.arrows > 0:
            possible_moves.append(RANGE_ATTACK)
        if self.mana >= 5:
            possible_moves.append(MAGIC_ATTACK)

        return random.choice(possible_moves)