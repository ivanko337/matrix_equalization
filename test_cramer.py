#!/usr/bin/env python3
#coding=utf-8

from copy import deepcopy
from test_new_algoritm import Matrix, printMatr
from numpy.linalg import det

def changeColumn(matrix, col, cColIndex):
    matrix = deepcopy(matrix)
    col = deepcopy(col)
    if matrix.shape[0] != len(col):
        return -1
    for i in range(len(col)):
        matrix[i][cColIndex] = col[i]
    return matrix



t2 = Matrix([[1., 3., -4.], [5., -2., 3.], [3., 4., -8.]])
c2 = Matrix([-4., 43., 1.])

printMatr(changeColumn(t2, c2, 0))