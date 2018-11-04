#coding=utf-8

from MyMatrix import Matrix
from copy import deepcopy
from MatrixAlghoritms import getDet, swapRowsL

class Cramer:
    def __init__(self, a, b):
        assert isinstance(a, Matrix) and len(a) == len(b)
        self.A = deepcopy(a)
        self.B = deepcopy(b)

    def getResult(self):
        assert self.A.shape[0] == self.A.shape[1]
        n = self.A.shape[0]
        det = getDet(self.A)
        if det == 0:
            print('Determinant is zero, Cramer\'s solution is impossible')
            return
        x = Matrix([])
        for i in range(n):
            t_matr = deepcopy(self.A)
            temp = getDet(swapRowsL(t_matr, i, self.B)) / det
            x.append(temp)
        return x

    @classmethod
    def getResultStatic(self, a, b):
        res = Cramer(a, b)
        return res.getResult()