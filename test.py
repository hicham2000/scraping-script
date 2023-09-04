import numpy as np




class OnlineMoments:
    def __init__(self):
        self.N = 0
        self.m = 0
        self.v = 0

    def update(self, x):
        self.N += 1
        w = 1 / self.N
        d = x - self.m
        self.m += d * w
        self.v += d * (x - self.m)

    def mean(self):
        return self.m

    def var(self):
        if self.N > 1:
            return self.v / (self.N - 1)
        else:
            return 0  # Variance is undefined for a single data point

# Testing the OnlineMoments class
om = OnlineMoments()
om.update(1)
om.update(1)
om.update(1)
assert om.mean() == 1
assert om.var() == 0

om = OnlineMoments()
om.update(1)
om.update(2)
om.update(3)
assert om.mean() == 2
assert np.isclose(om.var(), np.var([1, 2, 3]))
