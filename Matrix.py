#!/usr/bin/env python3
#coding=utf-8

import numpy as np

"""def getMinor(matrix, el_ind):
	res = []
	for i in range(len(matrix)):
		r = []
		for j in range(len(matrix[0])):
			if j != en_ind:
				r.append(matrix[i][j])
		res.append(r)
	return res

def det(matrix, iteration_count, digital_index, sum, numb):
        if iteration_count % 2 == 0:
                sign = -1
        else:
                sign = 1

	if len(matrix[0]) == 2:
		return (sum + (numb * sign * (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])))
"""

def toUnix(matrix): # hz
	res = []
	if len(matrix) != len(matrix[0]):
		print('Only for square matrix!')
		return
	for i in range(len(matrix[0])):
		temp = matrix[0][i]
		for j in range(len(matrix)):
			tn = -matrix[j][i] / temp
			matrix[j][i] *= tn
	return matrix

def toTriangle(matrix):
	for i in range(len(matrix[0])):
		temp = matrix[0][i]
		for j in range(i, len(matrix)):
			if j - 1 < len(matrix):
				continue
			tn = -(matrix[j - 1][i] / matrix[j][i])
			matrix[j][i] += tn
	return matrix

a = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(a.)
