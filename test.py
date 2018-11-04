#!/usr/bin/env python3
#coding=utf-8


t = [[1, 2, 3], [4, 5, 6], [4, 8, 9]]

def addLists(l1, l2):
	return [ l1[i] + l2[i] for i in range(len(l1)) ]

def mulToNumb(l, n):
	return [ i * n for i in l ]

def addRows(matrix, from_row, to_row, coefficient=1):
	matrix[to_row] = addLists(mulToNumb(matrix[from_row], coefficient), matrix[to_row])
	return matrix

for i in range(len(t)):
	temp = t[0][i]
	for j in range(len(t[0])):
		t = addRows(t, )
