from model.creatures.Archer_bandit import ArcherBandit
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
        print("\n")
        for i in range(len(room.fields)):
            temp_str = ''
            for j in range(len(room.fields[0])):
                temp_str += str(room.fields[i][j])
            print("\t\t"+temp_str)
    @staticmethod
    def display_statistics(player):
        print(f"Inventory: {player.inventory}", end = "\t")
        print(f"Health: {player.health}    Arrows: {player.arrows}    Mana: {player.mana}", end="\t")
        print('')
    def add_new_line(times=3):
        print(times*"\n", end="")


    @staticmethod
    def display_decor_info(object, info):
        
        info_line = "="*5 + repr(object) + "="*5
        decor_line = "=" * len(info_line)
        print(f"""
                {decor_line}
                {info_line}
                {decor_line}
                {info.center(len(info_line), "=")}
                {decor_line}
        """)
        sleep(0.5)
    @staticmethod


    def display_fight(player, enemy):
        Util.clear_screen()
        UI.add_new_line(2)
        print(f'\t\t\t  {player}        {enemy.fight_repr()}  ')
        print()
        print("\t\t\t*** FIGHT ***\n")
        print(f"\tPLAYER Health: {player.health}    Arrows: {player.arrows}    Mana: {player.mana}\
            \n\tENEMY Health: {enemy.health}     Arrows: {enemy.arrows}   Mana: {enemy.mana}")
        print()


    
    
    @staticmethod
    def display_fight_statistics():
        pass
        
    @staticmethod
    def annouce_winner(winner):
        UI.add_new_line()
        if type(winner) is Player.Player:
            UI.display_decor_info("Winner is", "Player")
        elif isinstance(winner, (Bandit.Bandit)):
            UI.display_decor_info("You've got", "DEFEATED")
        else:
            print("You've runned away")

        input("\nPress enter to continue...")

    @staticmethod
    def display_full_statistics(player):
        full_statistics = player.get_statistics()
        # formatted_rows = UI.get_formatted_rows_list(full_statistics)
        # UI.print_table(formatted_rows)
        Util.clear_screen()
        print("Full player statistics:\n")
        for key, value in full_statistics.items():
            print("| {:20} : {:10} |".format(key, value))
        input("\nPress enter to continue...")
        Util.clear_screen()
        

    @staticmethod
    def display_melee_animation(player, enemy, damage):
        is_blocked = damage < 0         

        if damage == 0:
            UI.display_info("Melee attack has missed.")
            return None            
        elif type(player) is Player.Player:
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}-/==>  {enemy.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t   {player.fight_repr()}-/==> {enemy.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t    {player.fight_repr()}-/==>{enemy.fight_repr()} ')
            sleep(0.25)
            if is_blocked:
                UI.display_info("Melee attack has been blocked")
                return
            
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t      {player.fight_repr()}-/={enemy.fight_repr()}=>')

            
        elif type(player) is not Player.Player:
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}  <==/-{player.fight_repr()}  ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()} <==/-{player.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}<==/-{player.fight_repr()} ')
            sleep(0.25)
            if is_blocked:
                UI.display_info("Melee attack has been blocked")
                return

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t<={enemy.fight_repr()}=/-{player.fight_repr()} ')
        print(f"Damage done: {damage}.")
        sleep(2)
    
    @staticmethod
    def display_range_animation(player, enemy, damage):
        is_blocked = damage < 0            

        if damage == 0:
            UI.display_info("Range attack missed or no ammunition.")
        elif type(player) is Player.Player:
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}|)->     {enemy.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}|) -->   {enemy.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}|)    -->{enemy.fight_repr()} ')
            sleep(0.25)

            if is_blocked:
                UI.display_info("Range attack has been blocked")
                return

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}|)      -{enemy.fight_repr()}> ')
            sleep(0.25)
        elif type(player) is not Player.Player:
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}     <-(|{player.fight_repr()}')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}   <-- (|{player.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}<--    (|{player.fight_repr()} ')
            sleep(0.25)

            if is_blocked:
                UI.display_info("Range attack has been blocked")
                return

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t <{enemy.fight_repr()}-     (|{player.fight_repr()} ')
            sleep(0.25)

        print(f"Damage done: {damage}.")
        sleep(1)

    @staticmethod
    def display_magic_animation(player, enemy, damage):
        is_blocked = damage < 0      

        if damage == 0:
            UI.display_info("No enough mana for magic attack.")
            return None
        elif type(player) is Player.Player:
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}~o      {enemy.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}   ~o   {enemy.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}      ~o{enemy.fight_repr()} ')
            sleep(0.25)

            if is_blocked:
                UI.display_info("Magic attack has been blocked")
                return

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {player.fight_repr()}        {enemy.fight_repr()}~o')
            sleep(0.25)
        elif type(player) is not Player.Player:
            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}      o~{player.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}   o~   {player.fight_repr()} ')
            sleep(0.25)

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t  {enemy.fight_repr()}o~      {player.fight_repr()} ')
            sleep(0.25)

            if is_blocked:
                UI.display_info("Magic attack has been blocked")
                return

            Util.clear_screen()
            UI.add_new_line()
            print(f'\t\t\t o~{enemy.fight_repr()}       {player.fight_repr()}  ')
            sleep(0.25)

        print(f"Damage done: {damage}.")
        sleep(1)


    @staticmethod
    def get_input_of_fight_menu():
        print()
        print("\tChoose option: 1. Melee attack 2. Range attack\n\t3. Magic attack 4. Run (only if your attack is higher)")
        try:
            return int(input("\n\tChoose one of options: "))
        except:
            return None
    

    @staticmethod
    def display_info(string, clear_screen=True, new_lines=3):
        if clear_screen: 
            Util.clear_screen()
        UI.add_new_line(new_lines)
        print(string)
        sleep(1)