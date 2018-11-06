#coding=utf-8

from random import randint

class Matrix(list):
        @classmethod
        def zeros(cls, shape):
                n_rows, n_cols = shape
                return cls([[0] * n_cols for i in range(n_rows)])

        @classmethod
        def random(cls, shape):
                M, (n_rows, n_cols) = cls(), shape
                for i in range(n_rows):
                        M.append([randint(-255, 255) for i in range(n_cols)])
                return M

        @property
        def shape(self):
                return ((0, 0) if not self else
                        (len(self), 1 if isinstance(self[0], int) else len(self[0])))
