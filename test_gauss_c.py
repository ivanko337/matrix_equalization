#!/usr/bin/env python
#coding=utf-8

from copy import deepcopy
from numpy import *


def swapRows(v, i, j):
    """Swaps rows i and j of vector or matrix [v].(transponse)"""
        if len(v) == 1:
                v[i],v[j] = v[j],v[i]
        else:
                temp = v[i].copy() #make the copy on [i] string
                v[i] = v[j]
                v[j] = temp

def pivoting(a, b):
        """changes matrix A by pivoting
        (The element in the diagonal of a matrix by which other elements are divided in an algorithm such as Gauss-Jordan elimination is called the pivot element.
        It is a non-zero element """

        n = len(b)
        """(argmax (from numpy) Indices of the maximum values along an axis.) In case of multiple occurrences of the maximum values, the indices corresponding to the first occurrence are returned
        abs = Return the absolute value of a number

        """

        for k in range(n - 1):
                p = int(argmax(abs(a[k:n, k]))) + k
                if (p != k):
                        swapRows(b, k, p)
                        swapRows(a, k, p)

def gauss(a, b, t=1.0e-9, verbose=False):
        """ Solves [a|b] by gauss elimination"""

        n = len(b)

        # make copies of a and b so as not to change the values in the arguments
        tempa = deepcopy(a)
        tempb = deepcopy(b)

        # check if matrix is singular. A square matrix is singular if and only if its determinant is 0.
        #esli modul oprdelitelya matrici men'she
        if abs(linalg.det(tempa)) < t:
                print "asn"
                return -1

        pivoting(tempa, tempb)

        for k in range(n - 1):
               for i in range(k + 1, n):
                        if tempa[i, k] != 0.0:
                                m = tempa[i, k] / tempa[k, k]

        # Back substitution
        for k in range(n-1,-1,-1):
                tempb[k] = (tempb[k] - dot(tempa[k, k + 1:n], tempb[k + 1:n])) / tempa[k, k]

        return tempb


a = array([[11., 0.11, 0.11, 0.11, 0.11, 0.11, 0.11],
                [0.12, 12., 0.12, 0.12, 0.12, 0.12, 0.12],
                [0.13, 0.13, 13., 0.13, 0.13, 0.13, 0.13],
                [0.14, 0.14, 0.14, 14., 0.14, 0.14, 0.14],
                [0.15, 0.15, 0.15, 0.15, 15., 0.15, 0.15],
                [0.16, 0.16, 0.16, 0.16, 0.16, 16., 0.16],
                [0.17, 0.17, 0.17, 0.17, 0.17, 0.17, 17.]])

b = array([11., 12., 13., 14., 15., 16., 17.])

x = gauss(a, b)
print "Solution. X = ", x

#sol = linalg.solve(a, b)
#print "linalg Solution = ", sol