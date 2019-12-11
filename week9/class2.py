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
        summ = Matrix()
        for i in range(self):
            summ[0][i] = self[0][i] + other[0][i]
        return summ

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
