from Field import *


class GameTable:

    def __init__(self, m, n, player_one, player_two):
        self.m = m
        self.n = n
        self.player_one = player_one
        self.player_two = player_two
        self.matrix = [[Field() for x in range(n)] for y in range(m)]

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
                if ([i, j] == self.player_one.pawn_one_position) or ([i, j] == self.player_one.pawn_two_position):
                    self.matrix[i][j].value = "X"
                if ([i, j] == self.player_two.pawn_one_position) or ([i, j] == self.player_two.pawn_two_position):
                    self.matrix[i][j].value = "O"
                if (i == 3 and j == 3) or (i == 3 and j == 10):
                    self.matrix[i][j].value = "\033[0;30;47mX\033[0;0m"
                if (i == 7 and j == 3) or (i == 7 and j == 10):
                    self.matrix[i][j].value = "\033[0;37;40mO\033[0;0m"

    def make_move(self, move):
        arr = list(move)
        print(arr)
        if arr[1] == "X":
            if arr[3] == "1":
                self.player_one.pawn_one_position = [int(arr[7]) - 1, int(arr[9]) - 1]
                if self.player_one.available_walls == 0:
                    return
                if arr[13] == 'B':
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_lower_wall(1)
                    self.matrix[int(arr[15]) - 1][int(arr[17])].set_lower_wall(1)
                else:
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_right_wall(1)
                    self.matrix[int(arr[15])][int(arr[17]) - 1].set_right_wall(1)
            else:
                self.player_one.pawn_two_position = [int(arr[7]) - 1, int(arr[9]) - 1]
                if arr[13] == 'B':
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_lower_wall(1)
                    self.matrix[int(arr[15]) - 1][int(arr[17])].set_lower_wall(1)
                else:
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_right_wall(1)
                    self.matrix[int(arr[15])][int(arr[17]) - 1].set_right_wall(1)
            self.player_one.available_walls = self.player_one.available_walls - 1
        else:
            if arr[3] == "1":
                self.player_two.pawn_one_position = [int(arr[7]) - 1, int(arr[9]) - 1]
                if self.player_two.available_walls == 0:
                    return
                if arr[13] == 'B':
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_lower_wall(1)
                    self.matrix[int(arr[15]) - 1][int(arr[17])].set_lower_wall(1)
                else:
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_right_wall(1)
                    self.matrix[int(arr[15])][int(arr[17]) - 1].set_right_wall(1)
            else:
                self.player_two.pawn_two_position = [int(arr[7]) - 1, int(arr[9]) - 1]
                if arr[13] == 'B':
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_lower_wall(1)
                    self.matrix[int(arr[15]) - 1][int(arr[17])].set_lower_wall(1)
                else:
                    self.matrix[int(arr[15]) - 1][int(arr[17]) - 1].set_right_wall(1)
                    self.matrix[int(arr[15])][int(arr[17]) - 1].set_right_wall(1)
            self.player_two.available_walls = self.player_one.available_walls - 1
