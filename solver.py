#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

class SudokoSolver():
    def __init__(self):
        self.verbose = False
        self.grid = np.zeros(shape=(9,9))
        self.setGrid()

    def setGrid(self):
        self.grid[0][8] = 8
        self.grid[1][0] = 1
        self.grid[1][1] = 8
        self.grid[1][5] = 2
        self.grid[1][6] = 3
        self.grid[2][1] = 6
        self.grid[2][4] = 5
        self.grid[2][5] = 7
        self.grid[2][8] = 1
        self.grid[3][1] = 7
        self.grid[3][3] = 9
        self.grid[3][4] = 6
        self.grid[4][1] = 9
        self.grid[4][3] = 7
        self.grid[4][5] = 4
        self.grid[4][7] = 1
        self.grid[5][4] = 8
        self.grid[5][5] = 1
        self.grid[5][7] = 4
        self.grid[6][0] = 6
        self.grid[6][3] = 2
        self.grid[6][4] = 4
        self.grid[6][7] = 8
        self.grid[7][2] = 4
        self.grid[7][3] = 5
        self.grid[7][7] = 9
        self.grid[7][8] = 3
        self.grid[8][0] = 5
        print(np.matrix(self.grid))

    def printTheGrid(self):
        print(np.matrix(self.grid))

    def check(self, y, x, n):
        for k in range(0, 9):
            if self.grid[y][k] == n:
                return False
        for k in range(0, 9):
            if self.grid[k][x] == n:
                return False
        x0 = (x//3) * 3
        y0 = (y//3) * 3
        for k in range(0,3):
            for l in range(0,3):
                if self.grid[y0 + k][x0 + l] == n:
                    return False
        return True

    def findSolution(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    for n in range(1, 10):
                        if self.check(i, j, n):
                            if self.verbose:
                                print("{} {} - {}".format(i, j, n))
                            self.grid[i][j] = n
                            self.findSolution()
                            self.grid[i][j] = 0
                    return
        self.printTheGrid()
        input("More")

if __name__ == "__main__":
    ss = SudokoSolver()
    ss.findSolution()
