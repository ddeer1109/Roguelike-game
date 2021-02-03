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
    def display_attack_info(enemy):
        
        info_line = "="*5 + repr(enemy) + "="*5
        decor_line = "=" * len(info_line)
        print(f"""
        {decor_line}
        {info_line}
        {decor_line}
        {"ATTACKED YOU".center(len(info_line), "=")}
        {decor_line}
        """)
        sleep(1.5)
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
        

    # @staticmethod
    # def print_table(table):
    #     """Prints tabular data like above.
        
    #     Args:
    #         table: list of lists - the table to print out
    #     """
    
    #     formatted_rows = UI.get_formatted_rows_list(table)
    #     example_row = formatted_rows[0]
        
    #     length_of_bot_top_border = len(example_row)
    #     border_center = "-" * length_of_bot_top_border
        
    #     top_border = f"/{border_center}\\"
    #     bottom_border = f"\\{border_center}/"
        
    #     inside_border = "".join(["-" if element != "|" else "|" for element in example_row])
        
    #     print(top_border)
    #     last_index = len(formatted_rows) - 1
    #     for current_index in range(len(formatted_rows)):
    #         print(formatted_rows[current_index])
    #         if current_index != last_index:
    #             print(inside_border)
    #     print(bottom_border)
    


    # def get_formatted_rows_list(table):
    #     ID_INDEX = 0

    #     header_record = table[ID_INDEX]
    #     columns = [[] for _ in range(len(header_record))]
    #     for record in table:
    #         for col_index ,table_element in enumerate(record):
    #             columns[col_index].append(table_element)

    #     formatted_columns = []
        
    #     for column in columns:
    #         max_length = max(map(len, column)) + 2       
    #         formatted_column = []
    #         for element in column:
    #             formatted_item = element.center(max_length)
    #             formatted_column.append(formatted_item)       
    #         formatted_columns.append(formatted_column)
    #     formatted_rows = []
        
    #     for row_index in range(len(table)): 
    #         formatted_rows.append(["|".join(element) for element in formatted_columns])

    #     return formatted_rows

    @staticmethod
    def display_melee_animation(player, enemy, damage):
        is_blocked = damage < 0         

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
            if is_blocked:
                UI.display_info("Melee attack has been blocked")
                return
            
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
            if is_blocked:
                UI.display_info("Melee attack has been blocked")
                return

            Util.clear_screen()
            print(f'<={enemy}=/-{player} ')
        print(f"Damage done: {damage}.")
        sleep(2)
    
    @staticmethod
    def display_range_animation(player, enemy, damage):
        is_blocked = damage < 0            

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

            if is_blocked:
                UI.display_info("Range attack has been blocked")
                return

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

            if is_blocked:
                UI.display_info("Range attack has been blocked")
                return

            Util.clear_screen()
            print(f' <{enemy}-     (|{player} ')
            sleep(0.25)

        print(f"Damage done: {damage}.")
        sleep(2)

    @staticmethod
    def display_magic_animation(player, enemy, damage):
        is_blocked = damage < 0      

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

            if is_blocked:
                UI.display_info("Magic attack has been blocked")
                return

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

            if is_blocked:
                UI.display_info("Magic attack has been blocked")
                return

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