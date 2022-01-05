from importlib import reload

import re
from GameTable import *
from Graph import *
from Player import *


def array_to_bst(array_nums):
    if not array_nums:
        return None
    mid_num = len(array_nums) // 2
    node = {'value': array_nums[mid_num], 'left': [], 'right': []}
    node['left'].append(array_to_bst(array_nums[:mid_num]))
    node['right'].append(array_to_bst(array_nums[mid_num + 1:]))
    return node


# Izgenerisati za svaki moguci potez u stablu moguve poteze, tako se pravi stablo
# Hardcoded na jedan dubina, moguca izmena na dalje
def minmax_alphabeta(node, depth, alpha, beta, maximizingPlayer):  # b +inf a -inf

    if depth == 0 or (node['left'] is None and node['right'] is None):
        return node['value'][0] + node['value'][1]

    if maximizingPlayer is True:
        for child in node['left']:
            alpha = alpha if alpha > minmax_alphabeta(child, depth - 1, alpha, beta,
                                                      not maximizingPlayer) else minmax_alphabeta(child, depth - 1,
                                                                                                  alpha, beta,
                                                                                                  not maximizingPlayer)
            if beta <= alpha:
                break

        for child in node['right']:
            alpha = alpha if alpha > minmax_alphabeta(child, depth - 1, alpha, beta,
                                                      not maximizingPlayer) else minmax_alphabeta(child, depth - 1,
                                                                                                  alpha, beta,
                                                                                                  not maximizingPlayer)
            if beta <= alpha:
                break
        return alpha
    else:
        for child in node['left']:
            beta = beta if beta < minmax_alphabeta(child, depth - 1, alpha, beta,
                                                   not maximizingPlayer) else minmax_alphabeta(child, depth - 1,
                                                                                               alpha, beta,
                                                                                               not maximizingPlayer)
            if beta <= alpha:
                break
        for child in node['right']:
            beta = beta if beta < minmax_alphabeta(child, depth - 1, alpha, beta,
                                                   not maximizingPlayer) else minmax_alphabeta(child, depth - 1,
                                                                                               alpha, beta,
                                                                                               not maximizingPlayer)
            if beta <= alpha:
                break
        return beta


def is_okay_position(player_pos, move_pos):
    if player_pos == move_pos:
        print("Ne moze stajati u mestu")
        return False
    if player_pos[0] + 1 == move_pos[0] and player_pos[1] == move_pos[1]:
        return True
    if player_pos[0] + 2 == move_pos[0] and player_pos[1] == move_pos[1]:
        return True
    if player_pos[0] + 1 == move_pos[0] and player_pos[1] - 1 == move_pos[1]:
        return True
    if player_pos[0] == move_pos[0] and player_pos[1] - 1 == move_pos[1]:
        return True
    if player_pos[0] == move_pos[0] and player_pos[1] - 2 == move_pos[1]:
        return True
    if player_pos[0] - 1 == move_pos[0] and player_pos[1] - 1 == move_pos[1]:
        return True
    if player_pos[0] - 1 == move_pos[0] and player_pos[1] == move_pos[1]:
        return True
    if player_pos[0] - 2 == move_pos[0] and player_pos[1] == move_pos[1]:
        return True
    if player_pos[0] - 1 == move_pos[0] and player_pos[1] + 1 == move_pos[1]:
        return True
    if player_pos[0] == move_pos[0] and player_pos[1] + 1 == move_pos[1]:
        return True
    if player_pos[0] == move_pos[0] and player_pos[1] + 2 == move_pos[1]:
        return True
    if player_pos[0] + 1 == move_pos[0] and player_pos[1] + 1 == move_pos[1]:
        return True
    print("Izdata pogresna pozicija za kretanje")
    return False


