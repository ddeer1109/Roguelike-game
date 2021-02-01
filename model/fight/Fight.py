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

    def service_fight(self):
        winner = self.start_fight()
        if winner == self.player:
            
            return "victory"
        
        elif winner == self.enemy:
            
            UI.display_info("=========== YOU DIED ==========")
            UI.display_info("========== GAME OVER =========")
            
            return "defeat"
        
        else:
            
            return "run"


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
        
        
        self.serve_move(random.choice([RANGE_ATTACK]), enemy, player)
        
        if player.health <= 0:
            return enemy


    def player_fight_input(self):
        
        player_input = UI.get_input_of_fight_menu()
        
        while player_input not in [MELEE_ATTACK, RANGE_ATTACK, MAGIC_ATTACK, RUN]:
            UI.print_incorrect_info()
            player_input = UI.get_input_of_fight_menu()
        return player_input


    def serve_move(self, move, player, enemy):
        if move == MELEE_ATTACK:
            dice_roll = random.randint(0,4)
            damage = dice_roll * player.attack
            UI.display_melee_animation(player, enemy, damage)

        #TODO (?)    
        elif move == RANGE_ATTACK:
            dice_roll = random.choice([7,7,8])
            damage = dice_roll * player.attack
            UI.display_range_animation(player, enemy, damage)
            
        
        elif move == MAGIC_ATTACK:
            if player.mana >= 5:
                dice_roll = 10
                damage = dice_roll * player.attack
                player.mana -= 5
                UI.display_magic_animation(player, enemy, damage)
            else:
                UI.display_info("No mana for magic attack.")

                return

        else:
            UI.display_info("Incorrect input", clear_screen=False)

        
        enemy.health -= damage
     
