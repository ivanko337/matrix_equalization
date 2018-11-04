class SquareMatrix:
    def __init__(self, dim):
        self.data = [[] for i in range(dim)]
        self.dim = dim

    @classmethod
    def random(self, n):
        from random import random
        res = SquareMatrix(n)
        for i in range(n):
            for j in range(n):
                res[i, j] = random()
        return res

    def __getitem__(self, (i, j)):
        assert i < self.dim and j < self.dim
        return self.data[i, j]

    def __setitem__(self, (i, j), val):
        assert i < self.dim and j < self.dim
        self.data[i, j] = val

    def minor(self, (i, j)):
        n = self.dim
        assert i < n and j < n
        res = SquareMatrix(n - 1)
        for k in range(n):
            for l in range(n):
                if k == i or l == j: continue
                if k < i:
                    K = k
                else:
                    K = k - 1
                if l < j:
                    L = l
                else:
                    L = l - 1
                res[K, L] = self[k, l]
        return res

    def det(self, i=0):
        n = self.dim
        if n == 1:
            return self.data[0, 0]
        res = 0
        for j in range(n):
            res += ( (-1) ** (i + j) ) * self[i, j] * self.minor((i, j)).det()
        return res

    