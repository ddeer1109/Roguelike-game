from view.util import Util
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