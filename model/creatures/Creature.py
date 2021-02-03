from model.board_objects.Empty_space import Empty_space
from model.constants import MELEE_ATTACK, RANGE_ATTACK, MAGIC_ATTACK, UPPER, BOTTOM, LEFT, RIGHT
import random
from model.items import Arrow, Food 
# import abc

# @abc.ABC
class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 50
        self.mana = 0
        self.arrows = 0
        
        self.attack = None
        self.defence = None
        
        self.direction = None
        self.isChasing = False

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

        elif direction == BOTTOM:
            modified_x, modified_y = self.x + 1, self.y

        elif direction == LEFT:
            modified_x, modified_y = self.x, self.y - 1

        elif direction == RIGHT:
            modified_x, modified_y = self.x, self.y + 1

        return modified_x, modified_y

    def get_defence_dice_roll(self):
        return random.randint(0, 4)

    def chase_creature(self, creature_object, room, distance=3):
        x,y = self.x, self.y
        if abs(x - creature_object.x) <= distance and abs(y - creature_object.y) <= distance: 
            if self.x > creature_object.x:
                if self.x > 1:
                    self.direction = UPPER
                    self.x-1
            elif self.x < creature_object.x:
                if self.x < len(room.fields) - 1:
                    self.direction = BOTTOM
                    x = self.x+1
            if self.y > creature_object.y:
                if self.y > 1:
                    self.direction = LEFT
                    y = self.y-1
            elif self.y < creature_object.y:
                if self.y < len(room.fields[0]) - 1:
                    self.direction = RIGHT
                    y = self.y+1
            return x,y
        return self.get_data_after_key_press(self.direction)

    def get_coords_around(self):
        coords_around = [
        (self.x, self.y),
        (self.x+1, self.y), 
        (self.x, self.y+1),
        (self.x-1, self.y),
        (self.x, self.y-1),
        (self.x+1, self.y+1),
        (self.x-1, self.y-1),
        (self.x+1, self.y-1),
        (self.x-1, self.y+1)]
        return coords_around

    def melee_attack(self):
        attack_dice_roll = random.randint(0,4)

        damage = attack_dice_roll * self.attack
        return damage

    def range_attack(self):
        if self.arrows > 0:
            attack_dice_roll = random.randint([0,0,0,5,6,7])
            
            damage = attack_dice_roll * self.attack
            self.arrows -= 1
            return damage
        else:
            return 0

    def magic_attack(self):
        if self.mana >= 5:
            attack_dice_roll = 8
    
            damage = attack_dice_roll * self.attack
            self.mana -= 5
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

    def drop_item(self, room):
        item = random.choice([Arrow.Arrow, Food.Food])
        del room.bandits[room.bandits.index(self)]
        room.fields[self.x][self.y] = item(self.x, self.y)
        