class Main:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.player_one = Player(self.m, self.n, "black")
        self.player_two = Player(self.m, self.n, "white")
        self.table = GameTable(self.m, self.n, self.player_one, self.player_two)
        self.graph = Graph(self.table)
        self.possible_moves_one = []
        self.possible_moves_two = []

    def starting_state(self):
        self.m = int(input("Enter the number of rows: "))
        self.n = int(input("Enter the number of columns: "))
        self.player_one = Player(self.m, self.n, "black")
        self.player_two = Player(self.m, self.n, "white")
        self.table = GameTable(self.m, self.n, self.player_one, self.player_two)
        self.graph = Graph(self.table)

    def show_table(self):
        self.table.print()

    def make_move(self):
        move = ""
        while self.is_move_valid(move) is False or self.is_move_legal(move) is False:
            move = input("Enter a move: ")
        self.table.make_move(move)
        self.graph = Graph(self.table)

    def is_move_valid(self, move):
        reg = re.compile('\[[XO] [12]] \[[A-Fa-f0-9]+ [A-Fa-f0-9]+] \[[BG] \d \d]')
        no_wall_reg = re.compile('\[[XO] [12]] \[\d \d]')
        return True if reg.match(move) or no_wall_reg.match(move) is not None else False

    def is_move_legal(self, move):
        if move == "":
            return False
        arr = list(move)
        move_cor = [int(arr[7], 16), int(arr[9], 16)]
        wall_cor = [int(arr[15], 16) - 1, int(arr[17], 16) - 1]
        if arr[1] == 'X' and self.player_one.player_turn is True:
            if arr[3] == '1':
                if is_okay_position(self.player_one.pawn_one_position, move_cor) is True and self.is_okay_wall(
                        arr[13], wall_cor) is True \
                        and self.check_if_goal_is_not_blocked(self.player_two, wall_cor, arr[13]) is True:
                    return True
            elif arr[3] == '2':
                if is_okay_position(self.player_one.pawn_two_position, move_cor) is True and self.is_okay_wall(
                        arr[13], wall_cor) is True \
                        and self.check_if_goal_is_not_blocked(self.player_two, wall_cor, arr[13]) is True:
                    return True
        elif arr[1] == 'O' and self.player_two.player_turn is True:
            if arr[3] == '1':
                if is_okay_position(self.player_two.pawn_one_position, move_cor) is True and self.is_okay_wall(
                        arr[13], wall_cor) is True \
                        and self.check_if_goal_is_not_blocked(self.player_one, wall_cor, arr[13]) is True:
                    return True
            elif arr[3] == '2':
                if is_okay_position(self.player_two.pawn_two_position, move_cor) is True and self.is_okay_wall(
                        arr[13], wall_cor) is True \
                        and self.check_if_goal_is_not_blocked(self.player_one, wall_cor, arr[13]) is True:
                    return True
        print("Izdat nelegalan potez")
        return False

    def check_if_goal_is_not_blocked(self, player, wall, wall_color):
        # privremeni zid
        is_valid = False
        if wall_color == 'B':
            self.table.matrix[int(wall[0])][int(wall[1])].set_lower_wall(1)
            self.table.matrix[int(wall[0])][int(wall[1]) + 1].set_lower_wall(1)
            self.table.matrix[int(wall[0]) + 1][int(wall[1])].set_upper_wall(1)
            self.table.matrix[int(wall[0]) + 1][int(wall[1]) + 1].set_upper_wall(1)
        else:
            self.table.matrix[int(wall[0])][int(wall[1])].set_right_wall(1)
            self.table.matrix[int(wall[0]) + 1][int(wall[1])].set_right_wall(1)
            self.table.matrix[int(wall[0])][int(wall[1]) + 1].set_left_wall(1)
            self.table.matrix[int(wall[0]) + 1][int(wall[1])].set_left_wall(1)
        self.graph = Graph(self.table)
        if player.player_color == "black":
            if (self.graph.is_there_path([player.pawn_one_position[0] - 1, player.pawn_one_position[1] - 1],
                                         [7, 3]) is True and self.graph.is_there_path(
                [player.pawn_two_position[0] - 1, player.pawn_two_position[1] - 1], [7, 3]) is True) and \
                    (self.graph.is_there_path([player.pawn_one_position[0] - 1, player.pawn_one_position[1] - 1],
                                              [7, 10]) is True and self.graph.is_there_path(
                        [player.pawn_two_position[0] - 1, player.pawn_two_position[1] - 1], [7, 10]) is True):
                is_valid = True
        else:
            if (self.graph.is_there_path([player.pawn_one_position[0] - 1, player.pawn_one_position[1] - 1],
                                         [3, 3]) is True and self.graph.is_there_path(
                [player.pawn_two_position[0] - 1, player.pawn_two_position[1] - 1], [3, 3]) is True) and \
                    (self.graph.is_there_path([player.pawn_one_position[0] - 1, player.pawn_one_position[1] - 1],
                                              [3, 10]) is True and self.graph.is_there_path(
                        [player.pawn_two_position[0] - 1, player.pawn_two_position[1] - 1], [3, 10]) is True):
                is_valid = True
        # ponistavanje zida
        if wall_color == 'B':
            self.table.matrix[int(wall[0])][int(wall[1])].set_lower_wall(0)
            self.table.matrix[int(wall[0])][int(wall[1]) + 1].set_lower_wall(0)
            self.table.matrix[int(wall[0]) + 1][int(wall[1])].set_upper_wall(0)
            self.table.matrix[int(wall[0]) + 1][int(wall[1]) + 1].set_upper_wall(0)
        else:
            self.table.matrix[int(wall[0])][int(wall[1])].set_right_wall(0)
            self.table.matrix[int(wall[0]) + 1][int(wall[1])].set_right_wall(0)
            self.table.matrix[int(wall[0])][int(wall[1]) + 1].set_left_wall(0)
            self.table.matrix[int(wall[0]) + 1][int(wall[1])].set_left_wall(0)
        self.graph = Graph(self.table)
        return is_valid

    def is_okay_wall(self, wall_color, wall_pos):
        if wall_color == "B":
            if wall_pos[1] == self.table.n - 1:
                return False
            if self.table.matrix[wall_pos[0]][wall_pos[1]].get_lower_wall() == 1 or \
                    self.table.matrix[wall_pos[0]][wall_pos[1] + 1].get_lower_wall() == 1:
                return False
        else:
            if wall_pos[0] == self.table.m - 1:
                return False
            if self.table.matrix[wall_pos[0]][wall_pos[1]].get_right_wall() == 1 or \
                    self.table.matrix[wall_pos[0] + 1][wall_pos[1]].get_right_wall() == 1:
                return False
        return True

    def main(self):
        self.starting_state()
        while self.is_it_end():
            self.show_table()
            self.make_move()
            self.player_one.player_turn = not self.player_one.player_turn
            self.player_two.player_turn = not self.player_two.player_turn
            if self.player_two.player_turn is True:
                if self.possible_moves(self.player_two) > 0:
                    self.table.make_move(f'[O 1] [{self.possible_moves_one[0][0]} {self.possible_moves_one[0][1]}]')
                else:
                    self.table.make_move(f'[O 2] [{self.possible_moves_two[0][0]} {self.possible_moves_two[0][1]}]')
                self.player_one.player_turn = not self.player_one.player_turn
                self.player_two.player_turn = not self.player_two.player_turn


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

    def possible_moves(self, player):
        self.possible_moves_one = self.graph.find_paths(
            [player.pawn_one_position[0] - 1, player.pawn_one_position[1] - 1], 1)
        self.possible_moves_two = self.graph.find_paths(
            [player.pawn_two_position[0] - 1, player.pawn_two_position[1] - 1], 1)
        return (minmax_alphabeta(array_to_bst(self.possible_moves_one), 2, -1000, 1000, True))-minmax_alphabeta(array_to_bst(self.possible_moves_two), 2, -1000, 1000, True)


game = Main()
game.main()
