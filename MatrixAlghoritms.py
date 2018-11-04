from MyMatrix import Matrix
from copy import copy

def minor(matrix, i, j):
    matrix = copy(matrix)
    minor = Matrix([row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])])
    return minor

def getDet(matrix):
    matrix = copy(matrix)
    assert matrix.shape[0] == matrix.shape[1]
    n = matrix.shape[0]
    if n == 1:
        return matrix[0][0]
    res = 0
    for i in range(n):
        res += ((-1) ** i) * matrix[0][i] * getDet(minor(matrix, 0, i))
    return res