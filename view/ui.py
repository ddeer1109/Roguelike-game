class UI:
    @staticmethod
    def display_room(room):
        '''
        Displays complete game board on the screen

        Returns:
        Nothing
        '''
        # clear_screen()
        for i in range(len(room.fields)):
            temp_str = ''
            for j in range(len(room.fields[0])):
                temp_str += str(room.fields[i][j])
            print(temp_str)