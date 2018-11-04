#!/usr/bin/env python3
#coding=utf-8

from numpy import linalg
from numpy import around
from copy import copy
from MyMatrix import Matrix
from MatrixAlghoritms import *

def addMatrix(matrix1, matrix2):
        if len(matrix1) != len(matrix2):
                return matrix1
        for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                        matrix1[i].append(matrix2[i][j])
        return matrix1

def addColumn(matrix, col, col_is_matrix=False):
        if col_is_matrix:
                return addMatrix(matrix, col)
        if len(matrix) != len(col):
                return matrix
        for i in range(len(matrix)):
                matrix[i].append(col[i])
        return matrix

def mulL(l, n):
	return [ i * n for i in l ] #round(i * n, 2)

def getCol(matrix, col, end):
        return Matrix([i[int(col):end] for i in matrix])

def addLists(l1, l2, coefficient=1):
	l1 = mulL(l1, coefficient)
	return [ l1[i] + l2[i] for i in range(len(l1)) ] #round(l1[i] + l2[i], 2)

def addRows(matrix, row1, row2, coefficient):
	res = addLists(matrix[row1], matrix[row2], coefficient)
	return res

#for Cramer
def swapRowsL(matrix, row_ind, row_s):
        matrix = copy(matrix)
        matrix[row_ind] = row_s
        return matrix

def swapRows(matrix, row1, row2):
        if isinstance(row2, list):
                swapRowsL(matrix, row1, row2)
        if row1 == row2:
                return matrix
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
        return matrix

def findMinFirstEl(matrix):
        ind = 0
        for i in range(len(matrix)):
                if matrix[i][0] < matrix[ind][0]:
                        ind = i
        matrix = swapRows(matrix, 0, ind)
        return matrix

def getUnitMatrix(n):
        res = Matrix([])
        for i in range(n):
                tr = Matrix([])
                for j in range(n):
                        if i == j:
                                tr.append(1)
                        else:
                                tr.append(0)
                res.append(tr)
        return res

def getNumberSign(num):
        if num < 0:
                return -1
        return 1

def printMatr(matr):
        for i in matr:
                print(i)

def getArguments(l):
        res = Matrix([])
        if len(l) == 1:
                return l[0]
        for i in l:
                if i != 0:
                        res.append(i)
        return res

# herь
def getLastX(arguments):
        return arguments[-1][1] / arguments[-1][0]

def toTriangleShape(matr, col=Matrix([])):
        matr = addColumn(matr, col)
        if matr[0][0] == 0:
            matr = swapRows(matr, 0, -1)
        for i in range(len(matr)):
                for j in range(i + 1, len(matr)):
                        coefficient = matr[j][i] / matr[i][i] #round(matr[j][i] / matr[i][i], 2)
                        coefficient = -coefficient
                        matr[j] = addRows(matr, i, j, coefficient)
        for i in range(len(matr)):
                matr[i] = mulL(matr[i], 1 / matr[i][i])
        return matr

def toUnitShape(matrix, col=Matrix([]), col_is_matr=False):
        matrix = addColumn(matrix, col, col_is_matrix=col_is_matr)
        for i in range(len(matrix)):
                matrix[i] = mulL(matrix[i], 1. / matrix[i][i])
        for i in range(len(matrix)):
                for j in range(i + 1, len(matrix)):
                        coefficient = matrix[j][i] / matrix[i][i] #round(matrix[j][i] / matrix[i][i], 2)
                        coefficient = -coefficient
                        matrix[j] = addRows(matrix, i, j, coefficient)
        for i in range(len(matrix)):
                matrix[i] = mulL(matrix[i], 1 / matrix[i][i])
        for i in range(len(matrix)):
                for j in range(i):
                        coefficient = matrix[j][i] / matrix[i][i] #round(matrix[j][i] / matrix[i][i], 2)
                        coefficient = -coefficient
                        matrix[j] = addRows(matrix, i, j, coefficient)
        return matrix

def getInverseMatrix(matrix):
        if linalg.det(matrix) == 0:
                print('Матрица невырождена')
                return matrix
        n = len(matrix)
        matrix = toUnitShape(matrix, getUnitMatrix(n), col_is_matr=True)
        n = len(matrix[0])
        matrix = getCol(matrix, n / 2, n)
        return matrix

def matrixProduct(x, y):
        x_rows, x_cols = x.shape
        y_rows, y_cols = y.shape
        z = Matrix.zeros((x_rows, y_cols))
        if x_cols != y_rows:
                return None
        for i in range(x_rows):
                for j in range(x_cols):
                        for k in range(y_cols):
                                if (not isinstance(x[i], int)) and (not isinstance(y[j], int)):
                                        z[i][k] += x[i][j] * y[j][k]
                                elif isinstance(x[i], int):
                                        z[i][k] += x[i] * y[j][k]
                                else:
                                        z[i][k] += x[i][j] * y[j]
        return z

def matrixMethod(a, b):
        a = copy(a)
        b = copy(b)
        inv_a = getInverseMatrix(a)
        return matrixProduct(inv_a, b)

def cramerMethod(matrix, col):
        assert matrix.shape[0] == matrix.shape[1]
        n = matrix.shape[0]
        det = getDet(matrix)
        if det == 0:
                print('Определитель равен нулю, решение методом Крамера невозможно!')
                return
        x = Matrix([])
        for i in range(n):
                print('{} / {} = {}'.format( getDet(swapRowsL(matrix, i, col)), det, getDet(swapRowsL(matrix, i, col)) / det ))
                #x.append(getDet(swapRowsL(matrix, i, col)) / det)
        #return x

def __main__():
        A = Matrix([ [ 5, 6, 9 ], [ 3, 8, 2 ], [7, 1, 2] ])
        B = Matrix([ 452, 245, 171 ])
        cramerMethod(A, B)
        #from numpy.linalg import solve
        #test2 = solve(A, B)
        #print('t1: {}\nt2: {}'.format(test, test2))

if __name__ == '__main__':
        __main__() 