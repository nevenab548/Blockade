from Player import *
from Wall import *
from Field import *


class GameTable:

    def __init__(self, m, n, player_one, player_two):
        self.m = m
        self.n = n
        self.player_one = player_one
        self.player_two = player_two
        self.matrix = [[Field() for x in range(n)] for y in range(m)]
        # self.set_fields()

    def print(self):
        self.set_fields()
        print(" ", end="")
        for i in range(0, self.n):
            print(' {:X}'.format(i + 1), end="")
        print(" ")
        print(" ", end="")
        for i in range(0, self.n):
            print(" =", end="")
        print(" ")
        for i in range(0, self.m):
            print('{:X}'.format(i + 1), end="")
            for j in range(0, self.n):
                self.matrix[i][j].print(j)
            print('{:X}'.format(i + 1), end="")
            print(" ")
            print(" ", end="")
            for k in range(0, self.n):
                print(" =" if self.matrix[i][k].get_lower_wall() == 1 else " —", end="")
            print(" ")
        print(" ", end="")
        for i in range(0, self.n):
            print(' {:X}'.format(i + 1), end="")
        print(" ")

    def set_fields(self):
        for i in range(0, self.m):
            for j in range(0, self.n):
                if i == self.m - 1:
                    self.matrix[i][j].set_lower_wall(1)
                if j == 0:
                    self.matrix[i][j].set_left_wall(1)
                if j == self.n - 1:
                    self.matrix[i][j].set_right_wall(1)
                if (i == 3 and j == 3) or (i == 3 and j == 10):
                    self.matrix[i][j].value = "X"
                if (i == 7 and j == 3) or (i == 7 and j == 10):
                    self.matrix[i][j].value = "O"

