#coding=utf-8

from MyMatrix import Matrix
from copy import deepcopy
from MatrixAlghoritms import toTriangleShape, addColumn, getCol

class Gauss:
    def __init__(self, a, b):
        assert isinstance(a, Matrix) and len(a) == len(b)
        self.A = deepcopy(a)
        self.B = deepcopy(b)

    def getResult(self):
        pass