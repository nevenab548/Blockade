from importlib import reload

import re
from GameTable import *
from Player import *


class Main:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.player_one = Player(self.m, self.n, "black")
        self.player_two = Player(self.m, self.n, "white")
        self.table = GameTable(self.m, self.n, self.player_one, self.player_two)

    def starting_state(self):
        self.m = int(input("Enter the number of rows: "))
        self.n = int(input("Enter the number of columns: "))
        self.player_one = Player(self.m, self.n, "black")
        self.player_two = Player(self.m, self.n, "white")
        self.table = GameTable(self.m, self.n, self.player_one, self.player_two)

    def show_table(self):
        self.table.print()

    def make_move(self):
        move = ""
        while self.is_move_valid(move) is False:
            move = input("Enter a move: ")
        self.table.make_move(move);

    def is_move_valid(self, move):
        reg = re.compile('\[[XO] [12]] \[\d \d] \[[BG] \d \d]')
        no_wall_reg = re.compile('\[[XO] [12]] \[\d \d]')
        return True if reg.match(move) or no_wall_reg.match(move) is not None else False

    def main(self):
        self.starting_state()
        while self.is_it_end():
            self.show_table()
            self.make_move()
            # ocictiti konzolu

    def is_it_end(self):
        if self.player_one.pawn_one_position == [7, 3] or self.player_one.pawn_one_position == [7, 10]:
            return False
        if self.player_one.pawn_two_position == [7, 3] or self.player_one.pawn_two_position == [7, 10]:
            return False
        if self.player_two.pawn_one_position == [3, 3] or self.player_two.pawn_one_position == [3, 10]:
            return False
        if self.player_two.pawn_two_position == [3, 3] or self.player_two.pawn_two_position == [3, 10]:
            return False
        return True


game = Main()
game.main()
