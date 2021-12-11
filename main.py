from importlib import reload

from GameTable import *


class Main:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.player_one = Player(self.m, self.n, "black")
        self.player_two = Player(self.m, self.n, "white")
        self.table = GameTable(self.m, self.n, self.player_one, self.player_two)

    def starting_state(self):
        m = int(input("Enter the number of rows: "))
        n = int(input("Enter the number of columns: "))
        self.table = GameTable(m, n)

    def show_table(self):
        self.table.print()

    def make_move(self):
        print("Move")

    def main(self):
        self.starting_state()
        while self.is_it_end():
            self.show_table()
            input()
            # ocictiti konzolu nekako

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
