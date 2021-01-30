import random
from time import sleep
MELEE_ATTACK = 1
RANGE_ATTACK = 2
MAGIC_ATTACK = 3
RUN = 4


class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


    def start_fight(self):
        player = self.player
        enemy = self.enemy
        
        while self.player.health > 0 and self.enemy.health > 0:
            print(f'_{player}_____{enemy}_')
            print(f"Player health: {self.player.health}\nEnemy health: {self.enemy.health}")
            
            winner = self.serve_turn(player, enemy)
            if winner == RUN:
                break
        
        return winner


    def serve_turn(self, player, enemy):
        player_input = self.player_fight_input()
        if player_input == RUN and player.attack >= enemy.attack:
            return RUN
        self.serve_move(player_input, player, enemy)
        input("press enter to continue")
        
        if enemy.health <= 0:
            return player
        self.serve_move(1, enemy, player)
        
        if player.health <= 0:
            return enemy
        input("press enter to continue")


    def player_fight_input(self):
        print("Choose option: 1. Melee attack 4. Run (only if your attack is higher)")
        player_input = int(input("Choose one of options: "))
        
        while player_input not in [MELEE_ATTACK, RUN]:
            print("Incorrect input. ")
            player_input = int(input("Choose one of options: "))
        return player_input



    def serve_move(self, move, player, enemy):
        if move == MELEE_ATTACK:
            dice_roll = random.randint(0,6)

            if dice_roll == 0:
                print("You missed")
                return "missed"
            damage = dice_roll * player.attack
            enemy.health -= damage
            print(f"Damage done: {damage}.")
            print(f'_{player}>   {enemy}_')
            sleep(0.5)
            print(f'_{player}->  {enemy}_')
            sleep(0.5)
            print(f'_{player}--> {enemy}_')
            sleep(0.5)
            print(f'_{player}--->{enemy}_')
            sleep(0.5)
        elif move == RANGE_ATTACK:
            pass
        elif move == MAGIC_ATTACK:
            pass
        
    # def get_enemy_attack(enemy, player):
    #     dice_roll = random.randint(0,6)

    #     if dice_roll == 0:
    #         print("Enemy missed")
    #         return
    #     damage = dice_roll * enemy.attack
    #     player.health -= damage
    #     print(f"Enemy's done {damage} damage")
