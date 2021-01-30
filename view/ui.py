from view.util import Util
from time import sleep
from model.creatures import Bandit, Player, Creature

class UI:
    @staticmethod
    def display_room(room):
        '''
        Displays complete game board on the screen

        Returns:
        Nothing
        '''
        Util.clear_screen()
        for i in range(len(room.fields)):
            temp_str = ''
            for j in range(len(room.fields[0])):
                temp_str += str(room.fields[i][j])
            print(temp_str)

    @staticmethod
    def display_statistics(player):
        print(f"Inventory: {player.inventory}", end = "\t")
        print(f"Healt: {player.health}", end="\t")
        print('')


    @staticmethod
    def display_fight(player, enemy):
        Util.clear_screen()
        print(f'_{player}_____{enemy}_')
        print()
        print(f"Player health: {player.health}\nEnemy health: {enemy.health}")
        print()
        
    @staticmethod
    def annouce_winner(winner):
        if type(winner) is Player.Player:
            print("Winner is Player")
        elif isinstance(winner, (Bandit.Bandit)):
            print("You've got defeated.")
        else:
            print("You've runned away")

        input("\nPress enter to continue...")

    @staticmethod
    def print_miss_info():
        Util.clear_screen()
        print("Attack is missed.")
        sleep(2)

    @staticmethod
    def display_melee_animation(player, enemy, damage):
        if damage == 0:
            UI.print_miss_info()
            return None
        elif type(player) is Player.Player:
            Util.clear_screen()
            print(f'_{player}>   {enemy}_')
            sleep(0.25)
            Util.clear_screen()

            print(f'_{player}->  {enemy}_')
            sleep(0.25)

            Util.clear_screen()
            print(f'_{player}--> {enemy}_')
            sleep(0.25)

            Util.clear_screen()
            print(f'_{player}--->{enemy}_')
            sleep(1)
        elif type(player) is Bandit.Bandit:
            Util.clear_screen()
            print(f'_{enemy}   <{player}_')
            sleep(0.25)
            Util.clear_screen()

            print(f'_{enemy}  <-{player}_')
            sleep(0.25)

            Util.clear_screen()
            print(f'_{enemy} <--{player}_')
            sleep(0.25)

            Util.clear_screen()
            print(f'_{enemy}<---{player}_')

        print(f"Damage done: {damage}.")
        sleep(2)
    
    
    @staticmethod
    def get_input_of_fight_menu():
        print()
        print("Choose option: 1. Melee attack 4. Run (only if your attack is higher)")
        return int(input("Choose one of options: "))

    @staticmethod
    def print_incorrect_info():
        print("Incorrect input.")