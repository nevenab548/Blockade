from Wall import *


class Field:

    def __init__(self):
        self.upper_wall = 0
        self.lower_wall = 0
        self.left_wall = 0
        self.right_wall = 0
        self.value = " "

    def set_upper_wall(self, upper_wall):
        self.upper_wall = upper_wall

    def set_lower_wall(self, lower_wall):
        self.lower_wall = lower_wall

    def set_left_wall(self, left_wall):
        self.left_wall = left_wall

    def set_right_wall(self, right_wall):
        self.right_wall = right_wall

    def set_value(self, value):
        self.value = value

    def get_lower_wall(self):
        return self.lower_wall

    def print(self, j):
        if j == 0:
            print("|" if self.left_wall == 0 else "∥", end="")
        print(self.value, end="")
        print("|" if self.right_wall == 0 else "∥", end="")
