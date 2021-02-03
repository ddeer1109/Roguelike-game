from view.ui import UI
from model.constants import MELEE_ATTACK, RANGE_ATTACK, MAGIC_ATTACK, RUN
from model.creatures.Player import Player


class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def service_fight(self):
        winner = self.start_fight()
        UI.annouce_winner(winner)
        if type(winner) is Player:
            self.player.killed_enemies += 1
            return "victory"
        
        elif winner == RUN:
            return "run"
        
        elif type(winner) is not Player:
            UI.display_info("=========== YOU DIED ==========")
            UI.display_info("========== GAME OVER =========")
            
            return "defeat"
        

    def start_fight(self):
        player = self.player
        enemy = self.enemy
        
        while self.player.health > 0 and self.enemy.health > 0:
            UI.display_fight(player,enemy)

            winner = self.serve_turn(player, enemy)
            
            if winner == RUN:
                return RUN

        return winner

    @classmethod
    def serve_turn(cls, player, enemy):
        player_input = cls.player_fight_input()
        
        if player_input == RUN: 
            if player.attack < enemy.attack:
                UI.display_info("Too small attack to run away!")
                player_input = MELEE_ATTACK
            else:
                return RUN
        
        cls.serve_move(player_input, player, enemy)
        
        if enemy.health <= 0:
            return player
        

        enemy_move = enemy.get_possible_moves_list()
        
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
        enemy_defence_dice_roll = enemy.get_defence_dice_roll()
        UI.display_info(f"ENEMY DEFENCE DICE ROLL: {enemy_defence_dice_roll}")
        if move == MELEE_ATTACK:
            damage = player.melee_attack()  
            if damage > 0:
                damage -= enemy_defence_dice_roll
            else:
                damage = 0
            
            UI.display_melee_animation(player, enemy, damage)

        elif move == RANGE_ATTACK:
            damage = player.range_attack()
            if damage > 0:
                damage -= enemy_defence_dice_roll
            else:
                damage = 0
            
            UI.display_range_animation(player, enemy, damage)
            
        elif move == MAGIC_ATTACK:
            damage = player.magic_attack()
            if damage > 0:
                damage -= enemy_defence_dice_roll
            else:
                damage = 0

            UI.display_magic_animation(player, enemy, damage)

        damage = 0 if damage < 0 else damage
        enemy.health -= damage
     
