class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def print_fight(self):
        print(self.player)
        print(self.enemy)
        print('___________________________')
        input('...')