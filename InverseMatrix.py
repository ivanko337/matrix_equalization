#coding=utf-8

from MyMatrix import Matrix
from copy import deepcopy
from MatrixAlghoritms import getInverseMatrix, matrixProduct
from numpy import around

class InverseMatrix:
    def __init__(self, a, b):
        assert isinstance(a, Matrix) and len(a) == len(b)
        self.A = deepcopy(a)
        self.B = deepcopy(b)

    def getResult(self):
        inv_a = getInverseMatrix(self.A)
        return matrixProduct(inv_a, self.B)

    @classmethod
    def getResultStatic(self, a, b):
        res = InverseMatrix(a, b)
        return res.getResult()