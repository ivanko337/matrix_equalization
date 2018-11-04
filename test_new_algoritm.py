#!/usr/bin/env python3
#coding=utf-8

from numpy import around
from copy import deepcopy
from MyMatrix import Matrix
from MatrixAlghoritms import *

def __main__():
        A = Matrix([ [ 5, 6, 9 ], [ 3, 8, 2 ], [7, 1, 2] ])
        B = Matrix([ 452, 245, 171 ])
        X = cramerMethod(A, B)
        print(X)

if __name__ == '__main__':
        __main__() 