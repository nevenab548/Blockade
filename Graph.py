from GameTable import *


def in_bounds(m, n, index_i, index_j):
    return 0 <= index_i < m and 0 <= index_j < n


class Graph:
    def __init__(self, table):
        self.table = table
        self.vertices = {}

        k = 0
        for i in range(0, self.table.m): #prepaviti dodavanje suseda
            for j in range(0, self.table.n):
                self.vertices[k] = []
                if in_bounds(self.table.m, self.table.n, i - 1, j - 1) and \
                        not (self.table.matrix[i][j].get_upper_wall() == 1
                             or self.table.matrix[i][j].get_left_wall() == 1):
                    self.vertices[k].append((i - 1) * self.table.m + j - 1)
                if in_bounds(self.table.m, self.table.n, i - 2, j) and \
                        not (self.table.matrix[i][j].get_upper_wall() == 1
                             or self.table.matrix[i - 1][j].get_upper_wall() == 1):
                    self.vertices[k].append((i - 2) * self.table.m + j)
                if in_bounds(self.table.m, self.table.n, i - 1, j) and \
                        self.table.matrix[i - 1][j].get_upper_wall() == 0:
                    self.vertices[k].append((i - 1) * self.table.m + j)
                if in_bounds(self.table.m, self.table.n, i - 1, j + 1) and \
                        not (self.table.matrix[i][j].get_upper_wall() == 1
                             or self.table.matrix[i][j].get_right_wall() == 1):
                    self.vertices[k].append((i - 1) * self.table.m + j + 1)
                if in_bounds(self.table.m, self.table.n, i, j + 1) and \
                        self.table.matrix[i][j].get_right_wall() == 0:
                    self.vertices[k].append(i * self.table.m + j + 1)
                if in_bounds(self.table.m, self.table.n, i, j + 2) and \
                        not (self.table.matrix[i][j].get_right_wall() == 1
                             or self.table.matrix[i][j + 1].get_right_wall() == 1):
                    self.vertices[k].append(i * self.table.m + j + 2)
                if in_bounds(self.table.m, self.table.n, i + 1, j + 1) and \
                        not (self.table.matrix[i][j].get_right_wall() == 1
                             or self.table.matrix[i][j].get_lower_wall() == 1):
                    self.vertices[k].append((i + 1) * self.table.m + j + 1)
                if in_bounds(self.table.m, self.table.n, i + 1, j) and \
                        self.table.matrix[i][j].get_lower_wall() == 0:
                    self.vertices[k].append((i + 1) * self.table.m + j)
                if in_bounds(self.table.m, self.table.n, i + 2, j) and \
                        not (self.table.matrix[i][j].get_lower_wall() == 1
                             or self.table.matrix[i + 1][j].get_lower_wall() == 1):
                    self.vertices[k].append((i + 2) * self.table.m + j)
                if in_bounds(self.table.m, self.table.n, i + 1, j - 1) and \
                        not (self.table.matrix[i][j].get_left_wall() == 1
                             or self.table.matrix[i][j].get_lower_wall() == 1):
                    self.vertices[k].append((i + 1) * self.table.m + j - 1)
                if in_bounds(self.table.m, self.table.n, i, j - 1) and \
                        self.table.matrix[i][j].get_left_wall() == 0:
                    self.vertices[k].append(i * self.table.m + j - 1)
                if in_bounds(self.table.m, self.table.n, i, j - 2) and \
                        not (self.table.matrix[i][j].get_left_wall() == 1
                             or self.table.matrix[i][j - 1].get_left_wall() == 1):
                    self.vertices[k].append(i * self.table.m + j - 2)
                k = k + 1

    def is_there_path(self, player_pos, goal_pos):
        goal_pos[0] = goal_pos[0] - 1
        goal_pos[1] = goal_pos[1] - 1
        start = player_pos[0] * self.table.m + player_pos[1]
        end = goal_pos[0] * self.table.m + goal_pos[1]
        if player_pos == goal_pos:
            return False
        visited = dict()
        for i in self.vertices.keys():
            visited[i] = False
        queue = [list(self.vertices.keys())[start]]
        visited[list(self.vertices.keys())[start]] = True
        while queue:
            node = queue.pop()
            for val in self.vertices[node]:
                if visited[val] is False:
                    queue.append(val)
                    visited[val] = True
        return True if visited[list(self.vertices.keys())[end]] else False

    def find_paths(self, start, length):
        paths = []
        queue = [[start[0]*self.table.m+start[1]]]

        while queue:
            curr, *queue = queue
            for n in self.vertices[curr[-1]]:
                if n not in curr and len(curr) <= length:
                    queue += [curr + [n]]
                    if length == len(curr):
                        paths += [curr + [n]]
        return paths
