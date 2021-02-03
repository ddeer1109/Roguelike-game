from model.creatures.Bandit import Bandit
from model.constants import ARCHER

class ArcherBandit(Bandit):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.arrows = 10
        self.icon = ARCHER

    def __repr__(self) -> str:
        return "Archer Bandit"

    def range_attack(self):
        return super().range_attack()