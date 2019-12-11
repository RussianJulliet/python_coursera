from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        string = ""
        for i in self.matrix:
            for j in i:
                string = string + '%s\t' % j
            string = string[:-1] + '\n'
        return string[:-1]

    def size(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        # for row in self.matrix:
        #    if len(row) > cols:
        #        cols = len(row)

        return (rows, cols)

    def __add__(self, other):
        summ = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summ[i][j] += other.matrix[i][j]
                # print(other[i][j])
        return summ

    def __mul__(self, c):
        mul = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                mul[i][j] = mul[i][j] * c
                # print(other[i][j])
        return mul

    __rmul__ = __mul__


exec(stdin.read())
