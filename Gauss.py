#coding=utf-8

from MyMatrix import Matrix
from copy import deepcopy
from MatrixAlghoritms import toTriangleShape, addColumn, getCol, printMatr, count
from collections import deque

class Gauss:
    def __init__(self, a, b):
        assert isinstance(a, Matrix) and len(a) == len(b)
        self.A = deepcopy(a)
        self.B = deepcopy(b)

    def getValues(self, matr):
        res = Matrix([])
        for i in range(len(matr))[::-1]:
            zero_zount = count(matr[i], 0.0)
            temp = []
            for j in range(zero_zount + 1, len(matr[i])):
                temp.append(matr[i][j])
            res.append(temp)
        return res

    def getResult(self):
        matr = toTriangleShape(addColumn(self.A, self.B))
        values = self.getValues(matr)
        res = deque(values[0])
        for i in range(1, len(values)):
            temp = 0.
            for j in range(1, len(values[i])):
                temp += res[j - 1] * values[i][j - 1]
            res.appendleft( values[i][-1] - temp )
        return list(res)

    @classmethod
    def getResultStatic(self, A, B):
        res = Gauss(A, B)
        return res.getResult()

if __name__ == '__main__':
    A = Matrix([ [1, 2, 3], [3, 2, 4], [2, -1, 0] ])
    B = Matrix([1, 2, -1])
    print(Gauss.getResultStatic(A, B))