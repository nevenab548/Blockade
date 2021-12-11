from GameTable import *



class Main:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.table = GameTable(self.m, self.n)
        self.player_one = Player(self.m, self.n, "black")
        self.player_two = Player(self.m, self.n, "white")

    def  starting_state(self):
        m = int(input("Enter the number of rows: "))
        n = int(input("Enter the number of columns: "))
        self.table = GameTable(m, n)

    def show_table(self):
        self.table.print()

    def is_it_end(self):
        print("End")

    def make_move(self):
        print("Move")

    def main(self):
        self.starting_state()
        self.show_table()


game = Main()
game.main()
