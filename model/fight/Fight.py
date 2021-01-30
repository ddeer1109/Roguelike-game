class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def print_fight(self):
        print("figth")

fight = Fight('player', 'enemy')
fight.print_fight()