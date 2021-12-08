from Player import *
from Wall import *


class GameTable:
    def __init__(self, m, n):
        self.player_one = Player(m, n, "black")
        self.player_two = Player(m, n, "white")

