import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

PI = 0
for X, Y in zip(a, b):
    PI += X*Y

print(PI)