#!/usr/bin/env python3
#coding=utf-8

def mulL(l, n):
	return [ i * n for i in l ]

def addLists(l1, l2, coefficient=1):
	l1 = mulL(l1, coefficient)
	return [ l1[i] + l2[i] for i in range(len(l1)) ]

def addRows(matrix, row1, row2, coefficient):
	matrix[row2] = addLists(matrix[row1], matrix[row2], coefficient)
	return matrix

def tr(matrix):
	for i in range(len(matrix[0]) - 1):
		for j in range(len(matrix) - 1):
			if matrix[i][j] != 0:
				coefficient = matrix[j + 1][i] / matrix[i][j]
			else:
				coefficient = 1
			matrix = addRows(matrix, j, j + 1, coefficient * -1)
	return matrix

t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(tr(t))
