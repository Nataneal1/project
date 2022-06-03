class SparseArray(object):

    def __init__(self, items=0):
        self.L = [0] * items

    def __setitem__(self, j, e):
        self.L[j] = e

    def __getitem__(self, j):
        return self.L[j]

    def __str__(self):
        return str(self.L)


a = SparseArray(6)

a[0] = (1, "a")

a[1] = (2, "b")

a[2] = (3, "c")

a[3] = (4, "d")

a[4] = (5, "e")

a[5] = (6, "f")

print("Sparse Array Content: \n", a)