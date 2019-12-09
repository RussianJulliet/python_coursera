from sys import stdin
from copy import deepcopy

class Matrix():
    def __init___(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        string = ""
        for i in self.matrix:
            for j in i:
                string = string + '%s\t' % j
            string = string[:-1] + '\n'
        return string[:-1]

    @property
    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)

        return (rows, cols)

#exec(stdin.read())


m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)
