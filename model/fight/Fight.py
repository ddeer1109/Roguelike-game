from view.ui import UI
from model.constants import MELEE_ATTACK, RANGE_ATTACK, MAGIC_ATTACK, RUN


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
                return
        
        UI.annouce_winner(winner)
        return winner

    @classmethod
    def serve_turn(cls, player, enemy):
        player_input = cls.player_fight_input()
        
        if player_input == RUN and player.attack >= enemy.attack:
            return RUN
        
        cls.serve_move(player_input, player, enemy)
        
        if enemy.health <= 0:
            return player
        

        enemy_move = enemy.get_random_possible_move()
        cls.serve_move(enemy_move, enemy, player)
        
        if player.health <= 0:
            return enemy

    @staticmethod
    def player_fight_input():
        
        player_input = UI.get_input_of_fight_menu()
        
        while player_input not in [MELEE_ATTACK, RANGE_ATTACK, MAGIC_ATTACK, RUN]:
            UI.display_info("Incorrect input", clear_screen=False)
            player_input = UI.get_input_of_fight_menu()
        return player_input


    @staticmethod
    def serve_move(move, player, enemy):
        if move == MELEE_ATTACK:
            damage = player.melee_attack()
            UI.display_melee_animation(player, enemy, damage)

        elif move == RANGE_ATTACK:
            damage = player.range_attack()
            UI.display_range_animation(player, enemy, damage)
            
        elif move == MAGIC_ATTACK:
            damage = player.magic_attack()
            UI.display_magic_animation(player, enemy, damage)

        enemy.health -= damage
     
