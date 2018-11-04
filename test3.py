#!/usr/bin/env python3
#coding=utf-8

def addColumn(matrix, col):
    if len(matrix) != len(col):
        print('Length of column is not equals length of matrix!')
        return matrix
    for i in range(len(matrix)):
        matrix[i].append(col[i])
    return matrix