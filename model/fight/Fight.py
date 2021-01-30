import random
from view.ui import UI
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
            UI.display_fight(player,enemy)

            winner = self.serve_turn(player, enemy)
            
            if winner == RUN:
                break
        
        UI.annouce_winner(winner)
        return winner


    def serve_turn(self, player, enemy):
        player_input = self.player_fight_input()
        if player_input == RUN and player.attack >= enemy.attack:
            return RUN
        self.serve_move(player_input, player, enemy)
        
        if enemy.health <= 0:
            return player
        self.serve_move(1, enemy, player)
        
        if player.health <= 0:
            return enemy


    def player_fight_input(self):
        
        player_input = UI.get_input_of_fight_menu()
        
        while player_input not in [MELEE_ATTACK, RUN]:
            UI.print_incorrect_info()
            player_input = UI.get_input_of_fight_menu()
        return player_input



    def serve_move(self, move, player, enemy):
        if move == MELEE_ATTACK:
            dice_roll = random.randint(0,4)

            damage = dice_roll * player.attack
            enemy.health -= damage
            UI.display_melee_animation(player, enemy, damage)

        #TODO (?)    
        elif move == RANGE_ATTACK:
            pass
        
        elif move == MAGIC_ATTACK:
            pass
     
