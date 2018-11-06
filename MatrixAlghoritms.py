#coding=utf-8

from MyMatrix import Matrix
from copy import deepcopy

def minor(matrix, i, j):
    matrix = deepcopy(matrix)
    minor = Matrix([row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])])
    return minor

def getDet(matrix):
    matrix = deepcopy(matrix)
    assert matrix.shape[0] == matrix.shape[1]
    n = matrix.shape[0]
    if n == 1:
        return matrix[0][0]
    res = 0
    for i in range(n):
        res += ((-1) ** i) * matrix[0][i] * getDet(minor(matrix, 0, i))
    return res

def matrixProduct(x, y):
    x = deepcopy(x); y = deepcopy(y)
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

def count(l, item):
    res = 0
    for i in l:
        if i == item: res += 1
    return res

def toTriangleShape(matr):
    matr = deepcopy(matr)
    if matr[0][0] == 0:
        matr = swapRows(matr, 0, -1)
    for i in range(len(matr)):
        for j in range(i + 1, len(matr)):
            coefficient = float(matr[j][i]) / float(matr[i][i])
            coefficient = -coefficient
            matr[j] = addRows(matr, i, j, coefficient)
    for i in range(len(matr)):
        matr[i] = mulL(matr[i], 1. / matr[i][i])
    return matr

def addMatrix(matrix1, matrix2):
    matrix1 = deepcopy(matrix1)
    matrix2 = deepcopy(matrix2)
    if len(matrix1) != len(matrix2):
        return matrix1
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            matrix1[i].append(matrix2[i][j])
    return matrix1

def addColumn(matrix, col, col_is_matrix=False):
    matrix = deepcopy(matrix)
    if col_is_matrix:
        return addMatrix(matrix, col)
    if len(matrix) != len(col):
        return matrix
    for i in range(len(matrix)):
        matrix[i].append(col[i])
    return matrix

def mulL(l, n):
    l = deepcopy(l)
    return [ i * n for i in l ]

def getCol(matrix, col, end):
    matrix = deepcopy(matrix)
    return Matrix([i[int(col):end] for i in matrix])

def addLists(l1, l2, coefficient=1):
    assert len(l1) == len(l2)
    l1 = deepcopy(l1)
    l2 = deepcopy(l2)
    l1 = mulL(l1, coefficient)
    return [ l1[i] + l2[i] for i in range(len(l1)) ]

def addRows(matrix, row1, row2, coefficient):
    matrix = deepcopy(matrix)
    row1 = deepcopy(row1)
    row2 = deepcopy(row2)
    res = addLists(matrix[row1], matrix[row2], coefficient)
    return res

#for Cramer
def swapRowsL(matrix, row_ind, row_s):
    matrix = deepcopy(matrix)
    assert len(matrix) == len(row_s)
    for i in range(len(matrix)):
        matrix[i][row_ind] = row_s[i]
    return matrix

def swapRows(matrix, row1, row2):
    matrix = deepcopy(matrix)
    if isinstance(row2, list):
        swapRowsL(matrix, row1, row2)
    if row1 == row2:
        return matrix
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix

def findMinFirstEl(matrix):
    matrix = deepcopy(matrix)
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

def toUnitShape(matrix, col=Matrix([]), col_is_matr=False):
    matrix = deepcopy(matrix)
    matrix = addColumn(matrix, col, col_is_matrix=col_is_matr)
    for i in range(len(matrix)):
        matrix[i] = mulL(matrix[i], 1. / matrix[i][i])
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            coefficient = matrix[j][i] / matrix[i][i]
            coefficient = -coefficient
            matrix[j] = addRows(matrix, i, j, coefficient)
    for i in range(len(matrix)):
        matrix[i] = mulL(matrix[i], 1 / matrix[i][i])
    for i in range(len(matrix)):
        for j in range(i):
            coefficient = matrix[j][i] / matrix[i][i]
            coefficient = -coefficient
            matrix[j] = addRows(matrix, i, j, coefficient)
    return matrix

def getInverseMatrix(matrix):
    matrix = deepcopy(matrix)
    if getDet(matrix) == 0:
        print('Matrix is nondegenerate')
        return matrix
    n = len(matrix)
    matrix = toUnitShape(matrix, getUnitMatrix(n), col_is_matr=True)
    n = len(matrix[0])
    matrix = getCol(matrix, n / 2, n)
    return matrix