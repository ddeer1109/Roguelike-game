from view.util import Util
from time import sleep
from model.creatures import Bandit, Player

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
        print(f"Health: {player.health}    Arrows: {player.arrows}    Mana: {player.mana}", end="\t")
        print('')


    @staticmethod
    def display_fight(player, enemy):
        Util.clear_screen()
        print(f'  {player}       {enemy}  ')
        print()
        print("*** FIGHT ***\n")
        print(f"PLAYER Health: {player.health}    Arrows: {player.arrows}    Mana: {player.mana}\
            \nENEMY Health: {enemy.health}     Arrows: {enemy.arrows}   Mana: {enemy.mana}")
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
    def display_melee_animation(player, enemy, damage):
        if damage == 0:
            UI.display_info("Melee attack has missed.")
            return None
        elif type(player) is Player.Player:
            Util.clear_screen()
            print(f'  {player}-/==>  {enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'   {player}-/==> {enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'    {player}-/==>{enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'      {player}-/={enemy}=>')

            
        elif type(player) is Bandit.Bandit:
            Util.clear_screen()
            print(f'  {enemy}  <==/-{player}  ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {enemy} <==/-{player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {enemy}<==/-{player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'<={enemy}=/-{player} ')
        print(f"Damage done: {damage}.")
        sleep(2)
    
    @staticmethod
    def display_range_animation(player, enemy, damage):
        if damage == 0:
            UI.display_info("Range attack missed or no ammunition.")
        elif type(player) is Player.Player:
            Util.clear_screen()
            print(f'  {player}|)->     {enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {player}|) -->   {enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {player}|)    -->{enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {player}|)      -{enemy}> ')
            sleep(0.25)
        elif type(player) is Bandit.Bandit:
            Util.clear_screen()
            print(f'  {enemy}     <-(|{player}')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {enemy}   <-- (|{player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {enemy}<--    (|{player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f' <{enemy}-     (|{player} ')
            sleep(0.25)

        print(f"Damage done: {damage}.")
        sleep(2)

    @staticmethod
    def display_magic_animation(player, enemy, damage):
        if damage == 0:
            UI.display_info("No enough mana for magic attack.")
            return None
        elif type(player) is Player.Player:
            Util.clear_screen()
            print(f'  {player}~o      {enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {player}    ~o  {enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {player}      ~o{enemy} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {player}        {enemy}~o')
            sleep(0.25)
        elif type(player) is Bandit.Bandit:
            Util.clear_screen()
            print(f'  {enemy}      o~{player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {enemy}   o~   {player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'  {enemy}o~      {player} ')
            sleep(0.25)

            Util.clear_screen()
            print(f'o~{enemy}        {player}  ')
            sleep(0.25)

        print(f"Damage done: {damage}.")
        sleep(2)


    @staticmethod
    def get_input_of_fight_menu():
        print()
        print("Choose option: 1. Melee attack 2. Range attack\n3. Magic attack 4. Run (only if your attack is higher)")
        try:
            return int(input("Choose one of options: "))
        except:
            return None
    

    @staticmethod
    def display_info(string, clear_screen=True):
        if clear_screen: Util.clear_screen()
        print(string)
        sleep(1)